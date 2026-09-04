/**
 * Record-level reconciliation: authority schedule JSON vs local generated file.
 * Compares date|ship|cruiseLine|arrival|departure fingerprints.
 *
 * Usage: npm run qa:schedules
 */
import { readFileSync, existsSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, "..");
const config = JSON.parse(readFileSync(path.join(__dirname, "destination.config.json"), "utf8"));

function fail(msg) {
  console.error(`qa:schedules FAIL: ${msg}`);
  process.exit(1);
}

function fp(c) {
  const arrival = c.arrival ?? "";
  const departure = c.departure ?? "";
  const line = c.cruiseLine || c.cruise_line || "";
  return `${c.date}|${c.ship}|${line}|${arrival}|${departure}`;
}

function loadAuthority() {
  const p = path.resolve(root, config.authoritySource);
  if (!existsSync(p)) fail(`Authority missing: ${p}`);
  const data = JSON.parse(readFileSync(p, "utf8"));
  if (!Array.isArray(data)) fail("Authority must be array");
  return data.map((c) => ({
    date: c.date,
    ship: c.ship,
    cruiseLine: c.cruiseLine || c.cruise_line,
    arrival: c.arrival || null,
    departure: c.departure || null,
  }));
}

function loadLocal() {
  const p = path.resolve(root, config.localOutput);
  if (!existsSync(p)) fail(`Local generated missing: ${p} — run npm run sync:schedules`);
  const data = JSON.parse(readFileSync(p, "utf8"));
  return (data.calls || []).map((c) => ({
    date: c.date,
    ship: c.ship,
    cruiseLine: c.cruiseLine,
    arrival: c.arrival,
    departure: c.departure,
  }));
}

function monthSum(calls) {
  const byMonth = {};
  for (const c of calls) {
    const m = c.date.slice(0, 7);
    byMonth[m] = (byMonth[m] || 0) + 1;
  }
  return byMonth;
}

/** Tokens that identify THIS destination — exclude from foreign-port scans. */
function ownPortTokens() {
  const tokens = new Set();
  const slug = String(config.portSlug || "").toLowerCase();
  const name = String(config.destinationName || "").toLowerCase();
  for (const raw of [slug, name]) {
    if (!raw) continue;
    tokens.add(raw);
    tokens.add(raw.replace(/-/g, " "));
    tokens.add(raw.replace(/\s+/g, "-"));
    tokens.add(raw.replace(/[-\s]/g, ""));
  }
  return tokens;
}

function isOwnPortMention(mention) {
  const own = ownPortTokens();
  const n = mention.toLowerCase();
  const variants = [n, n.replace(/-/g, " "), n.replace(/\s+/g, "-"), n.replace(/[-\s]/g, "")];
  return variants.some((v) => own.has(v));
}

function main() {
  const auth = loadAuthority();
  const local = loadLocal();
  const authSet = new Map();
  const localSet = new Map();

  for (const c of auth) {
    const k = fp(c);
    authSet.set(k, (authSet.get(k) || 0) + 1);
  }
  for (const c of local) {
    const k = fp(c);
    localSet.set(k, (localSet.get(k) || 0) + 1);
  }

  let missing = 0;
  let extra = 0;
  let changed = 0; // treated as missing+extra pairs; report separately via set diff

  for (const [k, n] of authSet) {
    const ln = localSet.get(k) || 0;
    if (ln < n) missing += n - ln;
  }
  for (const [k, n] of localSet) {
    const an = authSet.get(k) || 0;
    if (n > an) extra += n - an;
  }

  // Cross-port string scan in local file raw text
  const localRaw = readFileSync(path.resolve(root, config.localOutput), "utf8").toLowerCase();
  const allForeignPorts = [
    "aruba",
    "nassau",
    "costa maya",
    "costa-maya",
    "st maarten",
    "st-maarten",
    "roatan",
    "tortola",
    "bonaire",
    "dominica",
    "grand cayman",
    "grand-cayman",
    "ocho rios",
    "cozumel",
  ];
  const foreignPorts = allForeignPorts.filter((p) => !isOwnPortMention(p));
  const hits = foreignPorts.filter((p) => localRaw.includes(p));
  // Allow only if they appear inside ship names accidentally — flag for review
  // Strict: none of these should appear as port identity fields; we check for "port":
  const contamination = [];
  for (const p of hits) {
    if (localRaw.includes(`"port": "${p}"`) || localRaw.includes(`"portslug": "${p}"`)) {
      contamination.push(p);
    }
  }

  const byYearAuth = {};
  for (const c of auth) {
    const y = c.date.slice(0, 4);
    byYearAuth[y] = (byYearAuth[y] || 0) + 1;
  }
  const byMonthLocal = monthSum(local);
  const monthTotal = Object.values(byMonthLocal).reduce((a, b) => a + b, 0);

  console.log(
    JSON.stringify(
      {
        authorityCalls: auth.length,
        localCalls: local.length,
        byYearAuth,
        monthSumEqualsLocal: monthTotal === local.length,
        missing,
        extra,
        changed,
        duplicatesIntroduced: [...localSet.values()].filter((n) => n > 1).length,
        crossPortContamination: contamination,
        foreignStringMentionsReview: hits,
      },
      null,
      2,
    ),
  );

  if (auth.length !== local.length) fail(`Count mismatch auth=${auth.length} local=${local.length}`);
  if (missing || extra) fail(`Record diff missing=${missing} extra=${extra}`);
  if (contamination.length) fail(`Cross-port contamination: ${contamination.join(", ")}`);
  if (monthTotal !== local.length) fail("Month sum != local calls");

  const expected = config.expectedTotals;
  if (auth.length !== expected.total) fail(`Auth total != baseline ${expected.total}`);
  for (const [y, n] of Object.entries(expected.byYear)) {
    if ((byYearAuth[y] || 0) !== n) fail(`Year ${y} baseline fail`);
  }

  console.log("qa:schedules PASS");
}

main();
