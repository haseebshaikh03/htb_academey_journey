# Module 143 — Active Directory Enumeration & Attacks
## Theory/recon sections completed

**External Recon and Enumeration Principles:**
Approach: query the domain's TXT records with `dig TXT <domain>` — the section's flag is published directly in a TXT record.

**Enumerating & Retrieving Password Policies:**
- Approach: pull the *default domain* minimum password length from Microsoft's documented AD default policy values (not from the lab itself).
- Approach: enumerate the lab domain's actual effective password policy (e.g. via `net rpc`, `rpcclient`, `crackmapexec`/`netexec`, or PowerView's `Get-DomainPolicy`) and read the `minPwdLength` attribute it reports.

**ACL Abuse Primer:**
- Approach: recall/look up which of the two AD access-control-list types (DACL vs SACL) is the one that determines who is granted or denied access to an object.
- Approach: recall/look up which specific AD permission (from the standard extended-rights/generic-rights list) grants full control over an object — check the module's ACL rights table.

**Bleeding Edge Vulnerabilities:**
Approach: identify the pair of CVEs referenced by the NoPac vulnerability (covering the sAMAccountName spoofing + Kerberos ticket forging chain) — look these up via the module's own text or public CVE databases (search "NoPac CVE").

**Domain Trusts Primer:**
- Approach: from the lab's domain structure (as shown in the section's diagram/theory or via `Get-ADTrust`/`nltest /domain_trusts`), identify the child domain name, the external forest-trust partner's domain name, and the direction of that trust (one-way vs two-way).

**Additional AD Auditing Techniques:**
Answered directly from the section's theory text/quiz.
