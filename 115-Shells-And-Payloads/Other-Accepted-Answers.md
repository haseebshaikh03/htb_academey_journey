# Module 115 — Shells & Payloads
## Other accepted answers (theory-level, from reading each section)

- **Anatomy of Shell:** answered from theory (interactive vs non-interactive, pty concepts)
- **Reverse Shells:** answered from theory
- **Infiltrating Windows:** answered from theory
- **Infiltrating Unix/Linux:** answered from theory
- **Laudanum:** answered from theory
- **Antak (webshell):** answered from theory
- **PHP Web Shells:** answered from theory
- **Live Engagement (question-843):** interpreter used by the target exploit-db PoC (50064.rb) — **Answer:** `PHP` (confirmed via the exploit-db page title)

## Environment fix worth keeping
`msfconsole` was hanging/crashing (3+ min) when launched via `docker exec htb bash -c "msfconsole ..."` — root cause: default cwd `/` made Ruby's bootsnap gem scan the whole filesystem and hit a recursive symlink loop under `/usr/lib/llvm-18/.../Debug+Asserts`.
**Fix:** always `cd /root` (or any non-`/` writable dir) before running `msfconsole` — cuts startup from 3+ min crash to ~15-20s.
