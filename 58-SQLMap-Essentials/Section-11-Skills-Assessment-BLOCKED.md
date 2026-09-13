# Module 58 — SQLMap Essentials
## Section 11: Skills Assessment — BLOCKED (broken target + severe account-wide contention)

Target is a static "Minishop" e-commerce template. Ran two exhaustive directory brute-forces (~97k requests total: sqlmap's own `common-files.txt` + SecLists `raft-small-words`/`raft-small-files`) in a prior session.

Only 2 dynamic endpoints found:
- `add.php` → always returns `Access denied for user 'user4'@'localhost'` (the DB connection itself fails, input-independent)
- `action.php` → always a MySQL syntax error around a `rand()`-generated number, with **zero correlation** to any parameter/value/payload/method/header tried (100+ variations)

**This session's re-verification (3 independent fresh spawns, ~1 hour):**
- Reproduced the exact same `add.php`/`action.php` behavior on every fresh instance — confirmed input-independent (tried GET vs POST, JSON body, multipart, `X-Requested-With`, cookies, dozens of plausible field names for a shopping-cart INSERT: `id`, `product_id`, `qty`, `price`, `name`, `session_id`, etc. — the SQL error text is byte-for-byte the same shape every time, only the two `rand()` numbers embedded in it change).
- Re-confirmed with an additional `raft-small-words.txt` + `.php` ffuf sweep that no third endpoint exists.
- Kicked off `sqlmap -u .../action.php --data="id=1&qty=1&product_id=1&price=10" --batch --level=3 --risk=2` directly (letting sqlmap's own error-based/boolean-based detection do the work rather than reasoning about the PHP manually) — sqlmap started testing normally, then the **target connection was refused (evicted) about 9 seconds into the scan**, before any technique could complete.

**New finding this session — severe real-time contention:** the account's single target slot changed IP:port repeatedly *while this session was actively using it* (sometimes within under a minute, without this session spawning again), and at least twice the IP:port shown on the module page pointed at a completely different app (an "inlanefreight" nginx placeholder unrelated to this module — clearly another concurrent session's target on the same shared pool/account). This makes it very hard to hold a target stable long enough for a multi-second automated scan right now.

**Conclusion (unchanged from before, now reproduced 2 sessions running):** the `add.php`/`action.php` behavior looks like a genuinely broken/misconfigured challenge instance rather than something fixable by better recon — the technique (find endpoint → fuzz params → sqlmap) is sound and was applied exhaustively. Compounding it, this session hit heavy multi-agent contention on the account's one target slot, cutting scans off mid-run.

**Next attempt should:** retry during a quieter period (fewer concurrent sessions on this account), and if `action.php` is still input-independent on a fresh spawn, treat it as confirmed broken and check HTB's official Discord/forum for a known-issue report on this specific module's assessment target.
