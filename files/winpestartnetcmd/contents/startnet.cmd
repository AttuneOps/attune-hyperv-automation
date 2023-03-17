wpeinit -unattend:"X:\Unattend-PE.xml"

netsh.exe interface ipv4 set address ^
    name="${ksWindowsInterfaceAlias}" ^
    static ${targetServer.ip} ^
    ${targetSubnet.netmask} ^
    ${targetSubnet.gateway}
    
netsh.exe interface ipv4 add dnsservers ^
    name="${ksWindowsInterfaceAlias}" ^
    address=${targetSubnet.dns1} ^
    index=1

ipconfig /all

@echo off
set sambaIPaddress=${winpeSambaServer.ip}

:pingtheserver
ping %sambaIPaddress% | find "TTL" > nul
if errorlevel 1 (
    echo waiting for pingable Samba IP address ${winpeSambaServer.ip}...
    ping localhost -n 2 >NUL
    goto :pingtheserver
) else (
    echo ping successful for Samba server
)

:mountsamba
net use Z: \\%sambaIPaddress%\share | find "successfully" > nul
if errorlevel 1 (
    echo mount failed, waiting...
    ping localhost -n 2 >NUL
    goto :mountsamba
) else (
    echo Samba mount successful.
)
@echo on

Z:

cd .\${sambaWindowsDirectory}\

setup