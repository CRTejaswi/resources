    Copyright(c) 2020-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# JS
> Personal notes for JS.

# References (General)

[__Beau Carnes__](https://www.youtube.com/playlist?list=PL9WLlXArXbtcuYmDjagcHEN4pa24BC5iW) <br>
[__Brad Traversy__](https://www.youtube.com/user/TechGuyWeb/videos) <br>

# Index

- [General](#general)
- [CLI/GUI](#cligui)
- [Structured Data (CSV, JSON, XML)](#structured-data-csv-json-xml)
- [Databases](#databases)
- [JS Engines](#js-engines)
- [SVG](#svg)
- [D3js](#data-visualization)
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
Also see [Firefox: JS Interpreter](https://developer.mozilla.org/en-US/docs/Tools/Web_Console/The_command_line_interpreter) <br>
See [Yulia Startsev's streams](https://developer.mozilla.com/events/compiler-compiler-yulia-startsev/) to get started with SpiderMonkey. Later on, decide which project to focus on. <br>

## SVG

Refer: [Basics](https://codepen.io/crtejaswi/pen/GRowgmB), [Tutorial](https://www.w3.org/Graphics/SVG/IG/resources/svgprimer.html), [Tutorial](http://tutorials.jenkov.com/svg/index.html) & [Videos](https://www.youtube.com/playlist?list=PLL8woMHwr36F2tCFnWTbVBQAGQ6nTcXOO), [SVG Elements](https://developer.mozilla.org/en-US/docs/Web/SVG/Element#SVG_elements_by_category).

__Shapes__ <br>

<center>

| Tag | Attributes |
| :--: | :-- |
| `<line>` | `x1,y1,x2,y2`, `stroke`,`stroke-width`, `stroke-linecap`, `stroke-dasharray` |
| `<polyline>` | `points`, `fill`, `stroke`,`stroke-width`, `stroke-linecap`, `stroke-dasharray` |
| `<rect>` | `x,y`, `width,height`, `fill`, `stroke`,`stroke-width` |
| `<polygon>` | |
| `<circle>` | `cx,cy,r`, `fill`, `stroke`,`stroke-width`, `stroke-dasharray` |
| `<ellipse>` | `cx,cy,rx,ry`, `fill`, `stroke`,`stroke-width`, `stroke-dasharray` |
| `<path>` | `d (M-LQCA)`, `fill`, `stroke`,`stroke-width`, `stroke-dasharray` |
| `<text>` | `x,y`, `fill`, `font`, `font-family`, `font-size` |
| `<image>` | `xlink:href`, `x,y`, `width,height`, `preserveAspectRatio` |
| `<marker>` | `id`, `refX,refY`, `viewBox`, `markerWidth,markerHeight`, `orient`, `preserveAspectRatio` |

</center>

`<path>` is the most import shape, with a curve sketched by `M-LQCA` ("Move to M(x,y), then move linearly/quadratically/cubically/on an ellipticalArc").
```xml
<path d="M 0,0 L 100,0" fill="none" stroke="#000000"/>
<path d="M 0,0 Q 150,200 100,100 z" fill="none" stroke="#ff0000"/>
<path d="M 0,0 C 150,200 150,150 100,100 z" fill="none" stroke="#00ff00"/>
<path d="M 0,0 A 150,200 0 0,0 100,100 z" fill="none" stroke="#0000ff"/>
```

<img src="resources/svg1.png">


## Data Visualization

Refer: [Basics](https://codepen.io/crtejaswi/pen/wvMQBpO), [Tutorial](https://observablehq.com/collection/@d3/learn-d3), [Video](https://www.youtube.com/watch?v=TOJ9yjvlapY), [Videos](https://www.youtube.com/watch?v=_8V5o2UHG0E&t=9330s), [Examples](https://observablehq.com/@d3/gallery).
