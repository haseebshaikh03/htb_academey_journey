# Module 147 — Password Attacks
## Linux Authentication Process

```
unshadow /etc/passwd /etc/shadow > combined.txt
john combined.txt                          # single-crack mode
john --wordlist=rockyou.txt combined.txt   # wordlist mode
```

**Cracked:** `martin : Martin1` (single-crack mode)
**Cracked:** `sarah : mariposa` (rockyou wordlist mode)
