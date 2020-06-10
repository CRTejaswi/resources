    Copyright(c) 2020-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# PowerShell Scripts
> Personal scripts.

# Index

- [YouTube](#youtube)

## Youtube

- [x] __Gather list of videos/playlists for a YouTube user/channel.__ <br>
    I've managed to scrape link ids for videos/playlists and store them to a JSON file. [[jabykoay]](jabykoay.json) [[teamcoco]](teamcoco.json) <br>
    You can easily use `$baseURL/watch?v=$video` & `$baseURL/playlist?list=$video` to build absolute links. <br>
    The major issue with v2A,B is that not all links are retrieved (eg. `jabykoay` yields 110 videos when there are many more). [Prateek Singh's implementation](https://github.com/PrateekKumarSingh/PowershellScrapy/blob/master/Youtube/Get-YoutubeVideo.ps1) uses DOM instead of simple query like mine. This way, you can get title of videos as well. But his way also has the same issue - his gets fewer videos than mine.

<details>
<summary> v1 </summary>

> Gets Youtube playlists for a user, saves them to file, and opens all of them using a browser.

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
