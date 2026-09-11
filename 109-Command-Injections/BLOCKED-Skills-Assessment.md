# Module 109 — Command Injections
## Skills Assessment — BLOCKED

Target: Tiny File Manager 2.4.6, login `guest/guest`, e.g. `154.57.164.67:30700`.

Checked actual source (GitHub raw, master branch) — the app's ajax dispatch gate is:
```php
if ((...logged... || !FM_USE_AUTH) && isset($_POST['ajax'], $_POST['token'])) {
    if (!verifyToken($_POST['token'])) { die("Invalid Token."); }
    // type=search / settings / pwdhash / save / backup / upload handlers live here
}
```
This requires a `token` param to even be present — without it, the whole ajax block is skipped and the request falls through to a normal full-page render (matches everything observed: a ~60KB HTML page, never JSON).

No token value was ever found anywhere in the guest session (HTML, cookies, JS, meta tags) — most likely because the CSRF-token form is only rendered for non-readonly users, and `guest` is forced `FM_READONLY`.

**Ruled out (all tested, no differential behavior):** upload, rename (GET & POST), folder/file create, edit/save, chmod, search, settings, timing-injection on login/view/download/header fields, hidden endpoint/parameter brute-force, path traversal.

**Not yet tried:** the `pwdhash` ajax type specifically (likely blocked by the same token wall, but unverified) — and there may be a legitimate non-guest credential/registration path that wasn't discovered.

**Recommendation:** try a fresh target respawn (possible stale/misconfigured instance), or check HTB's module hints/discussion thread for section "Skills Assessment" (question ID was `question-700`) directly.
