



[![Docs](https://img.shields.io/badge/docs-latest-brightgreen.svg)](http://doc.servertribe.com)
[![Discord](https://img.shields.io/discord/844971127703994369)](http://discord.servertribe.com)
[![Docs](https://img.shields.io/badge/videos-watch-brightgreen.svg)](https://www.youtube.com/@servertribe)
[![Generic badge](https://img.shields.io/badge/download-latest-brightgreen.svg)](https://www.servertribe.com/community-edition/)

# Hyper-V Kickstarts






# Attune

[Attune](https://www.servertribe.com/)
automates and orchestrates processes to streamline deployments, scaling,
migrations, and management of your systems. The Attune platform is building a
community of sharable automated and orchestrated processes.

You can leverage the publicly available orchestrated blueprints to increase
your productivity, and accelerate the delivery of your projects. You can
open-source your own work and improve existing community orchestrated projects.

## Get Started with Attune, Download NOW!

The **Attune Community Edition** can be
[downloaded](https://www.servertribe.com/comunity-edition/)
for free from our
[ServerTribe website](https://www.servertribe.com/comunity-edition/).
You can learn more about Attune through
[ServerTribe's YouTube Channel](https://www.youtube.com/@servertribe).







# Clone this Project

To clone this project into your own instance of Attune, follow the
[Clone a GIT Project How To Instructions](https://servertribe-attune.readthedocs.io/en/latest/howto/design_workspace/clone_project.html).




## Blueprints

This Project contains the following Blueprints.



### Enable WSMan on Attune


### Hyper-V Blueprints


### Hyper-V Enable Push Files to Port 445


### Kickstart CentOS8.4+HyperV


### Kickstart RHEL8.7+HyperV+UEFI


### WinPE Kickstart Win10+HyperV


### WinPE Kickstart Win2019+HyperV





## Parameters


| Name | Type | Script Reference | Comment |
| ---- | ---- | ---------------- | ------- |
| Attune OS Build Server | Linux/Unix Node | `attuneosbuildserver` | This variable is used in the "Kickstart" build procedures, so the "Attune Server" can be used to build Attune servers. |
| DMS Subnet | Network IPv4 Subnet | `dmssubnet` | The subnet that the various DevOps servers are in. |
| Dropbox Access Token | Basic Credential | `dropboxaccesstoken` |  |
| Dropbox Path | Text | `dropboxpath` | Dropbox path to upload files. This will be relative to the root Dropbox app path.<br>Example: ~/Synerty Dropbox/Kean Ooi/Apps/Hyper-V Exports |
| HyperV Host | Windows Node | `hypervhost` |  |
| HyperV Host User | Windows Credential | `hypervhostuser` |  |
| Iso Folder | Text | `isofolder` |  |
| KS Linux: Disk First Letter | Text | `kslinuxdiskfirstletter` | The first letter of the disk in Linux, EG, sda or xda<br><br>s = sda for VMWare, Hyper-V and most servers<br>v = vda for oVirt/RHEV<br>x = xda for Citrix Xen |
| KS: VM CPU Count | Text | `ksvmcpucount` |  |
| KS: VM Ram Size GB | Text | `ksvmramsizegb` |  |
| KS VMWare: Attune Base Dir | Text | `ksvmwareattunebasedir` |  |
| KS: Windows Interface Alias | Text | `kswindowsinterfacealias` | oVirt Deployments = "Ethernet"<br>ESXi Deployments = "Ethernet0"<br><br>This is the "InternetAlias" of the interface shown when you run "get-netipaddress" from powershell on the machine. |
| Large Test File Name | Text | `largetestfilename` | File name of large test file to be created on Attune in /tmp and used for testing Copy-Item. |
| Linux: Attune User | Linux/Unix Credential | `linuxattuneuser` |  |
| Linux: Root User | Linux/Unix Credential | `linuxrootuser` |  |
| RPM Server | Linux/Unix Node | `rpmserver` |  |
| Samba Windows Directory | Text | `sambawindowsdirectory` | The extracted Windows Directory on the Samba server that we want to run setup.exe from. |
| Small Test File Name | Text | `smalltestfilename` | File name of small test file to be created on Attune in /tmp and used for testing Copy-Item. |
| Target Server | Basic Node | `targetserver` |  |
| Target Server: Lin | Linux/Unix Node | `targetserverlin` | The target server is a generic placeholder, usually used for the server a script will run on.<br>For example, the server being built if the procedure is building a server. |
| Target Server: Linux TimeZone | Text | `targetserverlinuxtimezone` |  |
| Target Server: Win | Windows Node | `targetserverwin` |  |
| Target Subnet | Network IPv4 Subnet | `targetsubnet` |  |
| test parameter | Text | `testparameter` |  |
| Virtual Hard Disk Folder | Text | `virtualharddiskfolder` |  |
| Windows: Administrator | Windows Credential | `windowsadministrator` | The windows administrator user |




## Files

| Name | Type | Comment |
| ---- | ---- | ------- |
| CentOS8 Boot ISO v8.4.2105 | Large Archives | This is from Kean's macbook attune on project "Build Peek V3 Cento08 Dev Node on Parallels" in file archive "CentOS8 Boot ISO v8.4.2105". |
| CentOS8 Kickstart Config | Version Controlled Files | https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/performing_an_advanced_rhel_installation/kickstart-commands-and-options-reference_installing-rhel-as-an-experienced-user |
| WinPE ISO for Windows 2019 Hyper-V | Large Archives | Taken from nzte1att2 file archive "WinPE 2019 ISO". |






# Contribute to this Project

**The collective power of a community of talented individuals working in
concert delivers not only more ideas, but quicker development and
troubleshooting when issues arise.**

If you’d like to contribute and help improve these projects, please fork our
repository, commit your changes in Attune, push you changes, and create a
pull request.

<img src="https://www.servertribe.com/wp-content/uploads/2023/02/Attune-pull-request-01.png" alt="pull request"/>

---

Please feel free to raise any issues or questions you have.

<img src="https://www.servertribe.com/wp-content/uploads/2023/02/Attune-get-help-02.png" alt="create an issue"/>


---

**Thank you**
