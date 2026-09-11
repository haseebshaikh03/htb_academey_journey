# Module 54 — Attacking Web Applications With Ffuf
## Section 9: Filtering Results

Vhost fuzz with a response-size filter (`-fs <baseline-size>`) to exclude the default catch-all page and surface the real one.

## Approach
Vhost/subdomain discovered by fuzzing Host headers and applying a response-size filter (`-fs`) to exclude the default catch-all page, isolating the genuine virtual host.
