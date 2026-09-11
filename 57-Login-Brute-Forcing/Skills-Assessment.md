# Module 57 — Login Brute Forcing
## Section: Skills Assessment (2 parts)

### Part 1 — Approach
`hydra` HTTP-GET basic-auth brute force against the target using existing wordlists.
Credentials recovered via hydra basic-auth brute force.
Logging in revealed the next-stage username for part 2.

### Part 2 — Approach
`hydra` SSH brute force for the username discovered in Part 1.
Credentials recovered via hydra SSH brute force.

Pivoted in over SSH, found a hint file naming an FTP user plus a target-specific password list.
Ran `username-anarchy "<First>" "<Last>"` against that password list, brute-forcing the local FTP service.
FTP credentials recovered via username-anarchy + brute force against the target-specific wordlist.
Retrieved `flag.txt` via FTP (python `ftplib`, over the SSH pivot).

**Flag** found by chaining the three brute-force stages above (basic-auth → SSH → FTP).
