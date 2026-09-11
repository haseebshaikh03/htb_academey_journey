# Module 110 — Using Web Proxies
## Section 10: Burp Intruder

Target path: `/admin/FUZZ.html`

**Wordlist:** SecLists `raft-small-words.txt`

Fuzzed the FUZZ position with Intruder (Sniper mode) against `/admin/FUZZ.html` → hit `/admin/2010.html`, which contained the flag.

**Flag:** `HTB{burp_1n7rud3r_fuzz3r!}`
