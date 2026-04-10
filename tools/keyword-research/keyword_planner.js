/**
 * Google Keyword Planner Automation
 *
 * Launches Windows Chrome with a separate automation profile (kp_session/).
 * Your existing Chrome and its profile are NOT touched.
 *
 * FIRST RUN: A Chrome window will open — log in with fahad@supple.com.au
 *            and select "Hardik Supple Solutions". Session is saved after that.
 *
 * USAGE:
 *   node keyword_planner.js "keyword1" "keyword2"
 *   node keyword_planner.js --file keywords.txt
 */

const { chromium } = require('playwright');
const { execSync, spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const readline = require('readline');

const DEBUG_PORT = 9223; // different port so it doesn't conflict with anything
const CHROME_WIN_PATH = '/mnt/c/Program Files/Google/Chrome/Application/chrome.exe';
// Windows path for the session dir (Chrome needs a Windows path)
const SESSION_DIR_WSL = path.join(__dirname, 'kp_session');
const KP_URL = 'https://ads.google.com/aw/keywordplanner/ideas/new';

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

function wslToWindowsPath(wslPath) {
  // Convert /home/invoi/... -> \\wsl.localhost\Ubuntu\home\invoi\...
  return wslPath.replace(/^\/mnt\/([a-z])\//, '$1:\\').replace(/\//g, '\\');
}

function isChromeDebugging() {
  try {
    execSync(`curl -s http://localhost:${DEBUG_PORT}/json/version --max-time 2`, {
      encoding: 'utf8', stdio: ['pipe', 'pipe', 'ignore']
    });
    return true;
  } catch {
    return false;
  }
}

async function launchWindowsChrome() {
  // Convert WSL path to Windows UNC path for Chrome
  const sessionWinPath = `\\\\wsl.localhost\\Ubuntu${SESSION_DIR_WSL}`;

  console.log('Launching Windows Chrome with automation profile...');
  console.log('(Your existing Chrome is not affected)');

  // Use powershell.exe to launch Chrome on Windows side
  const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
  const args = [
    `--remote-debugging-port=${DEBUG_PORT}`,
    `--user-data-dir=${sessionWinPath}`,
    '--no-first-run',
    '--window-size=1400,900',
  ].join(' ');
  const psCmd = `& 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe' ${args}`;

  execSync(`powershell.exe -Command "${psCmd}"`, { stdio: 'inherit' });

  // Wait for Chrome to be ready
  console.log('Waiting for Chrome to start...');
  const start = Date.now();
  while (Date.now() - start < 20000) {
    if (isChromeDebugging()) return true;
    await sleep(1000);
  }
  return false;
}

async function getKeywordData(keywords) {
  // Launch Windows Chrome if not already running with debug port
  if (!isChromeDebugging()) {
    const ready = await launchWindowsChrome();
    if (!ready) {
      console.error('Chrome did not start with debugging. Exiting.');
      process.exit(1);
    }
  } else {
    console.log(`Chrome already running on port ${DEBUG_PORT}`);
  }

  console.log('Connecting to Chrome...');
  const browser = await chromium.connectOverCDP(`http://localhost:${DEBUG_PORT}`);

  const contexts = browser.contexts();
  const context = contexts[0] || await browser.newContext();
  const page = await context.newPage();

  console.log('Navigating to Keyword Planner...');
  try {
    await page.goto(KP_URL, { waitUntil: 'domcontentloaded', timeout: 60000 });
  } catch (e) { /* ignore timeout */ }
  await sleep(3000);

  const url = page.url();
  console.log('Current URL:', url);

  // ── Handle login ──────────────────────────────────────────────────────────
  if (url.includes('accounts.google.com') || url.includes('signin') || url.includes('ServiceLogin')) {
    console.log('\n>>> A Chrome window has opened on your Windows desktop.');
    console.log('>>> Please log in with fahad@supple.com.au and select "Hardik Supple Solutions".');
    console.log('>>> Waiting up to 8 minutes...\n');
    try {
      await page.waitForURL(u => u.includes('ads.google.com/aw'), { timeout: 480000 });
      console.log('Login detected!');
    } catch (e) {
      console.log('Timed out waiting for login.');
    }
    await sleep(2000);
    try {
      await page.goto(KP_URL, { waitUntil: 'domcontentloaded', timeout: 60000 });
    } catch (e) { /* ignore */ }
    await sleep(4000);
  }

  // ── Handle account selector ───────────────────────────────────────────────
  const afterLoginUrl = page.url();
  if (!afterLoginUrl.includes('keywordplanner')) {
    console.log('Not on Keyword Planner yet:', afterLoginUrl);
    console.log('If an account chooser is showing, please select "Hardik Supple Solutions".');
    console.log('Waiting up to 90s...');
    try {
      await page.waitForURL(u => u.includes('keywordplanner'), { timeout: 90000 });
    } catch (e) {
      try {
        await page.goto(KP_URL, { waitUntil: 'domcontentloaded', timeout: 30000 });
      } catch (e2) { /* ignore */ }
    }
    await sleep(3000);
  }

  await page.screenshot({ path: 'kp_loaded.png' });
  console.log('Screenshot: kp_loaded.png');

  // ── Find keyword input ────────────────────────────────────────────────────
  console.log('Looking for keyword input...');
  let inputField = null;
  const inputSelectors = [
    'textarea[jsname]',
    'textarea[aria-label*="keyword" i]',
    'textarea[placeholder*="keyword" i]',
    'input[aria-label*="keyword" i]',
    'input[placeholder*="keyword" i]',
    'div[contenteditable="true"]',
    'textarea',
  ];

  for (const sel of inputSelectors) {
    try {
      const el = await page.$(sel);
      if (el && await el.isVisible()) {
        inputField = el;
        console.log(`Found input: ${sel}`);
        break;
      }
    } catch (e) { /* try next */ }
  }

  if (!inputField) {
    fs.writeFileSync('page_debug.html', await page.content());
    await page.screenshot({ path: 'debug_no_input.png', fullPage: true });
    console.log('ERROR: Keyword input not found. Saved page_debug.html and debug_no_input.png');
    await browser.close();
    return;
  }

  // ── Enter keywords ────────────────────────────────────────────────────────
  await inputField.click({ clickCount: 3 });
  await page.keyboard.press('Control+a');
  await inputField.fill('');
  for (let i = 0; i < keywords.length; i++) {
    await inputField.type(keywords[i]);
    if (i < keywords.length - 1) await page.keyboard.press('Enter');
  }
  console.log(`Entered ${keywords.length} keyword(s)`);

  // ── Submit ────────────────────────────────────────────────────────────────
  const submitSelectors = [
    'button:has-text("Get results")',
    'button:has-text("Get keyword ideas")',
    'button:has-text("Search")',
    '[data-uf="get-keyword-ideas-button"]',
  ];

  let submitted = false;
  for (const sel of submitSelectors) {
    try {
      const btn = await page.$(sel);
      if (btn && await btn.isVisible()) {
        await btn.click();
        submitted = true;
        console.log(`Clicked: ${sel}`);
        break;
      }
    } catch (e) { /* try next */ }
  }

  if (!submitted) {
    await page.keyboard.press('Enter');
    console.log('Submitted via Enter key');
  }

  // ── Wait for results ──────────────────────────────────────────────────────
  console.log('Waiting for results to load...');
  await sleep(10000);
  await page.screenshot({ path: 'results.png', fullPage: true });
  console.log('Results screenshot: results.png');

  // ── Extract data ──────────────────────────────────────────────────────────
  const results = await page.evaluate(() => {
    const data = [];
    document.querySelectorAll('tr').forEach(row => {
      const cells = [...row.querySelectorAll('td')];
      if (cells.length >= 2) {
        const vals = cells.map(c => (c.innerText || '').trim().replace(/\s+/g, ' '));
        if (vals[0]) data.push(vals);
      }
    });
    if (!data.length) {
      document.querySelectorAll('[role="row"]').forEach(row => {
        const cells = [...row.querySelectorAll('[role="gridcell"], [role="cell"]')];
        if (cells.length >= 2) {
          const vals = cells.map(c => (c.innerText || '').trim().replace(/\s+/g, ' '));
          if (vals[0]) data.push(vals);
        }
      });
    }
    return data;
  });

  if (results.length > 0) {
    const cols = ['Keyword', 'Avg Monthly Searches', 'Competition', 'Top Bid Low', 'Top Bid High'];
    console.log(`\n✓ Extracted ${results.length} rows\n`);
    console.log(cols.join(' | '));
    console.log('-'.repeat(90));
    results.slice(0, 50).forEach(r => console.log(r.slice(0, 5).join(' | ')));
    if (results.length > 50) console.log(`  ... and ${results.length - 50} more rows`);

    const csv = cols.join(',') + '\n' +
      results.map(r => r.slice(0, 5).map(c => `"${(c || '').replace(/"/g, '""')}"`).join(',')).join('\n');
    fs.writeFileSync('keyword_results.csv', csv);
    console.log('\nSaved: keyword_results.csv');
  } else {
    console.log('\nNo data extracted. Check results.png.');
  }

  await browser.close();
}

// ── Main ──────────────────────────────────────────────────────────────────────
async function main() {
  const args = process.argv.slice(2);
  let keywords = [];

  const fileFlag = args.indexOf('--file');
  if (fileFlag !== -1 && args[fileFlag + 1]) {
    keywords = fs.readFileSync(args[fileFlag + 1], 'utf8')
      .split('\n').map(k => k.trim()).filter(Boolean);
  } else {
    keywords = args.filter(a => !a.startsWith('--'));
  }

  if (!keywords.length) {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    const answer = await new Promise(resolve =>
      rl.question('Enter keywords (comma-separated): ', resolve)
    );
    rl.close();
    keywords = answer.split(',').map(k => k.trim()).filter(Boolean);
  }

  if (!keywords.length) {
    console.log('Usage:');
    console.log('  node keyword_planner.js "keyword1" "keyword2"');
    console.log('  node keyword_planner.js --file keywords.txt');
    process.exit(1);
  }

  console.log(`Keywords to research: ${keywords.join(', ')}\n`);
  await getKeywordData(keywords);
}

main().catch(err => {
  console.error('\nFatal error:', err.message);
  process.exit(1);
});
