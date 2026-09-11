# Module 110 — Using Web Proxies
## Section 10: Burp Intruder

Target path: `/admin/FUZZ.html`

## Approach
Send the request to Intruder (Sniper mode), set the FUZZ payload position on the filename, and load SecLists' `raft-small-words.txt` as the payload list. Look for a hit with a distinct response (different length/status) — open that page for the flag.
