# Module 58 — SQLMap Essentials
## Section 11: Skills Assessment — BLOCKED (target appears broken)

Target is a static "Minishop" e-commerce template. Ran two exhaustive directory brute-forces (~97k requests total: sqlmap's own `common-files.txt` + SecLists `raft-small-words`/`raft-small-files`).

Only 2 dynamic endpoints found:
- `add.php` → always returns `Access denied for user 'user4'@'localhost'` (the DB connection itself fails, input-independent)
- `action.php` → always a MySQL syntax error around a `rand()`-generated number, with **zero correlation** to any parameter/value/payload/method/header tried (100+ variations)

Reset and fully respawned the target container — identical broken behavior persisted, ruling out a transient glitch. No other files/ports found (`.DS_Store` checked, `/scss/` checked).

**Conclusion:** this looks like a genuinely misconfigured/non-functional target instance rather than a solvable puzzle at the time this was attempted. Retry with a fresh spawn later, or check HTB's module discussion for a known-broken-instance report.
