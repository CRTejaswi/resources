    Copyright(c) 2021-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+

# CC++
> Personal notes.

# Resources

| Link | Description |
| :--: | :-- |
| | DDescription escription |

# Index

- [Setup](#setup)

## Setup

Commonly used Compiler-suites for CC++ programming are GCC & MSVC.

On Windows, you can install GCC using [TDM-MinGW64](https://jmeubank.github.io/tdm-gcc/), and MSVC using [Build Tools for Visual Studio 2019](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019). (A complete Visual Studio IDE installation should be deffered in my opinion. Use the MSVC++ compiler `cl` only through aforementioned minimal installation. Here's a [hello world implementation](https://docs.microsoft.com/en-us/cpp/build/walkthrough-compiling-a-native-cpp-program-on-the-command-line?view=msvc-160#create-a-visual-c-source-file-and-compile-it-on-the-command-line) using `cl`.

As a learner, the primary advantage that MSVC offers over GCC is ["windows.h"](https://en.wikipedia.org/wiki/Windows.h) (aka: Windows API), which allows use to create Windows-native utilities. As far as coding practice is concerned, GCC is sufficient. If you work with your code in PowerShell, for system-programming, you can easily use its cmdlets to do all the heavy-lifting, and return the output to your CC++ program.

Here's an example that can be compiled with `gcc` on Windows:
```c
#include <stdio.h>
#include <stdlib.h>


int main(){
    // Lists items in current directory.
    return system("powershell Get-ChildItem .");
}
```
Although this isn't the way you should be coding in CC++, it's something pretty useful that should be aware of, early on. (FYI, it took me years to figure this out myself).

