# Module 23 — File Inclusion
## Section 9: Automated Scanning

Fuzzed for the vulnerable parameter name using SecLists' `burp-parameter-names.txt` — a small hand-built list found nothing; the full SecLists wordlist found the vulnerable parameter.

The vulnerable parameter needed an unusually deep traversal (~18+ levels of `../`) to reach the filesystem root and read the flag file.

**Flag** found via automated parameter fuzzing followed by a deep directory-traversal LFI payload.
