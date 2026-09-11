# Module 57 — Login Brute Forcing
## Section: Skills Assessment (2 parts)

### Part 1
`hydra` HTTP-GET basic-auth brute force against the target using existing wordlists.
**Credentials found:** `admin : Admin123`
Logging in as admin revealed the next-stage username: `satwossh`

### Part 2
`hydra` SSH brute force for user `satwossh`.
**Credentials found:** `satwossh : password1`

Pivoted in over SSH as satwossh, found a hint file naming "Thomas Smith" as the FTP user plus a target-specific `passwords.txt`.
Ran `username-anarchy "Thomas" "Smith"` against that password list, brute-forcing the local FTP service.
**FTP credentials found:** `thomas : chocolate!`
Retrieved `flag.txt` via FTP (python `ftplib`, over the SSH pivot).

**Flag:** `HTB{brut3f0rc1ng_succ3ssful}`
