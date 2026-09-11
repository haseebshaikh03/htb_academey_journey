# Module 110 — Using Web Proxies
## Section 15: Skills Assessment (4 questions, one target)

## Q1 — `/lucky.php`
Repeatedly POST the "get flag" parameter — the endpoint has a random chance of returning the flag each time. Automate the retry (Intruder / a loop) until it hits.

## Q2 — `/admin.php` cookie
The session cookie is hex-encoded, then base64-encoded. Hex-decode → base64-decode to reveal an incomplete token.

## Q3 — missing hex character
The decoded token from Q2 is one hex character short of a valid admin session token. Brute-force the missing character (0-9a-f) with Intruder until the app accepts the resulting session as valid admin.

## Q4 — ColdFusion path traversal
Look up Metasploit's `coldfusion_locale_traversal` module and check its default/target directory option.
