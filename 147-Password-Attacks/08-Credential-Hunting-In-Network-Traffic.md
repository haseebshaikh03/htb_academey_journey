# Module 147 — Password Attacks
## Credential Hunting in Network Traffic

Analyzed a provided `.pcap` with `tshark`/Wireshark:

- **FTP credentials in cleartext:** `leah : qwerty123`
- **File transferred over that FTP session:** `creds.txt` (downloaded/extracted from the pcap's FTP-DATA stream)
- **SNMP community string** (from SNMP packets): `s3cr3tSNMPC0mmun1ty`
- **Credit-card-looking number** found inside an HTTP POST body in the capture

Useful tshark filters: `ftp`, `ftp-data`, `snmp`, `http.request.method == POST`
