# Module 54 — Attacking Web Applications With Ffuf
## Section 7: Sub-domain Fuzzing

`ffuf -w <subdomain-list> -u http://academy.htb/ -H "Host: FUZZ.academy.htb"` (add each hit to `/etc/hosts`)

**Answer:** `customer.inlanefreight.com`
