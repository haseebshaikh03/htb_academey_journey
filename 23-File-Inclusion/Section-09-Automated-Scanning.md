# Module 23 — File Inclusion
## Section 9: Automated Scanning

Fuzzed for the vulnerable parameter name using SecLists' `burp-parameter-names.txt` — a small hand-built list found nothing; the real list found it: parameter `view`.

The `view` parameter needed an unusually deep traversal (~18+ levels of `../`) to reach the filesystem root and read `/flag.txt`.

**Flag:** `HTB{4u70m47!0n_f!nd5_#!dd3n_93m5}`
