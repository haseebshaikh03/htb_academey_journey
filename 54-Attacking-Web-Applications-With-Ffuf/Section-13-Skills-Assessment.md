# Module 54 — Attacking Web Applications With Ffuf
## Section 13: Skills Assessment (5 questions)

**Q1 — subdomains found:**
Discovered via vhost (Host-header) fuzzing against the base domain with ffuf, filtering out the default catch-all response. Several subdomains were identified this way.

**Q2 — extensions accepted by the domains — BLOCKED (format issue, technique re-confirmed correct on a fresh target):**
Re-ran the full recon end-to-end on a freshly-spawned instance to rule out stale-target artifacts:
1. Re-discovered the same set of vhosts via `ffuf -w subdomains-top1million-{5000,20000,110000}.txt -u http://<IP>:<PORT>/ -H "Host: FUZZ.academy.htb" -fs <baseline-size>` (baseline = default landing-page byte count). Cross-checked with 3 different wordlist sizes — same hits every time, so the vhost list is stable/complete.
2. Ran `ffuf -w web-extensions.txt -u http://<IP>:<PORT>/indexFUZZ -H "Host: <vhost>.academy.htb" -mc 200` against each discovered vhost. Result pattern matches the original finding exactly: one extension returns 200 on *all* vhosts, and one additional, less-common extension returns 200 on exactly *one* of them. (Also checked a `.phps`-style hit that shows up under `-mc all -fc 404` — that one is a generic Apache "source view forbidden" 403 unrelated to the app, confirmed a red herring via direct curl, not part of the real answer set.)
3. Verified with direct `curl -H "Host: ..."` requests (not just ffuf) that these are true positives (200/consistent) vs. a bogus extension (404), on all three vhosts.

**Format attempts (all rejected by the grader, ~30 variants tried across two sessions):** plain comma list, with/without leading dots, with/without spaces, reordered, newline/pipe/semicolon-separated, "X and Y", singular-only answers, upper-case, trailing punctuation.

**Conclusion:** the underlying recon (vhosts + accepted extensions) is reproducible and consistent across independent fresh target spawns, so the technique is right. The grader is rejecting every reasonable string format tried. Suspect the module's expected-answer regex wants something not yet tried (e.g. worded as a full sentence, or referencing which specific vhost has the extra extension) — worth checking HTB's official Discord/forum thread for this exact question if revisiting.

**Q3 — full vulnerable URL:**
Constructed from the vhost and extension identified in Q1/Q2, pointing at a specific course page discovered during directory/page fuzzing of that vhost.

**Q4 — parameter name(s) found:**
Discovered via GET parameter fuzzing against the vulnerable page, filtering the baseline "unrecognized parameter" response size.

**Q5 — final flag:**
Flag obtained by chaining the above steps (vhost discovery, extension fuzzing, directory/page fuzzing, and parameter fuzzing) to reach and access the vulnerable endpoint.
