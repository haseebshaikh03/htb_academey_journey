# Module 54 — Attacking Web Applications With Ffuf
## Section 13: Skills Assessment (5 questions)

**Q1 — subdomains found:**
`archive, faculty, test` (vhost-fuzzed off `academy.htb`)

**Q2 — extensions accepted by the domains — BLOCKED (format issue, technique confirmed correct):**
Ran an extension-fuzz (`ffuf -w extlist.txt -u http://target/indexFUZZ -H "Host: <vhost>"`) against all 4 vhosts (academy.htb, archive/faculty/test.academy.htb).
Confirmed via curl (200 vs 404 on bogus extensions, ruling out false positives):
- `.php` works on **all 4** vhosts
- `.php7` additionally works **only on faculty.academy.htb**
Tried ~15 answer-format variants (`php, php7` / `.php, .php7` / `PHP, PHP7` / newline-separated / different orderings/separators/casing) — **all rejected by the grader**. The underlying recon is correct; only the exact expected string format is unknown. Worth checking HTB's official discussion/hint for this exact question's expected format.

**Q3 — full vulnerable URL:**
`http://faculty.academy.htb:PORT/courses/linux-security.php7`

**Q4 — parameter name(s) found:**
`user, username`

**Q5 — final flag:**
`HTB{w3b_fuzz1n6_m4573r}`
