# Module 110 — Using Web Proxies
## Section 8: Encoding/Decoding

Downloaded the section's attached file. Content was encoded in layers:
1. Base64 decode (x3, repeated)
2. URL-decode

Using Burp's Decoder (or `base64 -d` three times + `urllib.parse.unquote` once) recovers the flag.

**Flag:** `HTB{3nc0d1n6_n1nj4}`
