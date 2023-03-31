



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

Clone this project into your own instance of Attune.

<img src="https://www.servertribe.com/wp-content/uploads/2023/02/Attune-clone-new-project-01.png" alt="clone a new project"/>

---

Paste the GIT repository URL into Attune and Select Clone.

<img src="https://www.servertribe.com/wp-content/uploads/2023/02/Attune-clone-new-project-02.png" alt="clone a new project"/>

---

**Now that this project is in your Attune instance you can begin creating
Jobs.**

Navigate to the Plan workspace and create a Job from a Blueprint in the
Project you cloned.

<img src="https://www.servertribe.com/wp-content/uploads/2023/02/Attune-plan-new-job-11.png" alt="plan a new job"/>

---

Configure the Parameters for the Job you created. Create the Values you're
missing in the next step.

<img src="https://www.servertribe.com/wp-content/uploads/2023/02/Attune-plan-new-job-12.png" alt="plan a new job"/>

---

Create the Values required to fill the Parameters for the Job.

<img src="https://www.servertribe.com/wp-content/uploads/2023/02/Attune-plan-new-job-13-1.png" alt="plan a new job"/>

---

Run your Job.

<img src="https://www.servertribe.com/wp-content/uploads/2023/02/Attune-run-job-01.png" alt="run your job"/>

---

**Congratulations, you’ve run a cloned project.**

If you need further assistance, please explore our help.

<img width=200 src="https://www.servertribe.com/wp-content/uploads/2023/02/Attune-get-help-01.png" alt="get help"/>




## Blueprints

This Project contains the following Blueprints.



### Backup Export to Dropbox


### Enable WSMan on Attune


### Export Virtual Machine


### Hyper-V Blueprints


### Hyper-V Enable Push Files to Port 445


### Kickstart CentOS8.4+HyperV


### Kickstart RHEL8.7+HyperV+UEFI


### WinPE Kickstart Win10+HyperV


### WinPE Kickstart Win2019+HyperV


### WIN Reboot





## Parameters


| Name | Type | Script Reference | Comment |
| ---- | ---- | ---------------- | ------- |
| Attune OS Build Server | Linux/Unix Node | `attuneosbuildserver` | This variable is used in the "Kickstart" build procedures, so the "Attune Server" can be used to build Attune servers. |
| DMS Subnet | Network IPv4 Subnet | `dmssubnet` | The subnet that the various DevOps servers are in. |
| Dropbox Access Token | Basic Credential | `dropboxaccesstoken` | None |
| HyperV Export Directory | Text | `hypervexportdirectory` | None |
| HyperV Host | Windows Node | `hypervhost` | None |
| HyperV Host User | Windows Credential | `hypervhostuser` | None |
| Iso Folder | Text | `isofolder` | None |
| Kickstart Organisation Name | Text | `kickstartorganisationname` | None |
| KS Linux: Disk First Letter | Text | `kslinuxdiskfirstletter` | The first letter of the disk in Linux, EG, sda or xda

s = sda for VMWare, Hyper-V and most servers
v = vda for oVirt/RHEV
x = xda for Citrix Xen |
| KS: VM CPU Count | Text | `ksvmcpucount` | None |
| KS: VM Ram Size GB | Text | `ksvmramsizegb` | None |
| KS VMWare: Attune Base Dir | Text | `ksvmwareattunebasedir` | None |
| KS: Windows Interface Alias | Text | `kswindowsinterfacealias` | oVirt Deployments = "Ethernet"
ESXi Deployments = "Ethernet0"

This is the "InternetAlias" of the interface shown when you run "get-netipaddress" from powershell on the machine. |
| Large Test File Name | Text | `largetestfilename` | File name of large test file to be created on Attune in /tmp and used for testing Copy-Item. |
| Linux: Attune User | Linux/Unix Credential | `linuxattuneuser` | None |
| Linux: Root User | Linux/Unix Credential | `linuxrootuser` | None |
| oVirt: TimeZone | Text | `ovirttimezone` | None |
| RHEL: 8 baseos Repo URL | Text | `rhel8baseosrepourl` | None |
| RPM Server | Linux/Unix Node | `rpmserver` | None |
| Samba Windows Directory | Text | `sambawindowsdirectory` | The extracted Windows Directory on the Samba server that we want to run setup.exe from. |
| Small Test File Name | Text | `smalltestfilename` | File name of small test file to be created on Attune in /tmp and used for testing Copy-Item. |
| Target Server | Basic Node | `targetserver` | None |
| Target Server: Lin | Linux/Unix Node | `targetserverlin` | The target server is a generic placeholder, usually used for the server a script will run on.
For example, the server being built if the procedure is building a server. |
| Target Server: Linux TimeZone | Text | `targetserverlinuxtimezone` | None |
| Target Server: Win | Windows Node | `targetserverwin` | None |
| Target Subnet | Network IPv4 Subnet | `targetsubnet` | None |
| test parameter | Text | `testparameter` | None |
| Virtual Hard Disk Folder | Text | `virtualharddiskfolder` | None |
| Windows: Administrator | Windows Credential | `windowsadministrator` | The windows administrator user |
| WinPE Samba Server | Linux/Unix Node | `winpesambaserver` | None |
| Dropbox App Key | Basic Credential | `dropboxappkey` | None |
| Dropbox Refresh Token | Basic Credential | `dropboxrefreshtoken` | None |
| Dropbox App Secret | Basic Credential | `dropboxappsecret` | None |




## Files


| Name | Type | Comment |
| ---- | ---- | ------- |
| CentOS8 Boot ISO v8.4.2105 | Large Archives | This is from Kean's macbook attune on project "Build Peek V3 Cento08 Dev Node on Parallels" in file archive "CentOS8 Boot ISO v8.4.2105". |
| CentOS8 Kickstart Config | Version Controlled Files | https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/performing_an_advanced_rhel_installation/kickstart-commands-and-options-reference_installing-rhel-as-an-experienced-user |
| Python Dropbox Uploader | Version Controlled Files | None |
| RHEL8.7 Boot ISO | Large Archives | None |
| RHEL8.7 grub.cfg Inside efiboot.img | Version Controlled Files | None |
| RHEL8.7 Kickstart Config UEFI | Version Controlled Files | None |
| WinPE ISO for Windows 10 Hyper-V | Large Archives | This is currently the same as "WinPE ISO for Windows 10 oVirt". |
| WinPE ISO for Windows 2019 Hyper-V | Large Archives | Taken from nzte1att2 file archive "WinPE 2019 ISO". |
| WinPE startnet.cmd | Version Controlled Files | None |
| WIN Win10 Unattended Config HyperV 7 - Working | Version Controlled Files | Copied from "WIN Win10 Unattended Config HyperV".

Changed LogonCount from 1 to 88. |
| WIN Win2019 Unattended Config HyperV | Version Controlled Files | This is the same as file archive "WIN Win2019 Unattended Config with Drivers". |






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
