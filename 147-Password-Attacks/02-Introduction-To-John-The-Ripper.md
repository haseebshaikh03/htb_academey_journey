# Module 147 — Password Attacks
## Introduction to John The Ripper

**Note:** Debian's stock `john` package lacks several formats (e.g. RIPEMD-128, sha512crypt). Had to build **John the Ripper jumbo** from source to get full format support.

## Approach
- **Single-crack mode** (uses GECOS/username info as candidates) against the target hash.
- **Wordlist mode** against a RIPEMD-128 hash, using rockyou.txt.
