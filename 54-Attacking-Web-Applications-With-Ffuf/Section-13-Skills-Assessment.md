# Module 54 — Attacking Web Applications With Ffuf
## Section 13: Skills Assessment (5 questions)

**Q1 — subdomains found:**
Discovered via vhost (Host-header) fuzzing against the base domain with ffuf, filtering out the default catch-all response. Several subdomains were identified this way.

**Q2 — extensions accepted by the domains — BLOCKED (format issue, technique confirmed correct):**
Ran an extension-fuzz (`ffuf -w extlist.txt -u http://target/indexFUZZ -H "Host: <vhost>"`) against all discovered vhosts.
Confirmed via curl (200 vs 404 on bogus extensions, ruling out false positives) which extensions were accepted — one extension worked across all vhosts, and a second, less common extension worked on only one of them.
Tried numerous answer-format variants (different casing, separators, orderings) — **all rejected by the grader**. The underlying recon is correct; only the exact expected string format is unknown. Worth checking HTB's official discussion/hint for this exact question's expected format.

**Q3 — full vulnerable URL:**
Constructed from the vhost and extension identified in Q1/Q2, pointing at a specific course page discovered during directory/page fuzzing of that vhost.

**Q4 — parameter name(s) found:**
Discovered via GET parameter fuzzing against the vulnerable page, filtering the baseline "unrecognized parameter" response size.

**Q5 — final flag:**
Flag obtained by chaining the above steps (vhost discovery, extension fuzzing, directory/page fuzzing, and parameter fuzzing) to reach and access the vulnerable endpoint.
