    Copyright(c) 2020-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# JS
> Personal notes for JS.

# References (General)

# Index

- [General](#general)
- [CLI/GUI](#cligui)
- [Structured Data (CSV, JSON, XML)](#structured-data-csv-json-xml)
- [Databases](#databases)
- [JS Engines](#js-engines)
- Book: Learn ECMAscript (Prusty)
    01. Introduction
    02. Standard Library
    03. Functional Programming
    04. Asynchronous Programming
    05. [Modular Programming](05.md)
    06. [API - Reflect](06.md)
    07. API - Proxy
    08. Object-oriented Programming
    09. Web (DOM) Programming
    10. API - Storage
    11. Web/Service Workers
    12. Shared Memory & Atomics

## General

- Access Environment Variables <br>
    Environment Variables can't be accessed in plain JS. <br>
    You can access User/System environment variables in NodeJS using [dotenv](https://github.com/motdotla/dotenv) package:
    ```
    require('dotenv').config();
    console.log(process.env.Youtube_ApiKey); // <API_KEY>
    ```
    This approach gets values from a file - `.env` (and not from your PC). So, eh?!

## CLI/GUI


## Structured Data (CSV, JSON, XML)

Refer:

__CSV__ <br>

__JSON__ <br>

__XML__ <br>

## Databases

## JS Engines

[SpiderMonkey](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey) by Mozilla & [V8](https://v8.dev/docs) by Google are two major JS engines out there; both written in C/C++. <br>
Install [JS Shell Utility](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Introduction_to_the_JavaScript_shell). <br>
See [Yulia Startsev's streams](https://developer.mozilla.com/events/compiler-compiler-yulia-startsev/) to get started with SpiderMonkey. Later on, decide which project to focus on. <br>