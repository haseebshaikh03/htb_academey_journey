SNMP Section:
Simple Network Management Protocol (SNMP) was created to monitor network devices. In addition, this protocol can also be used to handle configuration tasks and change settings remotely.
SNMP-enabled hardware includes routers, switches, servers, IoT devices, and many other devices that can also be queried and controlled using this standard protocol. 
Thus, it is a protocol for monitoring and managing network devices.
Ports:
Transmits control commands (UDP): 161
SNMP traps (UDP): 162

Footprinting: SNMP
Tools:

snmpwalk, onesixtyone, braa
snmpwalk - query OIDs and their information
Onesixtyone - brute-force the names of the community strings since they can be named arbitrarily
SNMPwalk

Enumeration: snmpwalk -v2c -c public $TARGET
OneSixtyOne

Brute-force community strings: onesixtyone -c /opt/useful/seclists/Discovery/SNMP/snmp.txt $TARGET
Braa

Brute-force individual OIDs and enumerate their information: braa community_string@$TARGET:.1.3.6.*

Questions:

Enumerate the SNMP service and obtain the email address of the admin. Submit it as the answer.
snmpwalk -v2c -c public $TARGET > snmpwalk_output
Answer: devadmin@inlanefreight.htb

What is the customized version of the SNMP server?
The version information is found in the output of the previous command.
Answer: InFreight SNMP v0.91


Enumerate the custom script that is running on the system and submit its output as the answer.
└──╼ [★]$ cat snmpwalk_output | grep "HTB"
