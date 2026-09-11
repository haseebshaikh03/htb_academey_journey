# Module 110 — Using Web Proxies
## Section 11: ZAP Fuzzer

Target uses an MD5-hash cookie for session identification.

## Approach
Use ZAP's Fuzzer against the cookie value with a username wordlist (SecLists `top-usernames-shortlist.txt`), MD5-hashing each candidate and comparing to the target cookie hash. The matching candidate is the underlying username.
