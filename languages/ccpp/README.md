    Copyright(c) 2021-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+

# CC++
> Personal notes.

# Index

- [Resources](#resources)
- [Setup](#setup)
- [Projects](#projects)

## Resources

| Link | Description |
| :--: | :-- |
| [Projects](#projects) | Useful list of projects |
|[Cpp: System Programming](https://www.packtpub.com/product/c-system-programming-cookbook/9781838646554) |  |
|[C: Linux Programming (CodeSorcery)](https://mentorembedded.github.io/advancedlinuxprogramming/) |  |
| [WebAssembly](https://www.packtpub.com/product/learn-webassembly/9781788997379) |  |

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

## Projects
(currently lifted from https://github.com/tuvtran/project-based-learning#cc)

- [Build an Interpreter](http://www.craftinginterpreters.com/) (Chapter 14 on is written in C)
- [Memory Allocators 101 - Write a simple memory allocator](https://arjunsreedharan.org/post/148675821737/memory-allocators-101-write-a-simple-memory)
- [Write a Shell in C](https://brennan.io/2015/01/16/write-a-shell-in-c/)
- [Write a FUSE Filesystem](https://www.cs.nmsu.edu/~pfeiffer/fuse-tutorial/)
- [Build Your Own Text Editor](http://viewsourcecode.org/snaptoken/kilo/)
- [Build Your Own Lisp](http://www.buildyourownlisp.com/)
- [How to Program an NES Game in C](https://nesdoug.com/)
- [Write an OS from scratch](https://github.com/tuhdo/os01)
- [How to create an OS from scratch ](https://github.com/cfenollosa/os-tutorial)
- [Building a CHIP-8 Emulator](https://austinmorlan.com/posts/chip8_emulator/)
- [Beginning Game Programming with C++ and SDL](http://lazyfoo.net/tutorials/SDL/)
- [Implementing a Key-Value Store](http://codecapsule.com/2012/11/07/ikvs-implementing-a-key-value-store-table-of-contents/)
- Tiny 3D graphics projects
  - [Tiny Renderer or how OpenGL works: software rendering in 500 lines of code](https://github.com/ssloy/tinyrenderer/wiki)
  - [Understandable RayTracing in 256 lines of bare C++](https://github.com/ssloy/tinyraytracer/wiki)
  - [KABOOM! in 180 lines of bare C++](https://github.com/ssloy/tinykaboom/wiki)
  - [486 lines of C++: old-school FPS in a weekend](https://github.com/ssloy/tinyraycaster/wiki)
- Writing a minimal x86-64 JIT compiler in C++
  - [Part 1](https://solarianprogrammer.com/2018/01/10/writing-minimal-x86-64-jit-compiler-cpp/)
  - [Part 2](https://solarianprogrammer.com/2018/01/12/writing-minimal-x86-64-jit-compiler-cpp-part-2/)
- [Build a Live Code-reloader Library for C++](http://howistart.org/posts/cpp/1/index.html)
- [Write a hash table in C](https://github.com/jamesroutley/write-a-hash-table)
- [Let's Build a Simple Database](https://cstack.github.io/db_tutorial/)
- [Let's Write a Kernel](http://arjunsreedharan.org/post/82710718100/kernel-101-lets-write-a-kernel)
- [Write a Bootloader in C](http://3zanders.co.uk/2017/10/13/writing-a-bootloader/)
- [Linux Container in 500 Lines of Code](https://blog.lizzie.io/linux-containers-in-500-loc.html)
- [Write Your Own Virtual Machine](https://justinmeiners.github.io/lc3-vm/)
- [Learning KVM - Implement Your Own Linux Kernel](https://david942j.blogspot.com/2018/10/note-learning-kvm-implement-your-own.html)
- Write a C compiler
  - [Part 1: Integers, Lexing and Code Generation](https://norasandler.com/2017/11/29/Write-a-Compiler.html)
  - [Part 2: Unary Operators](https://norasandler.com/2017/12/05/Write-a-Compiler-2.html)
  - [Part 3: Binary Operators](https://norasandler.com/2017/12/15/Write-a-Compiler-3.html)
  - [Part 4: Even More Binary Operators](https://norasandler.com/2017/12/28/Write-a-Compiler-4.html)
  - [Part 5: Local Variables](https://norasandler.com/2018/01/08/Write-a-Compiler-5.html)
  - [Part 6: Conditionals](https://norasandler.com/2018/02/25/Write-a-Compiler-6.html)
  - [Part 7: Compound Statements](https://norasandler.com/2018/03/14/Write-a-Compiler-7.html)
  - [Part 8: Loops](https://norasandler.com/2018/04/10/Write-a-Compiler-8.html)
  - [Part 9: Functions](https://norasandler.com/2018/06/27/Write-a-Compiler-9.html)
  - [Part 10: Global Variables](https://norasandler.com/2019/02/18/Write-a-Compiler-10.html)
- [Implementing a Language with LLVM](https://llvm.org/docs/tutorial/#kaleidoscope-implementing-a-language-with-llvm)
- [Meta Crush Saga: a C++17 compile-time game](https://jguegant.github.io//jguegant.github.io/blogs/tech/meta-crush-saga.html)
- [High-Performance Matrix Multiplication](https://gist.github.com/nadavrot/5b35d44e8ba3dd718e595e40184d03f0)
- Space Invaders from Scratch
  - [Part 1](http://nicktasios.nl/posts/space-invaders-from-scratch-part-1.html)
  - [Part 2](http://nicktasios.nl/posts/space-invaders-from-scratch-part-2.html)
  - [Part 3](http://nicktasios.nl/posts/space-invaders-from-scratch-part-3.html)
  - [Part 4](http://nicktasios.nl/posts/space-invaders-from-scratch-part-4.html)
  - [Part 5](http://nicktasios.nl/posts/space-invaders-from-scratch-part-5.html)
- [Tetris Tutorial in C++ Platform Independent](http://javilop.com/gamedev/tetris-tutorial-in-c-platform-independent-focused-in-game-logic-for-beginners/)
- Writing a Linux Debugger
  - [Part 1: Setup](https://blog.tartanllama.xyz/writing-a-linux-debugger-setup/)
  - [Part 2: Breakpoints](https://blog.tartanllama.xyz/writing-a-linux-debugger-breakpoints/)
  - [Part 3: Registers and memory](https://blog.tartanllama.xyz/writing-a-linux-debugger-registers/)
  - [Part 4: Elves and dwarves](https://blog.tartanllama.xyz/writing-a-linux-debugger-elf-dwarf/)
  - [Part 5: Source and signals](https://blog.tartanllama.xyz/writing-a-linux-debugger-source-signal/)
  - [Part 6: Source-level stepping](https://blog.tartanllama.xyz/writing-a-linux-debugger-dwarf-step/)
  - [Part 7: Source-level breakpoints](https://blog.tartanllama.xyz/writing-a-linux-debugger-source-break/)
  - [Part 8: Stack unwinding](https://blog.tartanllama.xyz/writing-a-linux-debugger-unwinding/)
  - [Part 9: Handling variables](https://blog.tartanllama.xyz/writing-a-linux-debugger-variables/)
  - [Part 10: Advanced topics](https://blog.tartanllama.xyz/writing-a-linux-debugger-advanced-topics/)

### Network programming

- Let's Code a TCP/IP Stack

  - [Part 1: Ethernet & ARP](http://www.saminiir.com/lets-code-tcp-ip-stack-1-ethernet-arp/)
  - [Part 2: IPv4 & ICMPv4](http://www.saminiir.com/lets-code-tcp-ip-stack-2-ipv4-icmpv4/)
  - [Part 3: TCP Basics & Handshake](http://www.saminiir.com/lets-code-tcp-ip-stack-3-tcp-handshake/)
  - [Part 4: TCP Data Flow & Socket API](http://www.saminiir.com/lets-code-tcp-ip-stack-4-tcp-data-flow-socket-api/)
  - [Part 5: TCP Retransmission](http://www.saminiir.com/lets-code-tcp-ip-stack-5-tcp-retransmission/)

- Programming concurrent servers
  - [Part 1 - Introduction](https://eli.thegreenplace.net/2017/concurrent-servers-part-1-introduction/)
  - [Part 2 - Threads](https://eli.thegreenplace.net/2017/concurrent-servers-part-2-threads/)
  - [Part 3 - Event-driven](https://eli.thegreenplace.net/2017/concurrent-servers-part-3-event-driven/)
  - [Part 4 - libuv](https://eli.thegreenplace.net/2017/concurrent-servers-part-4-libuv/)
  - [Part 5 - Redis case study](https://eli.thegreenplace.net/2017/concurrent-servers-part-5-redis-case-study/)
  - [Part 6 - Callbacks, Promises and async/await](https://eli.thegreenplace.net/2018/concurrent-servers-part-6-callbacks-promises-and-asyncawait/)
 
- MQTT Broker from scratch
  - [Part 1 - The protocol](https://codepr.github.io/posts/sol-mqtt-broker)
  - [Part 2 - Networking](https://codepr.github.io/posts/sol-mqtt-broker-p2)
  - [Part 3 - Server](https://codepr.github.io/posts/sol-mqtt-broker-p3)
  - [Part 4 - Data structures](https://codepr.github.io/posts/sol-mqtt-broker-p4)
  - [Part 5 - Topic abstraction](https://codepr.github.io/posts/sol-mqtt-broker-p5)
  - [Part 6 - Handlers](https://codepr.github.io/posts/sol-mqtt-broker-p6)
  - [Bonus - Multithreading](https://codepr.github.io/posts/sol-mqtt-broker-bonus)

### OpenGL:

- Creating 2D Breakout game clone in C++ with OpenGL
  - [Breakout](https://learnopengl.com/In-Practice/2D-Game/Breakout)
  - [Setting up](https://learnopengl.com/In-Practice/2D-Game/Setting-up)
  - [Rendering Sprites](https://learnopengl.com/In-Practice/2D-Game/Rendering-Sprites)
  - [Levels](https://learnopengl.com/In-Practice/2D-Game/Levels)
  - Collisions
    - [Ball](https://learnopengl.com/In-Practice/2D-Game/Collisions/Ball)
    - [Collision detection](https://learnopengl.com/In-Practice/2D-Game/Collisions/Collision-detection)
    - [Collision resolution](https://learnopengl.com/In-Practice/2D-Game/Collisions/Collision-resolution)
  - [Particles](https://learnopengl.com/In-Practice/2D-Game/Particles)
  - [Postprocessing](https://learnopengl.com/In-Practice/2D-Game/Postprocessing)
  - [Powerups](https://learnopengl.com/In-Practice/2D-Game/Powerups)
  - [Audio](https://learnopengl.com/In-Practice/2D-Game/Audio)
  - [Render text](https://learnopengl.com/In-Practice/2D-Game/Render-text)
  - [Final thoughts](https://learnopengl.com/In-Practice/2D-Game/Final-thoughts)
- [Handmade Hero](https://handmadehero.org)
- [How to Make Minecraft in C++/OpenGL](https://www.youtube.com/playlist?list=PLMZ_9w2XRxiZq1vfw1lrpCMRDufe2MKV_) (video)

