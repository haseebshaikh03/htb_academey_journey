# Module 54 — Attacking Web Applications With Ffuf
## Section 3: Directory Fuzzing

`ffuf -w <dirlist> -u http://target/FUZZ`

## Approach
Directory name discovered via wordlist-based fuzzing with ffuf against the target root, filtering the results for a valid (non-404) response to identify the hidden directory.
