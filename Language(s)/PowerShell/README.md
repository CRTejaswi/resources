    Copyright(c) 2019-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# PowerShell
> Personal notes.

# Index

- [General](#general)
- [System Help](#system-help)
- [Exception Handling](#exception-handling)
- [Objects](#objects)
- [Pipelining](#pipelining)
- [Formatting](#formatting)
- [Filtering & Comparisons](#filtering-comparisons)
- [Remote Access](#remote-access)
- [Background Processes (`Job`s)](#background-processes-aka-job)
- [Variables](#variables)
- [Regular Expressions](#regular-expressions)
- [Scripting](#scripting)
- [Formatted Data (CSV, XML, JSON)](#formatted-data-csv-xml-json)
- [Databases](#databases-sqlite)
- [Recipies](#recipies)
- [ ] [PowerShell/Python Interoperability](#powershell-python)
- [Common Windows TODO](#windows-todo)

## General

- Update (from PS)
    ```
    iex "& { $(irm https://aka.ms/install-powershell.ps1) } -UseMSI"
    ```

- Clear Command History <br> Press `Ctrl + F7`

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
    ni -path 'C:\Users\CRTejaswi\Desktop' -ItemType 'directory' -name 'myTEST'
    ni -path 'C:\Users\CRTejaswi\Desktop\myTEST' -ItemType 'file' -name 'myTEST.md'
    ```

- Get storage directory of binary file.
    ```
    gps firefox | ls
    ```

- Common Aliases
    ```
    man -> Get-Help    (to lookup command syntax)
    gcm -> Get-Command (to lookup command syntax)
    gm  -> Get-Member  (to learn more about an object)
    gal -> Get-Alias

    gcb -> Get-Clipboard (Copy from clipboard)
    scb -> Set-Clipboard (Copy to clipboard)
    gps -> Get-Process

    ft  -> Format-Table
    fl  -> Format-List

    gsv -> Get-Service
    gin -> Get-ComputerInfo
    gtz -> Get-TimeZone

    gwmi -> Get-WmiObject
    gjb  -> Get-Job

    cls -> Clear-Host ('clear shell')
    clc -> Clear-Content
    clv -> Clear-Variable
    cli -> Clear-Item
    clp -> Clear-ItemProperty

    pushd, popd -> Push-Location, Pop-Location
    copy, move  -> Copy-Item, Move-Item
    history     -> Get-History
    ```

- Create new aliases <br>
    Create `aliases.csv`
    ```
    Name,Value
    gotodir,Get-ChildItem
    sel,Select-Object
    clip,Get-Clipboard
    ```
    Import these aliases using:
    ```
    import-csv aliases.csv | new-alias
    ```

<center><b>TODO</b></center>

- [ ] Come up with useful aliases

## System Help

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

## Objects

Unlike UNIX, PS outputs objects (instead of text). This makes it easy to sort them.
This instruction gets all the members (properties/methods) of `get-process` cmdlet, sorted by name.
    ```
    get-process | get-member | sort Name
    gps | gm | sort Name
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

- Objects: Sorting & Selecting <br>
    Use `Sort-Object` (`sort`) & `Select-Object`(`select`).
    ```
    # Sort processes based on ID & VM-usage (descending). Display only ID, Name, VM, PM.
    gps | select ID,Name,VM,PM | sort VM,ID -desc
    # Save above table as HTML.
    gps | select ID,Name,VM,PM | sort VM,ID -desc | convertto-html | out-file TEST.html
    ```

- Objects: Selecting (`Sort-Object` v `Where-Object`) <br>
    `Sort-Object` lets you select/filter objects based on properties. <br>
    `Where-Object` lets you select/filter objects based on a criteria. <br>
    ```
    # List all processes with ID >= 1000, sorted in ascending order.
    gps | where {$_.Handles -ge 1000} | sort -Property Handles
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

<center><b>TODO</b></center>

- [ ] Study `ls`,`sort`,`select`,`where` cmdlets.

- [x] Get current date & time. Then, show only time.
```
get-date; get-date | select Hour,Minute,Second

Saturday, May 9, 2020 11:49:03 AM

Hour   : 11
Minute : 49
Second : 3

```

- [x] Display a list of installed hotfixes. Display installation date, installed by, and ID, sorted by installation date.
    ```
    get-hotfix | select installedon,installedby,hotfixid | sort installedon

    InstalledOn           installedby         hotfixid
    -----------           -----------         --------
    3/13/2020 12:00:00 AM NT AUTHORITY\SYSTEM KB4538674
    3/13/2020 12:00:00 AM NT AUTHORITY\SYSTEM KB4541338
    3/13/2020 12:00:00 AM NT AUTHORITY\SYSTEM KB4537759
    3/13/2020 12:00:00 AM NT AUTHORITY\SYSTEM KB4537572
    3/13/2020 12:00:00 AM NT AUTHORITY\SYSTEM KB4517245
    4/22/2020 12:00:00 AM NT AUTHORITY\SYSTEM KB4549951
    4/22/2020 12:00:00 AM NT AUTHORITY\SYSTEM KB4552152
    ```

- [x] Display a list of 10 latest Security Event-logs. Display index, time, source for each file, with the oldest entries appearing first (and same-time entries sorted by index).
    ```
    get-eventlog -logname system -newest 10 | select index,timegenerated,source | sort timegenerated,index | out-gridview

    Index TimeGenerated        Source
    ----- -------------        ------
    19167 5/9/2020 10:09:26 AM Microsoft-Windows-TPM-WMI
    19168 5/9/2020 10:09:26 AM Microsoft-Windows-Winlogon
    19169 5/9/2020 10:09:27 AM Microsoft-Windows-TPM-WMI
    19170 5/9/2020 10:11:22 AM DCOM
    19171 5/9/2020 10:11:22 AM DCOM
    19172 5/9/2020 10:11:22 AM DCOM
    19173 5/9/2020 10:11:25 AM Microsoft-Windows-FilterManager
    19174 5/9/2020 10:15:16 AM Service Control Manager
    19175 5/9/2020 10:17:21 AM Service Control Manager
    19176 5/9/2020 10:19:17 AM Microsoft-Windows-Kernel-General
    ```

## Pipelining

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
    ```
    gps | convertto-html | out-file TEST.html
    ls  | convertto-html | out-file -append TEST.html
    ```

<center><b>TODO</b></center>

- [ ] Select/Sort & save necessary columns to `TEST.html`
- [ ] Using CSS, beautiful `TEST.html`

- Compare two structured files (XML) <br>
    ```
    # List different processes running in two PCs (reference, difference).
    diff -reference (import-clixml reference.xml) -difference (gps) -property Name

    name         SideIndicator
    ----         -------------
    calc            =>
    mspaint         =>
    notepad         <=
    ```

- Output <br>
    ```
    out-file     -> O/P to file.
    out-gridview -> O/P to table in new GUI window. (*)
    out-printer  -> O/P to printer (SaveAs PDF).
    ```
    Instead of piping `>` output to a file, use `out-file`. <br>
    `out-file` lets you specify: <br>
    ```
    -append   -> append, not replace contents
    -encoding -> file encoding (ascii, unicode, utf8, oem, string)
    -width    -> set column width (default = 80 characters/line)
    ```
    ```
    # Append outputs instead of replacing.
    ls | out-file -append -width 100 TEST.txt
    ```

## Pipeline Parameter-Binding

```
PS> cmdA | cmdB
```
What goes through the `|`?

- Display processes/services from a list of computers connected to your PC.
    ```
    # computers.csv
    hostname,operatingsystem
    Feynman,windows
    ...
    ```
    ```
    # Processes
    gps -ComputerName (import-csv .\computers.csv | select -ExpandProperty hostname) | out-gridview

    # Services
    gsv -ComputerName (import-csv .\computers.csv | select -ExpandProperty hostname) | select Name,Status | sort Name | out-gridview
    ```

## Formatting

- Format-Table, Format-List, Format-Wide, Format-Custom

- Customized Formatting

- [x] Display process names, IDs, responding (to Windows or not) in a table
    ```
    gps | format-table Name,ID,Responding -autosize -wrap
    ```
- [x] Display process names, IDs, virtual/physical memory usage (in MB) in a table
    ```
    gps |
        format-table Name,ID,
        @{name='Virtual(MB)';expression={$_.vm/1MB};formatstring='F2'},
        @{name='Physical(MB)';expression={$_.workingset/1MB};formatstring='F2'} -autosize
    ```
- [x] Display available event-logs - their names and retention periods in a table
    ```
    get-eventlog -list |
        format-table @{name='Name';expression={$_.LogDisplayName}},
                     @{name='Retention(days)';expression={$_.MininumRetentionDays}}
    ```
- [x] Display service grouped-by their status (start/stop) <br>
[[OUTPUT]](services.pdf)
    ```
    gsv | sort status -desc | format-table -groupby status
    ```
- [x] Display a list of all binaries (.exe) in `C:\Windows` with their name, versionInfo & fileSize <br>
[[OUTPUT]](binaries.pdf)
    ```
    ls C:\Windows\*.exe | format-list Name,VersionInfo,@{Name='Size';Expression={$_.length}}
    ```

## Filtering & Comparisons

__The Approach__ <br>

- A. Specify what you need. <br>
- B. Filter out what you need from what PS gives you. <br>

    eg. To get a specific service, you can specify it with `get-service`. <br>
    ```
    gsv -name e*,*seo*
    ```
    But if you want a list of ONLY running services, you have to filter. <br>
    ```
    gsv -name e*,*seo* | where {$_.status -eq 'running'}
    ```
    Don't rely on headers O/P by cmdlets like `get-service` to infer it's properties. <br>
    Always use `get-member` to lookup cmdlet property names. <br>
    ```
    gsv | gm
    ```

__The Operators__ <br>
Refer `about_comparison_operators`. <br>

<center>

| Name | Description | Note |
| :-- | :--: | :--: |
| `-eq`,`-ceq` | equal to | `c` implies case-sensitive |
| `-ne`,`-cne` | not equal to | . |
| `-ge`,`-cge`,`-le`,`-cle` | greater/lesser than OR equal to | . |
| `-gt`,`-cgt`,`-lt`,`-clt` | greater/lesser than | . |
| `-and`,`-or`,`-not` | and, or, not | . |
| `-like`,`-clike` | checks matching strings | `c` implies case-sensitive |
| `-match`,`-cmatch` | matches RegEx | . |

</center>

- [x] Example (`-not`): Both these commands check if the process isn't responding.
    ```
    $_.responding -eq $False
    -not $_.responding
    ```

- [x] Display all binaries (EXE) in `C:\Windows\System32` larger than 5MB.
    ```
    ls C:\Windows\System32\*.exe | where {$_.length -gt 5MB}
    ```

- [x] Get all hotfixes that are security updates.
    ```
    get-hotfix -Description 'Security Update'
    ```

- [x] Display a list of all running processes with the name `Conhost` or `Svchost`.
    ```
    gps -name svchost,conhost | format-table -groupby name
    ```

## Remote Access
- Windows Remote Management (WinRM)
- Windows Management Instrumentation (WMI) [OLD] & the Common Information Model (CIM) [NEW] <br>
    `Get-WmiObject`,`Invoke-WmiMethod`,`GetCimInstance`,`Invoke-CimMethod` <br>
    WMI commands work over RPCs. CIM commands work over WS-MAN (WinRM). <br>
    CIM instructions need WinRM to be enabled on every PC. So, prefer the old WMI instructions. <br>

- [x] Display all HDD partitions with total/free memory.
    ```
    gwmi win32_logicaldisk |
        format-table deviceid,
        @{name='Total Memory (GB)';e={$_.size/1GB};formatstring='F2'},
        @{name='Free Memory (GB)';e={$_.freespace/1GB};formatstring='F2'}
    ```
- [x] Display list of services sorted by mode (auto, manual)
    ```
    gwmi -class win32_service -Filter "state = 'running'" | sort startmode,name
    ```

## Background Processes (aka `job`)
PS calls _'background process'_, a `job`. <br>

- Create a local background process (`job`) <br>
    Use [1] for on-spot instructions. Use [2] if instructions are retrieved from a file.
    ```
    start-job -scriptblock {...}
    start-job -filepath ...
    ```
    Although this can also work for remote execution, prefer WMI cmdlets.
    ```
    start-job -scriptblock {get-eventlog security -computerName server1,server2}
    ```

- Create a remote background process (`job`) <br>
    By default, WMI cmdlets, even if they're running on multiple PCs, do so synchronously. <br>
    This means, if PC1 has a long list of commands to execute, it will take forever to execute commands on PC2. <br>
    To do this asynchronously using background process (`job`), attach the `-asJob` parameter to the cmdlet.
    ```
    gwmi Win32_OperatingSystem -computerName (cat allservers.txt) -asJob
    ```

- Managing background processes (`job`) <br>

    ```
    Get-Job     -> Retrieve status of all jobs.
    Receive-Job -> Retrieve results of all jobs.
    Remove-Job  -> Deletes job alongwith all cached memory.
    Stop-Job    -> Terminates a blocked job.
    Wait-Job    -> Forces Shell to wait until a job is finished executing.
    ```
    Retrieving results of a job removes it from memory. To avoid this deletion, use `-keep` parameter.
    ```
    receive-job -id 1 -keep
    ```

- Scheduling background processes (`job`) <br>
    Start by creating a trigger using `New-JobTrigger`. <br>
    Set additional options using `New-ScheduledTaskOption`. <br>
    Register the job with the Task Scheduler using `Register-ScheduledJob`. <br>
    The last step defines the job in 'Task Scheduler' by writing to an XML file. <br>
    For me, this is located at `C:\Users\Chaitanya Tejaswi\AppData\Local\Microsoft\Windows\PowerShell\ScheduledJobs`. <br>

- [x] Play an audio daily at 7:30PM
    ```
    register-scheduledjob -name myDailyJobs -scriptblock {vlc "B:\CRTejaswi\Music\Anna McLuckie - Little Man On The Moon.mp3"} -trigger (new-jobtrigger -daily -at '19:30')
    ```
    While this isn't neccesary for this particular example, use this template to run with elevated privileges.
    ```
    register-scheduledjob
      -name myDailyJobs
      -scriptblock {vlc "B:\CRTejaswi\Music\Anna McLuckie - Little Man On The Moon.mp3"} -trigger (new-jobtrigger -daily -at '19:30')
      -scheduledjoboption (new-scheduledjoboption -waketorun -runelevated)
    ```
    Scheduled tasks are non-volatile, meaning they don't get erased when you close the Shell. This is because it is stored in XML files on disk (`C:\Users\Chaitanya Tejaswi\AppData\Local\Microsoft\Windows\PowerShell\ScheduledJobs`).

## Batch Cmdlets/Processing

## Variables

- Single & Double Quotes (`'`,`"`) <br>
    Anything within a single-quote is a literal string. <br>
    Anything within a double-quote is a parsed string. <br>
    ```
    PS> $var='LOCALHOST'
    PS> $var1='Try $var'
    PS> $var2="Try $var"
    PS> $var; $var1; $var2;
    LOCALHOST
    Try $var
    Try LOCALHOST
    ```
    Using double-quotes, you can also assign cmdlet & the object with it's property/method that it generates.
    ```
    PS> $services=get-service
    PS> $var="First Service Is $($services[0].name)"
    First Service Is ABLookupSvc
    ```
- Escape Sequences <br>
    Just as C-syntax uses `back-slash` (__\\__) to escape sequences, PS-syntax used `back-tick`(__\`__) <br>

- Accessing Object Property/Method <br>
    PS3+ allows using Object.Property/Object.Method syntax.
    ```
    PS> $services=Get-Service
    PS> $services.name; $services.gettype()
    ```
    Here, `Name` & `GetType()` are property/method defined on objects returned by `Get-Service`.
    Check using `gsv | gm`.

- Declaring Variable Types
    Use `[type]$var` notation.
    ```
    PS> [int]$var = Read-Host "Enter A Number"
    Enter A Number: 100
    PS> $var | gm
        TypeName: System.Int32
    ...
    ```

<center>

| Type | Description |
| :-- | :--: |
| `[int]`,`[single]`,`[double]` | integer, single/double precision floating values |
| `[char]`,`[string]` | character, string of characters |
| `[xml]` | XML document |
| `[adsi]` | ActiveDirectory Service Interface (ADSI) query |

</center>

## Regular Expressions

Pattern matching is done using `-match`&`-cmatch` operators, and `select-string` cmdlet. <br>


<center>

| Expression | Meaning |
|   :---:   |  :---:  |
| `.` | Any character (except newline) |
| `\d`, `\D` | Digit (0-9), !Digit |
| `\w`, `\W`| Word (a-z, A-Z, 0-9, _), !Word|
| `\s`, `\S` | Whitespace (space, tab, newline), !Whitespace |
| `\b`, `\B` | WordBoundary, !WordBoundary |
| `^`, `$` | Beginning/End of String |
| `[]`,`[^]`,`()`,`{}` | CharacterSet, !CharacterSet, WordGroup, #Values |

__Quantifiers__

| Expression | Meaning |
|   :---:   |  :---:  |
| `0` | >=0 |
| `+` | >=1 |
| `?` | 0 or 1 |
| `{n}` | Exact value (=n) |
| `{start, stop}` | Range of values (min, max) |

</center>

- [x] Get all files that have a 2-digit value in their name. <br>
    ```
    ls | where {$_.name -match "\d{2}"}
    ```
- [x] Display process id, name & company of all processes that are from MicroSoft. <br>
    ```
    gps | where {$_.company -match "^Microsoft"} | select name,id,company
    ```
- [x] Retrieve all DNS entries where Data property is an IPv4 address. <br>
    ```
    Get-DnsClientCache | where {$_.data -match "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"}
    ```
- [x] Retrieve IIS logfile records that contain 40x errors. <br>
    ```
    ls *.log -recurse |
        select-string -pattern "\s40[0-9]\s" |
        format-table Filename,LineNumber,Line -wrap
    ```

## Scripting

__Specifying Parameters__ <br>
    By specifying `CmdletBinding` (at the top of script), we can add several features to our parameters.

- Enabling the features <br>
    All of these features listed below need `CmdletBinding` to be enabled.
    ```
    <#
    # Comments
    #>
    [CmdletBinding()]
    ```

- Mandatory parameters <br>
    Here, we make `$myVar` a mandatory parameter. (The `HelpMessage` is optional).
    ```
    param (
        [Parameter (Mandatory=$True, HelpMessage='A variable-name is mandatory')]
        [string]$myVar,

        [int]$Var1,
        [int]$Var2,
    )
    ```

- Parameter aliases <br>
    Here, we give an alias (`name`) to `$myVar`.
    ```
    param (
        [Parameter (Mandatory=$True)]
        [Alias ('name')]
        [string]$myVar,

        [int]$Var1,
        [int]$Var2,
    )
    ```

- Validating parameter input <br>
    Here, we specify a set of valid inputs for `$Var1` & `$Var2`.
    ```
    param (
        [string]$myVar,

        [ValidateSet(0,1)]
        [int]$Var1,
        [ValidateSet(0,1)]
        [int]$Var2,
    )
    ```
    Read more about validation tricks, [here](https://jdhitsolutions.com/blog/tag/validation/).

- Using `Write-Verbose` to print progress information <br>
    Using `Write-Verbose` (instead of `Write-Host`) in our scripts allow us to optionally determine the progress of our code. <br>
    Verbose output is visible only when the script is run with `-verbose` switch. But, you cannot set its foreground/background colors (as you could with `Write-Host`), since PS has predefined color-codes for Verbose/Debug/Warning. <br>
    ```
    Write-Verbose "Using $myVar Values"
    ```

__Note__ <br>

- Prefer outputting Objects over formatted-tables.
    ```
    [NO]
    gwmi win32_logicaldisk |
        format-table deviceid,
        @{name='Total Memory (GB)';e={$_.size/1GB};formatstring='F2'},
        @{name='Free Memory (GB)';e={$_.freespace/1GB};formatstring='F2'}
    ```
    ```
    [YES]
    gwmi win32_logicaldisk |
        select deviceid,
        @{name='Total Memory (GB)';e={$_.size/1GB -as [int]}},
        @{name='Free Memory (GB)';e={$_.freespace/1GB -as [int]}}
    ```
    Here we've used `-as [int]` to round off as  `Select-Object` doesn't offer `formatstring` option. Also, outputting objects allows us to do this (something which formatted tables don't):
    ```
    .\test.ps1 | export-csv test.csv
    ```



## Formatted Data (CSV, XML, JSON)

https://www.youtube.com/watch?v=Ukuj_DxueIc&app=desktop
https://github.com/jdhitsolutions/psdatafiles/tree/master/demos

## Databases (SQLite)
http://ramblingcookiemonster.github.io/SQLite-and-PowerShell/
https://www.darkartistry.com/2019/08/create-insert-and-query-sqlite-with-powershell/


# PowerShell & Python

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

# Recipies

## Clipboard Operations (`gcb`/`scb`)

- [x] Print/Create PDF from copied text
    ```
    gcb | out-printer
    ```

- [x] Copy a filepath(s) to clipboard (So it becomes easy to paste in GUI)
    ```
    ls *.pdf | % {$_.fullname} | scb
    ```

- [x] Convert text (from docx) to epub/html/pdf
    ```
    start input.docx
    gcb | pandoc $_ --metadata title='Title' +RTS -Ksize -RTS -o output.epub
    gcb | pandoc $_ --metadata title='Title' -o output.html
    gcb | pandoc $_ --metadata title='Title' --pdf-engine=xelatex -o output.pdf
    ```

- [x] Copy code(s)/text & save as code-file/text-file <br>
    `ascii` is ideal. `utf8` gives `UTF-8 with BOM`, so, you'll have to re-encode in editor.
    ```
    gcb | out-file -Encoding ascii output.py
    gcb | out-file -Encoding utf8 output.py
    ```
    Instead of creating a new file each time, simply append to the original:
    ```
    gcb | out-file -Append -Encoding ascii output.md
    ```
    This is ideal for simultaneous Copy & Paste (if you are too lazy to use `Ctrl+C`,`Ctrl+V` repeatedly).

- [x] Open links in Firefox
    ```
    # Copied
    firefox (gcb)
    # From text-file
    firefox (cat .\input.txt)
    ```
    A better way is to create a PS User-Profile
    ```
    notepad $profile
    -> Add variables/methods... and save.
    -> Run them from Shell
    ```
    To `$profile`, append path of file containing links `$mylinks=B:\CRTejaswi\Documents\Links.txt`. <br>
    Open links using:
    ```
    firefox (cat $mylinks)
    ```
    Use `subl $mylinks` to update links you want to visit now. <br>
    Read more about PS User-Profiles using: `man about_profiles -ShowWindow`


- [x] [Eject USB drive](https://serverfault.com/a/580298)
    ```
    $driveEject = New-Object -comObject Shell.Application
    $driveEject.Namespace(17).ParseName("D:").InvokeVerb("Eject")
    ```

- [ ] Write templated strings to a file <br>
    Here, template is `file n.mp4`; n=1-27
    ```
    file 1.mp4
    file 2.mp4
    file 3.mp4
    file 4.mp4
    file 5.mp4
    file 6.mp4
    file 7.mp4
    file 8.mp4
    file 9.mp4
    file 10.mp4
    file 11.mp4
    file 12.mp4
    file 13.mp4
    file 14.mp4
    file 15.mp4
    file 16.mp4
    file 17.mp4
    file 18.mp4
    file 19.mp4
    file 20.mp4
    file 21.mp4
    file 22.mp4
    file 23.mp4
    file 24.mp4
    file 25.mp4
    file 26.mp4
    file 27.mp4
    ```

- [ ] Print strings following a matching sub-string <br>
    From CONFIG, I want to query the cmd to merge files using FFmpeg. <br>
    Logic:
      -> print 10 lines after a 'merge' (inclusive) is encountered.

    This cmd gets `ffmpeg` lines out of CONFIG.
    ```
    cat $myconfig | ? {$_ -match 'ffmpeg'}
    ```
    https://devtipscurator.wordpress.com/2016/11/25/how-to-filter-contents-in-a-text-file-using-powershell/

## HTTP Requests

PS gives `Invoke-WebRequest` (aka `curl`) to work with webpages. <br>

- __NOTE:__ Before doing anything useful, make sure to install & configure Internet Explorer. (Although you can make do without this by using `-UseBasicParsing` switch; this is an absolutely fuckall workaround. This is because using it doesn't give you access to the webpage's DOM, which means, you cannot parse it, or get anything useful out of it. It's like standing with a gun - a water gun. So, just install the damn thing!) <br>

    - Install from [here](https://support.microsoft.com/en-in/help/17621/internet-explorer-downloads).
    - To configure, `Win+I` >> Apps & Features >> Optional Features >> Add a feature >> Internet Explorer 11. Then, `Win+R` >> Control >> Turn Windows Features ON/OFF >> [x] Internet Explorer. Restart PC. <br>
    - Open up Internet Explorer, set to `Recommended Settings`. Done! <br>

- [x] Get contents of a URL <br>
    This generates a local copy of my [CV](https://crtejaswi.github.io/CV).
    ```
    $response = Invoke-WebRequest -Uri crtejaswi.github.io/CV
    $response.Content | out-file -encoding utf8 test.html
    ```
- [x] Get all links from a webpage <br>
    This gets all links from my [CV](https://crtejaswi.github.io/CV).
    ```
    $links = (curl crtejaswi.github.io/CV -UseBasicParsing).links.href
    ```

- [x] Get weather temperatures <br>
    Retrieving data for Delhi (28.7041° N, 77.1025° E).
    ```
    $myurl = 'https://weather.com/en-IN/weather/today/l/28.7041,77.1025?temp=c'
    $response = curl -Uri $myurl
    ($response.allelements | where { $_.class -Match "\w+--location--\w+" -or $_.class -Match "\w+--tempHiLoValue--\w+" }).innerText

    Rohini Sector 2, Delhi Weather
    35°/26°
    ```