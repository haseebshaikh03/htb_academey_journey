# Module 54 — Attacking Web Applications With Ffuf
## Section 5: Recursive Fuzzing

`ffuf -w <wordlist> -u http://target/FUZZ -recursion -recursion-depth 2` (or manually re-fuzzing each newly-found directory) uncovers a nested path holding the flag.

**Flag:** `HTB{fuzz1n6_7h3_w3b!}`
