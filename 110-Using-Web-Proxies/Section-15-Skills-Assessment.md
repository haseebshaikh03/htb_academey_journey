# Module 110 — Using Web Proxies
## Section 15: Skills Assessment (4 questions, one target)

**Q1 — `/lucky.php`:**
Repeatedly POST `getflag=true` — the endpoint has a random chance of returning the flag each time, so send it in a loop/via Intruder until it hits.
**Answer:** `HTB{d154bl3d_bu770n5_w0n7_570p_m3}`

**Q2 — `/admin.php` cookie:**
The session cookie is hex-encoded, then base64-encoded. Hex-decode → base64-decode to reveal a 31-character string.
**Answer:** `3dac93b8cd250aa8c1a36fffc79a17a`

**Q3 — missing 32nd hex character:**
The above 31-char string is one hex character short of a valid admin session token. Brute-forced the missing character (0-9a-f) via Intruder until the app accepted the resulting session as valid admin.
**Answer:** the missing char is `d` (completes the token → grants admin session)
**Flag:** `HTB{burp_1n7rud3r_n1nj4!}`

**Q4 — ColdFusion path traversal:**
Metasploit's `coldfusion_locale_traversal` module's default/target directory.
**Answer:** `CFIDE`
