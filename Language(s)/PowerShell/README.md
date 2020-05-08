    Copyright(c) 2019-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# [PowerShell](file:///B:/CRTejaswi/Documents/CONFIG.html#powershell-ps)
> Personal notes.

# Index

- [ ] [General](#general)
- [ ] [PowerShell/Python Interoperability](#powershell-python)
- [ ] [PowerShell Linux Compatibility](#powershell-linux)
- [ ] [Common Windows TODO](#windows-todo)

# General

- Update (from PS)
```
iex "& { $(irm https://aka.ms/install-powershell.ps1) } -UseMSI"
```

- Uninstall built-in apps
```
Get-AppxPackage *3dbuilder* | Remove-AppxPackage
Get-AppxPackage *getstarted* | Remove-AppxPackage
Get-AppxPackage *windowsalarms* | Remove-AppxPackage
Get-AppxPackage *windowscalculator* | Remove-AppxPackage
Get-AppxPackage *windowscommunicationapps* | Remove-AppxPackage
Get-AppxPackage *windowsmaps* | Remove-AppxPackage
Get-AppxPackage *windowsphone* | Remove-AppxPackage
Get-AppxPackage *windowsstore* | Remove-AppxPackage
Get-AppxPackage *zunemusic* | Remove-AppxPackage
Get-AppxPackage *zunevideo* | Remove-AppxPackage
Get-AppxPackage *bingfinance* | Remove-AppxPackage
Get-AppxPackage *bingnews* | Remove-AppxPackage
Get-AppxPackage *bingweather* | Remove-AppxPackage
Get-AppxPackage *bingsports* | Remove-AppxPackage
Get-AppxPackage *photos* | Remove-AppxPackage
Get-AppxPackage *soundrecorder* | Remove-AppxPackage
Get-AppxPackage *xboxapp* | Remove-AppxPackage
```

- Create New File/Folder
```
ni -path 'C:\Users\Chaitanya Tejaswi\Desktop' -ItemType 'directory' -name 'myTEST'
ni -path 'C:\Users\Chaitanya Tejaswi\Desktop\myTEST' -ItemType 'file' -name 'myTEST.md'
```

- Get storage directory of binary file.
```
gps firefox | ls
```

### System Help
- Update help.
```
update-help -Force
```
- Get help.
```
man *service*
man get-service
man get-service -detailed
man get-service -showwindow
man get-service -examples
man get-service -full
man get-service -online
man *eventlog*
man about_*
```
- Nouns & Verbs <br>
PS names cmdlets/functions in a `Verb-Noun` manner, to make their names predictable. (eg. `Get-Service`) <br>
To lookup all PERMITTED verbs (98), use:
```
get-verb
get-verb | measure
```

### Pipelining

- Import/Export
```
man export*
man import*
```
```
Export-Clixml                     Cmdlet
Export-Csv                        Cmdlet
Export-FormatData                 Cmdlet
Export-PSSession                  Cmdlet
Export-BinaryMiLog                Cmdlet
Export-WindowsDriver              Cmdlet
Export-WindowsCapabilitySource    Cmdlet
Export-WindowsImage               Cmdlet
Export-Counter                    Cmdlet
Export-ODataEndpointProxy         Function
Export-Certificate                Cmdlet
Export-PfxCertificate             Cmdlet
Export-ProvisioningPackage        Cmdlet
Export-Trace                      Cmdlet
Export-ScheduledTask              Function
Export-StartLayoutEdgeAssets      Cmdlet
Export-StartLayout                Cmdlet
Export-TlsSessionTicketKey        Cmdlet

ImportSystemModules               Function
Import-PowerShellDataFile         Function
Import-Module                     Cmdlet
Import-Alias                      Cmdlet
Import-Clixml                     Cmdlet
Import-Csv                        Cmdlet
Import-LocalizedData              Cmdlet
Import-PSSession                  Cmdlet
Import-PackageProvider            Cmdlet
Import-BinaryMiLog                Cmdlet
Import-IseSnippet                 Function
Import-Counter                    Cmdlet
Import-PfxCertificate             Cmdlet
Import-Certificate                Cmdlet
Import-StartLayout                Cmdlet
Import-TpmOwnerAuth               Cmdlet
```

- Import/Export CSV, XML
```
gps | export-csv process.csv
gps | export-clixml process.xml
```

- Convert to HTML
  - [ ] Select/Sort & save necessary columns to `test.html`
  - [ ] Using CSS, beautiful `test.html`
```
gps | convertto-html | out-file test.html
ls  | convertto-html | out-file -append test.html
```

### Objects

<center><b>TODO</b></center>

- [ ] Study `ls` cmdlet.

Unlike UNIX, PS outputs objects (instead of text). This makes it easy to sort them.
This instruction gets all the members (properties/methods) of `get-process` cmdlet, sorted by name.
```
get-process | get-member | sort Name
```
```
   TypeName: System.Diagnostics.Process

Name                       MemberType     Definition
----                       ----------     ----------
__NounName                 NoteProperty   string __NounName=Process
BasePriority               Property       int BasePriority {get;}
BeginErrorReadLine         Method         void BeginErrorReadLine()
BeginOutputReadLine        Method         void BeginOutputReadLine()
CancelErrorRead            Method         void CancelErrorRead()
CancelOutputRead           Method         void CancelOutputRead()
Close                      Method         void Close()
CloseMainWindow            Method         bool CloseMainWindow()
Company                    ScriptProperty System.Object Company {get=$this.Mainmodule.FileVersionInfo.CompanyName;}
Container                  Property       System.ComponentModel.IContainer Container {get;}
CPU                        ScriptProperty System.Object CPU {get=$this.TotalProcessorTime.TotalSeconds;}
CreateObjRef               Method         System.Runtime.Remoting.ObjRef CreateObjRef(type requestedType)
Description                ScriptProperty System.Object Description {get=$this.Mainmodule.FileVersionInfo.FileDescription;}
Dispose                    Method         void Dispose(), void IDisposable.Dispose()
Disposed                   Event          System.EventHandler Disposed(System.Object, System.EventArgs)
EnableRaisingEvents        Property       bool EnableRaisingEvents {get;set;}
Equals                     Method         bool Equals(System.Object obj)
ErrorDataReceived          Event          System.Diagnostics.DataReceivedEventHandler ErrorDataReceived(System.Object, System.Diagnostics.DataReceivedEventArgs)
ExitCode                   Property       int ExitCode {get;}
Exited                     Event          System.EventHandler Exited(System.Object, System.EventArgs)
ExitTime                   Property       datetime ExitTime {get;}
FileVersion                ScriptProperty System.Object FileVersion {get=$this.Mainmodule.FileVersionInfo.FileVersion;}
GetHashCode                Method         int GetHashCode()
GetLifetimeService         Method         System.Object GetLifetimeService()
GetType                    Method         type GetType()
Handle                     Property       System.IntPtr Handle {get;}
HandleCount                Property       int HandleCount {get;}
Handles                    AliasProperty  Handles = Handlecount
HasExited                  Property       bool HasExited {get;}
Id                         Property       int Id {get;}
InitializeLifetimeService  Method         System.Object InitializeLifetimeService()
Kill                       Method         void Kill()
MachineName                Property       string MachineName {get;}
MainModule                 Property       System.Diagnostics.ProcessModule MainModule {get;}
MainWindowHandle           Property       System.IntPtr MainWindowHandle {get;}
MainWindowTitle            Property       string MainWindowTitle {get;}
MaxWorkingSet              Property       System.IntPtr MaxWorkingSet {get;set;}
MinWorkingSet              Property       System.IntPtr MinWorkingSet {get;set;}
Modules                    Property       System.Diagnostics.ProcessModuleCollection Modules {get;}
Name                       AliasProperty  Name = ProcessName
NonpagedSystemMemorySize   Property       int NonpagedSystemMemorySize {get;}
NonpagedSystemMemorySize64 Property       long NonpagedSystemMemorySize64 {get;}
NPM                        AliasProperty  NPM = NonpagedSystemMemorySize64
OutputDataReceived         Event          System.Diagnostics.DataReceivedEventHandler OutputDataReceived(System.Object, System.Diagnostics.DataReceivedEventArgs)
PagedMemorySize            Property       int PagedMemorySize {get;}
PagedMemorySize64          Property       long PagedMemorySize64 {get;}
PagedSystemMemorySize      Property       int PagedSystemMemorySize {get;}
PagedSystemMemorySize64    Property       long PagedSystemMemorySize64 {get;}
Path                       ScriptProperty System.Object Path {get=$this.Mainmodule.FileName;}
PeakPagedMemorySize        Property       int PeakPagedMemorySize {get;}
PeakPagedMemorySize64      Property       long PeakPagedMemorySize64 {get;}
PeakVirtualMemorySize      Property       int PeakVirtualMemorySize {get;}
PeakVirtualMemorySize64    Property       long PeakVirtualMemorySize64 {get;}
PeakWorkingSet             Property       int PeakWorkingSet {get;}
PeakWorkingSet64           Property       long PeakWorkingSet64 {get;}
PM                         AliasProperty  PM = PagedMemorySize64
PriorityBoostEnabled       Property       bool PriorityBoostEnabled {get;set;}
PriorityClass              Property       System.Diagnostics.ProcessPriorityClass PriorityClass {get;set;}
PrivateMemorySize          Property       int PrivateMemorySize {get;}
PrivateMemorySize64        Property       long PrivateMemorySize64 {get;}
PrivilegedProcessorTime    Property       timespan PrivilegedProcessorTime {get;}
ProcessName                Property       string ProcessName {get;}
ProcessorAffinity          Property       System.IntPtr ProcessorAffinity {get;set;}
Product                    ScriptProperty System.Object Product {get=$this.Mainmodule.FileVersionInfo.ProductName;}
ProductVersion             ScriptProperty System.Object ProductVersion {get=$this.Mainmodule.FileVersionInfo.ProductVersion;}
PSConfiguration            PropertySet    PSConfiguration {Name, Id, PriorityClass, FileVersion}
PSResources                PropertySet    PSResources {Name, Id, Handlecount, WorkingSet, NonPagedMemorySize, PagedMemorySize, PrivateMemorySize, VirtualMemorySize, Threads.Count, TotalProcessorTime}
Refresh                    Method         void Refresh()
Responding                 Property       bool Responding {get;}
SafeHandle                 Property       Microsoft.Win32.SafeHandles.SafeProcessHandle SafeHandle {get;}
SessionId                  Property       int SessionId {get;}
SI                         AliasProperty  SI = SessionId
Site                       Property       System.ComponentModel.ISite Site {get;set;}
StandardError              Property       System.IO.StreamReader StandardError {get;}
StandardInput              Property       System.IO.StreamWriter StandardInput {get;}
StandardOutput             Property       System.IO.StreamReader StandardOutput {get;}
Start                      Method         bool Start()
StartInfo                  Property       System.Diagnostics.ProcessStartInfo StartInfo {get;set;}
StartTime                  Property       datetime StartTime {get;}
SynchronizingObject        Property       System.ComponentModel.ISynchronizeInvoke SynchronizingObject {get;set;}
Threads                    Property       System.Diagnostics.ProcessThreadCollection Threads {get;}
ToString                   Method         string ToString()
TotalProcessorTime         Property       timespan TotalProcessorTime {get;}
UserProcessorTime          Property       timespan UserProcessorTime {get;}
VirtualMemorySize          Property       int VirtualMemorySize {get;}
VirtualMemorySize64        Property       long VirtualMemorySize64 {get;}
VM                         AliasProperty  VM = VirtualMemorySize64
WaitForExit                Method         bool WaitForExit(int milliseconds), void WaitForExit()
WaitForInputIdle           Method         bool WaitForInputIdle(int milliseconds), bool WaitForInputIdle()
WorkingSet                 Property       int WorkingSet {get;}
WorkingSet64               Property       long WorkingSet64 {get;}
WS                         AliasProperty  WS = WorkingSet64
```

Using `where`

The code below lists all processes with ID >= 1000, sorted in ascending order.
```
get-process | where {$_.Handles -ge 1000} | sort -Property Handles
```
```
Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
   1011      42    39560      23564              4664   0 LenovoVantageService
   1060      22    11932      24380              1044   0 svchost
   1073       6     8740      12100             14168   0 Windows.WARP.JITService
   1136      52    50488      41276              4136   0 Lenovo.Modern.ImController
   1201      17     7516      11760              1208   0 svchost
   1209      91   102380     165036      18.14   8500   1 SearchUI
   1376      22     7248      13288               976   0 lsass
   1453      93   179728     231288      42.13   3016   1 firefox
   2075      81   384764     151604              4332   0 MsMpEng
   3523       9     1868       3972              8632   1 rundll32
   3538     137   119552     132228     153.25   7980   1 explorer
   5508       0      188        136                 4   0 System
```





# PowerShell & Python
# PowerShell & Linux
# Windows Todo

- Rename User.
```
Win+R >> netplwiz >> Change User details.
    OR
Win+X, A >>
    net localgroup Users "account-name" /add
    net localgroup Users "account-name" /delete
    net localgroup Administrators "account-name" /add
    net localgroup Administrators "account-name" /delete
```

- Disable Automatic Updates
```
1. Disable Windows Update Service.
Win+R >> services.msc >> Windows Update (wuauserv) >> Disable, Stop, Fail Count=365 days.
2. Meter your internet connection.
3. Add Registry Key for Windows Update.
Win+R >> regedit >> HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows >> New Key (WindowsUpdate) >> New Key (AU) >> New -> DWORD (32-bit) (AUOptions) >> Set Value=2.
Value=2 indicates "Notify for download/install".
Restart.
```

- Disable Quick Access & Recent Items && Disable File Explorer History.
```
Right-Click Quick Access >> Options >> Open File Explorer to: "This PC" >> Uncheck Privacy Options.
```
- Disable OneDrive.
