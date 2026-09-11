# Module 147 — Password Attacks
## Cracking Protected Files

Password-protected `.xlsx` file.

```
office2john protected.xlsx > hash.txt
john --wordlist=rockyou.txt hash.txt
```

**Cracked password:** `beethoven`
