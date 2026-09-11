# Module 147 — Password Attacks
## Introduction to Hashcat

**Dictionary attack:** `hashcat -m <mode> hash.txt rockyou.txt` → `crazy!`

**Dictionary + rules attack:** `hashcat -m <mode> hash.txt rockyou.txt -r rules/best64.rule` → `c0wb0ys1`

**Mask attack:** `hashcat -m <mode> hash.txt -a 3 ?u?l?l?l?l?d?s` (1 upper, 4 lower, 1 digit, 1 special) → `Mouse5!`
