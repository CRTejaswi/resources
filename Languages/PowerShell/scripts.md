    Copyright(c) 2020-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# PowerShell Scripts
> Personal scripts.

# Index

- [Basics](#basics)
- [Logins](#logins)
- [YouTube](#youtube)
- [Structured Data (CSV, JSON, XML)](#structured-data-csv-json-xml)

## Basics

- [x] Calculate the sum of even numbers in the range 1-100.

```powershell
$range = 1..100; $range | where {$_ % 2 -eq 0} | measure -Sum

(1..100 | where {-not ($_ % 2)} | measure -Sum).sum
```

- [x] Calculate the sum of multiples of __k__ within a range __start-stop__.

```powershell
function Get-mySum{
    [cmdletBinding()]
    param(
        [Parameter (Position=0,Mandatory=$True)]
        [int32]$Start,
        [Parameter (Position=1,Mandatory=$True)]
        [int32]$Stop,
        [Parameter (Position=2,Mandatory=$True)]
        [int32]$Base
    )

    ($Start..$Stop | where {-not ($_ % $Base)} | measure -Sum).sum
}
```

- [x] Calculate sum, values & average of multiples of __k__ within a range __start-stop__.

```powershell
function Get-myStats{
    [cmdletBinding()]
    param(
        [Parameter (Position=0,Mandatory=$True)]
        [int32]$Start,
        [Parameter (Position=1,Mandatory=$True)]
        [int32]$Stop,
        [Parameter (Position=2,Mandatory=$True)]
        [int32]$Base
    )

    $values = @()
    $values += $Start..$Stop | where {-not ($_ % $Base)}
    $sum = ($values | measure -sum).sum

    [PSCustomObject]@{
        Start   = $Start
        Stop    = $Stop
        Base    = $Base
        Values  = $values
        Sum     = $sum
        Average = $sum / $values.count
    }
}
```
```
Get-myStats 1 100 5


Start   : 1
Stop    : 100
Base    : 5
Values  : {5, 10, 15, 20...}
Sum     : 1050
Average : 52.5
```

- [x] Code-File Inventory [\*](https://ironscripter.us/building-a-powershell-command-inventory/) <br>
    Count no. of lines of code in files of a given directory. <br>

```powershell
$Path = 'B:\'

# PowerShell files
ls -Path $Path -Filter '*.ps*' -Recurse |
    where {$_.extension -match "\.ps[md]?1$"} -outvariable files |
    cat | measure -line |
    select @{name='Path';expression={$Path}},
    @{name='TotalFiles';expression={$files.count}},
    lines,
    @{name='Date';expression={get-date -Format 'dd-MM-yy hh:mm:ss'}}
# Python files
ls -Path $Path -Filter '*.py' -Recurse -outvariable files |
    cat | measure -line |
    select @{name='Path';expression={$Path}},
    @{name='TotalFiles';expression={$files.count}},
    lines,
    @{name='Date';expression={get-date -Format 'dd-MM-yy hh:mm:ss'}}
```
```
Path TotalFiles Lines Date
---- ---------- ----- ----
B:\          17  1297 22-06-2020 11:29:54

Path TotalFiles   Lines Date
---- ----------   ----- ----
B:\        9392 2137211 22-06-2020 11:31:48
```

```powershell
function Get-CodeFileLines{
    [cmdletBinding()]
    param(
        [Parameter (Position=0,Mandatory=$True)]
        [string]$Path,
        [Parameter (Position=1,Mandatory=$True)]
        [ValidateSet('.py','.c','.cpp','.h','.hpp','.asm','.hs','.js','.ps1')]
        [string]$Name
    )

    ls -Path $Path -Filter "*$Name" -Recurse -outvariable files |
        cat | measure -line |
        select @{name='Path';expression={$Path}},
        @{name='TotalFiles';expression={$files.count}},
        lines,
        @{name='Date';expression={Get-Date -Format 'dd-MM-yyyy hh:mm:ss'}}

}
```
```
Get-CodeFileLines B:\ .ps1; Get-CodeFileLines B:\ .js;

Path TotalFiles Lines Date
---- ---------- ----- ----
B:\           3   356 22-06-2020 11:39:44

Path TotalFiles Lines Date
---- ---------- ----- ----
B:\        3804 668922 22-06-2020 11:41:18
```

- [x] Output Code into Markdown files

```powershell
function Out-mdNotes{
    [cmdletBinding()]
    param(
        [Parameter (Position=0,Mandatory=$True)]
        [System.IO.FileInfo]$Path,
        [Parameter (Position=1)]
        [System.IO.FileInfo]$FilePath
    )
    $page = @()

    if ($PSBoundParameters.containsKey('Path')){
        switch ($Path.extension){
            '.py' {
                $page += '```python',(cat $Path),'```','```',(python $Path),'```'
            }
            '.c' {
                $page += '```c',(cat $Path),'```','```',($Path.fullname.split('.')[0]+'.exe'),'```'
            }
            '.js' {
                $page += '```javascript',(cat $Path),'```','```',(node $Path),'```'
            }
            default {
                Write-Host "Unknown Language!"
            }
        }
    }
    Write-Verbose "$page"
    $page | Out-File -Encoding utf8 $FilePath -Append
}
```

<center>
    <b>Issue</b> <br></center>
    <img src="resources/Out-mdNotes.png" title="Issue with console.table()">
</center>

## Logins

- [x] __Open webpage in browser & copy credentials for manual login__ <br>
    This queries a [`$myLogins=logins.csv`](https://raw.githubusercontent.com/CRTejaswi/API/master/logins.csv) file for entries, and copies username/password to clipboard. <br>
    It also opens the webpage in a browser to manually login (-disable using `-PassThru`). <br>
    The `$PSBoundParameters.ContainsKey('<param>')` check is unnecessary since there aren't many columns to access, and doing so is verbose. <br>

<details>
<summary> v1 </summary>

```powershell
# get-login -gdrive

function Get-Login{
    [cmdletBinding()]
    param(

        [Parameter (Mandatory=$True)]
        [string]$Site,

        [switch]$PassThru
    )

    $logins = import-csv $myLogins
    $match = $logins | where site -eq $Site
    if (-not $PassThru) {firefox $match.link}
    $match.username,$match.password | scb
}
```

</details>

<details>
<summary> v2 </summary>

> CHANGES: Added `-List` option.

```powershell
# get-login -list
# get-login -gdrive

function Get-Login{
    [cmdletBinding()]
    param(
        [string]$Site,
        [switch]$List,
        [switch]$PassThru
    )

    $logins = import-csv $myLogins
    if ($List) {$logins.site}
    $match = $logins | where site -eq $Site
    if (-not $PassThru -and -not $List) {firefox $match.link}
    $match.username,$match.password | scb
}
```

</details>

- [x] __Get song lyrics; open in browser.__ <br>

```powershell
# get-lyrics edsheeran beautifulpeople

function Get-Lyrics{
    [cmdletBinding()]
    param(
        [Parameter (Mandatory=$True)]
        [string]$Artist,
        [Parameter (Mandatory=$True)]
        [string]$Song
    )

    $link = "https://www.azlyrics.com/lyrics/$Artist/$Song.html"
    firefox $link
}
```

## Youtube

- [x] __Gather list of videos/playlists for a YouTube user/channel.__ <br>
    I've managed to scrape link ids for videos/playlists and store them to a JSON file. [[jabykoay]](resources/jabykoay.json) [[teamcoco]](resources/teamcoco.json) <br>
    You can easily use `$baseURL/watch?v=$video` & `$baseURL/playlist?list=$video` to build absolute links. <br>
    The major issue with v2A,B is that not all links are retrieved (eg. `jabykoay` yields 110 videos when there are many more). [Prateek Singh's implementation](https://github.com/PrateekKumarSingh/PowershellScrapy/blob/master/Youtube/Get-YoutubeVideo.ps1) uses DOM instead of simple query like mine. This way, you can get title of videos as well. But his way also has the same issue - his gets fewer videos than mine.

<details>
<summary> v1 </summary>

> Gets Youtube playlists for a user, saves them to file, and opens all of them in a browser.

```powershell
$tmp = New-TemporaryFile; $page = @();
$URI = 'https://www.youtube.com/user/jabykoay'
$response = curl -Uri $URI
$links = $response.links
$page += $links.href -match '^/playlist'
$page.count # 13
$page.replace('/playlist', 'www.youtube.com/playlist') | out-file $tmp.fullname
firefox (cat $tmp.fullname)
```
</details>

<details>
<summary> v2A </summary>

> CHANGES: See implementation of `$content`. No duplicate video/playlist link except ones that contain both video & playlist reference in same link.

```powershell
function Get-YouTubeVideos{
    [cmdletBinding()]
    param(

        [Parameter (Mandatory=$True)]
        [string]$Name,

        [ValidateSet('user','channel', 'c')]
        [string]$Id
    )

    $URI = "https://www.youtube.com/$Id/$Name"
    $response = Invoke-WebRequest -Uri $URI
    $links = $response.links
    $content = @{'videos'=@(); 'playlists'=@()}
    $content.videos = $links.href -match '^/watch\?v=' -replace '^/watch\?v=','' | Get-Unique;
    $content.playlists = $links.href -match '^/playlist\?list=' -replace '^/playlist\?list=','' | Get-Unique;

    return $content
}
```
```
Get-YouTubeVideos -Name 'jabykoay' -id 'user' | ConvertTo-Json | Out-File -encoding ascii jabykoay.json
Get-YouTubeVideos -Name 'teamcoco' -id 'user' | ConvertTo-Json | Out-File -encoding ascii teamcoco.json
```

</details>

<details>
<summary> v2B </summary>

> CHANGES: See implementation of `$content`. Several duplicate video/playlist links are present.

```powershell
function Get-YouTubeVideos{
    [cmdletBinding()]
    param(

        [Parameter (Mandatory=$True)]
        [string]$Name,

        [ValidateSet('user','channel', 'c')]
        [string]$Id
    )

    $URI = "https://www.youtube.com/$Id/$Name"
    $response = Invoke-WebRequest -Uri $URI
    $links = $response.links
    $content = @{'videos'=@(); 'playlists'=@()}
    switch -regex ($links.href){
        '^/watch\?v=' {
            $content.videos += ($_ -replace '^/watch\?v=','')
        }
        '^/playlist\?list=' {
            $content.playlists += ($_ -replace '^/playlist\?list=','')
        }
    }

    return $content
}
```
```
Get-YouTubeVideos -Name 'jabykoay' -id 'user' | ConvertTo-Json | Out-File -encoding ascii jabykoay.json
Get-YouTubeVideos -Name 'teamcoco' -id 'user' | ConvertTo-Json | Out-File -encoding ascii teamcoco.json
```

</details>

## Unsorted

- [x] Write a utility that gets technical specifications of remote PCs. <br>
Each entry is logged into a database. If this fails, log error info in a file.

```powershell
<#
.SYNOPSIS
Gets system-specifications of remote computers on a CIM server.
.EXAMPLE
PS> Get-MachineInfo -ComputerName localhost
ComputerName Version    ServicePackMajorVersion
------------ -------    -----------------------
localhost    10.0.18363                       0
#>

function Get-MachineInfo {
    param (
        [string[]]$ComputerName,
        [string]$LogFailuresToPath,
        [string]$Protocol = 'wsman',
        [switch]$ProtocolFallback
    )

    forEach ($name in $computername){
        if ($protocol -eq 'DCom'){
            $option = New-CimSessionOption -Protocol DCom
        } else {
            $option = New-CimSessionOption -Protocol WSMan
        }

        $session = New-CimSession -ComputerName $name -SessionOption $option
        $os = Get-CimInstance -ClassName Win32_OperatingSystem -CimSession $session
        $session | Remove-CimSession
        $os | Select-Object -Property @{n='ComputerName'; e={$name}},Version,ServicePackMajorVersion
    }
}
```
```
PS> import-module -name 'C:\Users\Chaitanya Tejaswi\Documents\WindowsPowerShell\Modules\myTest' -force -verbose

VERBOSE: Loading module from path 'C:\Users\Chaitanya Tejaswi\Documents\WindowsPowerShell\Modules\myTest\myTest.psm1'.
VERBOSE: Exporting function 'Get-MachineInfo'.
VERBOSE: Importing function 'Get-MachineInfo'.```

PS> Get-MachineInfo -ComputerName localhost

ComputerName Version    ServicePackMajorVersion
------------ -------    -----------------------
localhost    10.0.18363                       0
```

- [x] Write a utility that changes logon passwords of services of remote PCs. <br>
If this fails, log error info in a file. Passwords may be supplied as plain string.

```powershell
<#
.SYNOPSIS
Sets logon passwords of services of remote computers on a CIM server.
.EXAMPLE
PS> Set-ServiceLogon -ComputerName localhost
                     -ServiceName BITS
                     -NewPassword 'P@ssw0rd'

PS> Set-ServiceLogon -ComputerName S1,S2
                     -ServiceName BITS
                     -NewPassword 'P@ssw0rd'
                     -NewUser 'COMPANY\User'
#>

function Set-ServiceLogon {
    param (
        [string[]]$ComputerName,
        [string]$ServiceName,
        [string]$NewUser,
        [string]$NewPassword,
        [string]$ErrorLogFilePath
    )

    forEach ($name in $computername){
        $option = New-CimSessionOption -Protocol WSMan
        $session = New-CimSession -ComputerName $name -SessionOption $option

        if ($PSBoundParameters.ContainsKey('NewUser')){
            $args = @{'StartName'=$NewUser; 'StartPassword'=$NewPassword}
        } else {
            $args = @{'StartPassword'=$NewPassword}
        }

        Invoke-CimMethod -ComputerName $name -MethodName Change `
                         -Query "SELECT * FROM  Win32_Service WHERE name='$ServiceName'" `
                         -Arguments $args |
                            Select-Object -Property @{n='ComputerName'; e={$name}} `
                                                    @{n='Result'; e={$_.ReturnValue}}

        $session | Remove-CimSession
    }
}
```

## Structured Data (CSV, JSON, XML)

- [x] Given a CSV file with `IP address, Department` entries, create a report containing DNS names of these computers with an access timestamp.

    ```powershell
    function Get-PCNames{
        [cmdletBinding()]
        param(

            [Parameter (Mandatory=$True)]
            [string]$Path,
        )

        $rows = Import-Csv $Path
        forEach ($row in $rows){
            try {
                $output = [PSCustomObject]  @{
                    IPAddress  = $row.IPAddress
                    Department = $row.Department
                    IsOnline   = $False
                    HostName   = $Null
                    Error      = $Null
                    Timestamp  = Get-Date -Format 'dd-MM-yy hh:mm:ss tt'
                }
                # Ping each IP address with an ICMP packet
                if (Test-Connection -ComputerName $row.IPAddress -Count 1 -Quiet){
                    $output.IsOnline = $True
                }
                # Get HostName of each IPAddress
                if ($hostname = (Resolve-DnsName -Name $row.IPAddress -ErrorAction Stop).Name){
                    $output.HostName = $hostname
                }
            } catch {
                $output.Error = $_.Exception.Message
            } finally {
                $output
            }
        }
    }
    ```
    ```
    Get-PCNames -Path .\test.csv | Export-Csv -Path .\results.csv -Append -NoTypeInformation
    ```