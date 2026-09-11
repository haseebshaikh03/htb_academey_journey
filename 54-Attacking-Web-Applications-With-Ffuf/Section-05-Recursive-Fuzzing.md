# Module 54 — Attacking Web Applications With Ffuf
## Section 5: Recursive Fuzzing

`ffuf -w <wordlist> -u http://target/FUZZ -recursion -recursion-depth 2` (or manually re-fuzzing each newly-found directory)

## Approach
Recursive fuzzing uncovers a nested path several directories deep. The flag was found on a page inside that nested path.

Flag found by recursively fuzzing directories until a nested hidden path was uncovered.
