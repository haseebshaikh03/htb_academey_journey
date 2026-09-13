# Module 144 — Information Gathering - Web Edition
## Session progress notes (63.16% -> 84.21% this run)

These sections do NOT require the shared/contested HTB lab VM slot — they're pure OSINT / theory sections against static reference material, so they were completed without needing to spawn a target:

## Automating Recon (Chapter 8)
Theory-only section covering FinalRecon, Recon-ng, theHarvester, SpiderFoot, OSINT Framework. No questions — marked complete after reading.

## Search Engine Discovery (Chapter 6)
Theory-only section on Google Dorking (`site:`, `inurl:`, `filetype:` operators) and the Google Hacking Database. No questions — marked complete after reading.

## Creepy Crawlies / Well-Known URIs (Crawling chapter, remaining 2 sections)
**Well-Known URIs:** theory-only (RFC 8615 `/.well-known/` standard, e.g. `/.well-known/openid-configuration`). No questions — marked complete.
Other Crawling sub-section found already previously completed on revisit.

## robots.txt / Subdomains intro (DNS & Subdomains chapter, remaining section)
**Subdomains** (intro theory page, chapter 3): no questions, marked complete. Other DNS&Subdomains sub-sections (Subdomain Bruteforcing, DNS Zone Transfers, Certificate Transparency Logs) were already completed from a prior session.

## Virtual Hosts (DNS & Subdomains) — 4 of 5 questions answered
**Approach:** spawned the module's target (an `inlanefreight.htb` vhost-routing web app on a floating IP:port, e.g. `154.57.164.x:3xxxx` — a different target type than the usual 10.129.x.x VPN lab VM, reachable directly over the internet from the attack box, no VPN needed). Brute-forced virtual hosts with:
```
gobuster vhost -u http://<ip:port>/ --domain inlanefreight.htb --append-domain -w <subdomain-wordlist> -t <threads> -q
```
using SecLists' `subdomains-top1million-*.txt` wordlists, and confirmed each with `curl -H "Host: <name>.inlanefreight.htb" http://<ip:port>/` (comparing response `Content-Length` against the ~116-byte default/no-match baseline). This surfaced real vhosts `support`, `admin`, `browse`, `vm5` (also `blog`/`forum`, which aren't part of the 5 graded prefixes) and matched them to the question prefixes "su", "a", "br", "vm" — all 4 submitted and confirmed correct.

**BLOCKED — Question 1 ("web" prefix):** exhaustively brute-forced ~12,600+ words starting with "web" (SecLists top-20k/110k plus the n0kovo huge subdomain list filtered to `^web`) against multiple fresh spawns of this target — no distinct vhost found; every candidate returned the same default-page byte size. Also tried numeric suffixes (`web0`-`web99`), hyphen/underscore variants, and case variants (`Web`/`WEB`). No hit. This target type also appears to auto-cycle to a new IP:port every 1-2 minutes (independent of the account-wide spawn contention), which limited how long any single brute-force pass could run — worth retrying with a fresh spawn and a very large wordlist (or the module's own suggested `subdomains-top1million-110000.txt` run to completion in one pass) in a future session.

## BLOCKED — Skills Assessment Q3/Q4/Q5 (unchanged from before, re-verified this session)
Re-spawned the target and re-tested: this specific `inlanefreight.htb` instance returns the **exact same static placeholder page** (`<h1>Welcome to inlanefreight.htb</h1>`, ~120 bytes) for every Host header and every path tried — confirmed via `gobuster dir` (SecLists `raft-medium-directories.txt`, ~30k words, only `/index.html` found) and `gobuster vhost` (SecLists top-20k, zero distinct vhosts — every Host header returns the identical byte-for-byte response, unlike the *Virtual Hosts* section's target which does differentiate). robots.txt/sitemap.xml return real nginx 404s (so the box itself is alive and correctly proxying), just with no discoverable hidden admin directory or crawlable content on this instance. Conclusion stands from the prior session: this specific skills-assessment target instance is not behaving as the lesson describes — worth an HTB support ticket referencing module 144 section 1311, or trying HTB's official step-by-step solution (PRO feature).

## Remaining incomplete (module now at 84.21%)
- DNS & Subdomains: Virtual Hosts section, Question 1 ("web" prefix) only.
- Crawling: shows 3/4 — one sub-section reverted to incomplete on a later revisit; recheck next session.
- Skills Assessment: Questions 3, 4, 5 (see BLOCKED above).
