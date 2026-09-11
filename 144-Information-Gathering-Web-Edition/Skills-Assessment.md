# Module 144 — Information Gathering - Web Edition
## Skills Assessment (final section, 63.16% reached — 3 of 5 Qs answered)

Target domain: `inlanefreight.htb`

**Q1 — whois IANA ID of the registrar:**
Approach: run `whois inlanefreight.com` and read the registrar's IANA ID out of the whois record.

**Q2 — web server software:**
Approach: request the site and read the `Server:` field from the HTTP response headers (e.g. `curl -I`).

## BLOCKED — Q3, Q4, Q5 (hidden admin API key / crawled email / new API key)

Module's own theory taught: `gobuster vhost -w subdomains-top1million-110000.txt --append-domain`, and a custom crawler tool **ReconSpider** (`python3 ReconSpider.py <url>`) for extracting emails/links/comments — these are the intended tools, confirmed by re-reading the module's earlier sections.

Despite exhaustive testing (5 different large wordlists, ~450k+ combined vhost/dir candidates, robots.txt/sitemap.xml/.well-known/.git/.env/common-CMS-path checks, full 1-65535 port scan, TLS/SNI routing, X-Forwarded-Host header, alternate HTTP methods, thematic logistics/HR-themed guesses, fresh container respawn to rule out staleness) — every single request regardless of Host header/path/method returned the exact same static placeholder page with an identical ETag/Last-Modified.

**Conclusion:** this specific target instance appears to have a genuine deployment/content issue (or needs a technique not covered anywhere in the module/its hints). Worth checking HTB Academy's official "step-by-step solution" (PRO feature) for this exact section, or opening an HTB support ticket referencing module 144 section 1311.
