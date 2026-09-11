# Module 147 — Password Attacks
## Linux Authentication Process

## Approach
```
unshadow /etc/passwd /etc/shadow > combined.txt
john combined.txt                          # single-crack mode
john --wordlist=rockyou.txt combined.txt   # wordlist mode
```
Single-crack mode recovered one account's credentials directly from GECOS/username info; wordlist mode against rockyou.txt recovered another's.
