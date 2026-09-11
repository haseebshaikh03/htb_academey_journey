# Module 103 — Cross-Site Scripting (XSS)
## Phishing (full attack chain)

1. Injection point: `<img src=...>` with a single-quote breakout.
2. Payload used `document.write()` to inject a fake login form over the real page.
3. Form auto-submits to an attacker-controlled log server via `setTimeout(() => form.submit(), <ms>)`.
4. Stood up a simple Python HTTP log server (`/tmp/logserver.py`) on port 80 to receive the POSTed credentials.
5. Victim (admin bot) "logged in" through the fake form, real credentials were captured in the log server.

**Captured admin creds:** `admin` / `p1zd0nt57341myp455`

**Flag:** `HTB{r3f13c73d_cr3d5_84ck_2_m3}`
