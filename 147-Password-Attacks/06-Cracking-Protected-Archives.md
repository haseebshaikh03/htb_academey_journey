# Module 147 — Password Attacks
## Cracking Protected Archives (BitLocker VHD)

```
hashcat -m 22100 bitlocker_hash.txt rockyou.txt
```
**Cracked password:** `francisco`

**Reading the flag afterward:** no `/dev/fuse` available in the container, so a real BitLocker mount wasn't possible. Instead decrypted and read the volume directly in Python using `libbde` (BitLocker) + `libfsntfs` (NTFS-inside-BitLocker) bindings to pull `flag.txt` without mounting.
