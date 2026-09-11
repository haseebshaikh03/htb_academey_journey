# Module 143 — Active Directory Enumeration & Attacks
## Theory/recon sections completed

**External Recon and Enumeration Principles:**
`dig TXT inlanefreight.com` → flag: `HTB{5Fz6UPNUFFzqjdg0AzXyxCjMZ}`

**Enumerating & Retrieving Password Policies:**
- Default domain minimum password length: `7`
- INLANEFREIGHT.LOCAL's actual minPwdLength: `8`

**ACL Abuse Primer:**
- Access-control list type: `DACL`
- Permission that lets you fully control an object: `GenericAll`

**Bleeding Edge Vulnerabilities:**
NoPac CVE pair: `2021-42278&2021-42287`

**Domain Trusts Primer:**
- Child domain: `LOGISTICS.INLANEFREIGHT.LOCAL`
- Forest-trust domain: `FREIGHTLOGISTICS.LOCAL`
- Trust direction: `Bidirectional`

**Additional AD Auditing Techniques:**
Answer: `COMPLETE`
