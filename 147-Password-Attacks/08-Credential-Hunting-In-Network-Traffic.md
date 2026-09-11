# Module 147 — Password Attacks
## Credential Hunting in Network Traffic

Analyzed a provided `.pcap` with `tshark`/Wireshark:

## Approach
- **FTP credentials in cleartext:** recovered by filtering for the FTP control-channel stream and reading the login exchange.
- **File transferred over that FTP session:** located and extracted from the pcap's FTP-DATA stream.
- **SNMP community string:** recovered by filtering for SNMP packets and inspecting the community field.
- **Credit-card-looking number:** found inside an HTTP POST body in the capture.

Useful tshark filters: `ftp`, `ftp-data`, `snmp`, `http.request.method == POST`
