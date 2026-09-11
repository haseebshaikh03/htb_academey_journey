# Module 147 — Password Attacks
## Introduction to Hashcat

## Approach
**Dictionary attack:** `hashcat -m <mode> hash.txt rockyou.txt`

**Dictionary + rules attack:** `hashcat -m <mode> hash.txt rockyou.txt -r rules/best64.rule`

**Mask attack:** `hashcat -m <mode> hash.txt -a 3 ?u?l?l?l?l?d?s` (1 upper, 4 lower, 1 digit, 1 special)
