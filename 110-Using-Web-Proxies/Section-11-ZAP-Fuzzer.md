# Module 110 — Using Web Proxies
## Section 11: ZAP Fuzzer

Target used an MD5-hash cookie for session identification.

**Method:** Fuzzed the cookie value against SecLists `top-usernames-shortlist.txt`, MD5-hashing each candidate username and comparing to the cookie hash, using ZAP's Fuzzer.

**Username found:** `user`

**Flag:** `HTB{fuzz1n6_my_f1r57_c00k13}`
