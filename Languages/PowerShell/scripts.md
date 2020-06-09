    Copyright(c) 2020-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# PowerShell Scripts
> Personal scripts.

# Index

- [YouTube](#youtube)

## Youtube

- [x] Gather list of videos/playlists for a YouTube user/channel. <br>
    I've managed to scrape link ids for videos/playlists and stored them to a JSON file. To build full links, you can easily use `$baseURL/watch?v=$video` & `$baseURL/playlist?list=$video` to build absolute links. The major issue with v1/v2 is that not all links are retrieved (eg. `jabykoay` yields 110 videos when there are many more). [Prateek Singh's implementation] uses DOM instead of simple query like mine. This way, you can get title of videos as well. But his way also has the same issue - his gets fewer videos than mine.

<details>
<summary> v1 </summary>

> CHANGES: See implementation of `$content`. No duplicate videos/playlist link except ones that contain both video & playlist reference in same link.

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
<summary> v2 </summary>

> CHANGES: See implementation of `$content`. Several duplicate videos/playlist links are present.

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