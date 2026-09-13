# Module 109 — Command Injections
## Skills Assessment — BLOCKED

Target: Tiny File Manager (guest/guest login, readonly). Spawns as e.g. `154.57.164.73:32762`.

### New findings this session
- **Ruled out `admin`/`admin@123`** (Tiny File Manager's well-known hardcoded default admin credentials) — login explicitly returns "Invalid" on this instance, so the deployed config has changed the default admin password/removed the account.
- **`guest`/`guest` login confirmed working** (session cookie set, `logout` link present, full file listing rendered).
- As `guest`, the file manager root lists ~9 randomly-named `.txt` files plus a `tmp/` folder. Eight of the `.txt` files are decoys ("this is just a random document"); **one contains the hint: "Stop looking at these random documents! Don't you have some injection to do :)"** — confirms the intended vuln is a real OS command injection somewhere reachable by the readonly `guest` account, not a privesc-to-admin puzzle.
- Confirmed (via the rendered page's own inline JS) that the client never sends a `token` field on **any** ajax action (`search`, `backup`, `save_settings`, `new_password_hash`, `upload_from_url` all POST via `$.ajax` with no token in the payload) — yet the server silently 302-redirects (falls through to default page render) on every ajax POST attempted as `guest`, **including `type=search`, which should be readable by anyone**. This means the ajax dispatch gate is being blocked by something else, most likely a `FM_READONLY` check gating the entire ajax branch for `guest`, not (only) the CSRF-token gate found in the public GitHub source.
- Tried a bogus `token=bogus` value on the search request too — same silent-redirect behavior, no "Invalid Token" message ever appears, reinforcing that this deployed build's gate is different from what's on GitHub master (or the readonly check simply happens first).

### Not yet tried (next steps)
- The `tmp/` folder was seen in the listing but not explored — browse into it as guest, it may contain further hints or an uploadable/writable path despite readonly mode.
- Guest-accessible **GET-based** file operations that might shell out (as opposed to the POST/ajax-gated ones already ruled out): view/quickView of specific file types (image thumbnailing via ImageMagick/exiftool, zip/archive listing via `unzip -l`) — these are classic TFM command-injection surfaces and are GET requests, so they would NOT be blocked by the ajax/readonly gate seen above. Worth testing `?to=&view=<crafted-name>` and any archive-preview feature specifically.
- Never got far enough to test path traversal (`?to=../../..`) for arbitrary file read, which might turn up the actual app source or a config file with real admin creds.
- This session's target instability (see 147's BLOCKED file for account-wide contention evidence) meant a freshly-spawned instance sat at a generic "Welcome to HTB Academy" placeholder page for 2+ minutes before terminate/reset stopped working reliably — if that happens again, terminate and respawn rather than waiting it out.

**Recommendation:** next session, focus on GET-based file-type-triggered shell-outs (image/archive preview) rather than the ajax POST endpoints, since those are now fairly conclusively gated off for `guest`. Also fully explore `tmp/`.
