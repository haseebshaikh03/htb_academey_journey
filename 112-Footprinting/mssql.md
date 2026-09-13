MSSQL
Microsoft SQL (MSSQL) is Microsoft's SQL-based relational database management system. MSSQL is closed source and was initially written to run on Windows operating systems. 
It is popular among database administrators and developers when building applications that run on Microsoft's .NET framework due to its strong native support for .NET. 
There are versions of MSSQL that will run on Linux and MacOS, but we will more likely come across MSSQL instances on targets running Windows.

Port (TCP): 1433
SQL Server Management Studio (SSMS) comes as a feature that can be installed with the MSSQL package or can be downloaded separately.

Default Configuration
The service will likely run as NT SERVICE\MSSQLSERVER

Footprinting: MSSQL
Nmap Script Scan

sudo nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 $TARGET
MSSQL Ping in Metasploit

scanner/mssql/mssql_ping

Lab: MSSQL
Enumerate the target using the concepts taught in this section. List the hostname of MSSQL server.
Use Nmap to take an initial look at the service.


Connect to the MSSQL instance running on the target using the account (backdoor:Password1), then list the non-default database present on the server.
Use the mssql.py script to authenticate to the MSSQL instance. Then, enumerate the service.

└──╼ [★]$ mssqlclient.py backdoor@$TARGET -windows-auth
Answer: Employees


