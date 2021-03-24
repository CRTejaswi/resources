    Copyright(c) 2020-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# JS
> Personal notes for JS.

# References (General)

[__Beau Carnes__](https://www.youtube.com/playlist?list=PL9WLlXArXbtcuYmDjagcHEN4pa24BC5iW) <br>
[__Brad Traversy__](https://www.youtube.com/user/TechGuyWeb/videos) <br>

# Index

- [Resources](#resources)
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
- PWA
https://www.youtube.com/playlist?list=PLNYkxOF6rcIB2xHBZ7opgc2Mv009X87Hh
https://www.youtube.com/playlist?list=PLlyCyjh2pUe9RHFCJHU0kxpaivUzADPYk
- [Projects](#projects)

## Resources

| Link | Description |
| :--: | :-- |
| [Projects](#projects) | Useful list of projects |

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

## Array

## Object
 - [Defining Properties & Methods](#Object01)
 - [Generic Properties & Methods](#Object02)

<a id="Object01"></a>

### Defining Properties & Methods
1. __Using Object-Initialization__ \
    Explanation of code-snippet.
``` js
SYNTAX:
    var obj = {
              property(params) {...},
              *generator(params) {...},
        async property(params) {...},
        async *generator(params) {...},

              [property](params) {...},
              *[generator](params) {...},
        async [property](params) {...},

          get property(){...},
          set property(value){...}
    };
```
``` js
var car1 = {
    make: 'Honda',
    model: 'City',
    year: 2008
};
var car2 = {
    make: 'Suzuki',
    model: 'Wagon-R',
    year: 2017
};

console.table([car1, car2]);
```
```
(index)  make    model    year
   0    Honda    City     2008
   1    Suzuki  Wagon-R   2017
```

2. __Using A Constructor-Function__ \
    Explanation of code-snippet.
``` js
function Car(make, model, year){
    this.make = make;
    this.model = model;
    this.year = year;
    this.displayCar = displayCar;
};
function displayCar(){
    var result = `A Beautiful ${this.year} ${this.make} ${this.model}`;
    return result;
}

var car1 = new Car('Honda', 'City', 2008);
var car2 = new Car('Suzuki', 'Wagon-R', 2017);
console.log(car1.displayCar());
console.log(car2.displayCar());
```
```
A Beautiful 2008 Honda City
A Beautiful 2017 Suzuki Wagon-R
```

3. __Using `Object.create` Method__ \
    Explanation of code-snippet.
``` js
var Car = {
    make: '',
    model: '',
    year: undefined
};

var car1 = Object.create(Car);
var car2 = Object.create(Car);

car1.make = 'Honda'; car1.model = 'City'; car1.year = 2008;
car2.make = 'Suzuki'; car2.model = 'Wagon-R'; car2.year = 2017;

console.table([car1, car2]);
```
```
(index)  make    model    year
   0    Honda    City     2008
   1    Suzuki  Wagon-R   2017
```
<a id="Object02"></a>

### Generic Properties & Methods
1. __Using Object-Initialization__ \
    Explanation of code-snippet.
``` js
SYNTAX:
    var obj = {
              property(params) {...},
              *generator(params) {...},
        async property(params) {...},
        async *generator(params) {...},

              [property](params) {...},
              *[generator](params) {...},
        async [property](params) {...},

          get property(){...},
          set property(value){...}
    };
```


### Iterator v Iterable Protocol
- Iterator Protocol
``` js
let obj = {
    array: [1,2,3,4,5],
    nextIndex: 0,
    next: function(){
        return (this.nextIndex < this.array.length)
            ? {value: this.array[this.nextIndex++],
               done: false}
            : {done: true}
    }
};

for (var i=0; i < 5; i++)
    console.log(obj.next().value);
console.log(obj.next().done);
```
- Iterable Protocol
``` js
let obj = {
    array: [1,2,3,4,5],
    nextIndex: 0,
    [Symbol.iterator]: function(){
        return {
            array: this.array,
            nextIndex: this.nextIndex,
            next: function(){
                return (this.nextIndex < this.array.length)
                    ? {value: this.array[this.nextIndex++],
                       done: false}
                    : {done: true}
            }
        }
    }
};

let iterable = obj[Symbol.iterator]()
for (var i=0; i < 5; i++)
    console.log(iterable.next().value);
console.log(iterable.next().done);
```
Outputs of both these code-snippets are:
```
1
2
3
4
5
true
```
- Generator (Iterator + Iterable)

    - Returns the next natural number
``` js
  function* foo(n){
    while (true)
        yield ++n;
}

let generator = foo(0);
for (var i = 0; i < 10; i++)
    console.log(generator.next().value);
```

## Promise
``` js
var car1 = {
    make: 'Honda',
    model: 'City',
    year: 2008
};
var car2 = {
    make: 'Suzuki',
    model: 'Wagon-R',
    year: 2017
};
console.table([car1, car2]);

Promise.resolve(car1)
    .then (function(value){
        console.log(value.make, value.model, value.year);
        console.log(value[0], value[1], value[2]);
        console.log(value['make'], value['model'], value['year']);
    });
Promise.reject(car2)
    .then (null, function(value){
        console.log(value.make, value.model, value.year);
        console.log(value[0], value[1], value[2]);
        console.log(value['make'], value['model'], value['year']);
    });
```
```
(index)  make    model    year
   0    Honda    City     2008
   1    Suzuki  Wagon-R   2017
​
Honda City 2008
undefined undefined undefined
Honda City 2008
Suzuki Wagon-R 2017
undefined undefined undefined
Suzuki Wagon-R 2017
```

## Structured Data (CSV, JSON, XML)

Refer:

__CSV__ <br>

__JSON__ <br>

__XML__ <br>

## Databases

- IndexDB
https://www.youtube.com/watch?v=pcelNF8Ckhk
https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API
https://developers.google.com/web/ilt/pwa/working-with-indexeddb

- SQLite
https://github.com/sql-js/sql.js

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

`<path>` is the most important shape, with a curve sketched by `M-LQCA` ("Move to M(x,y), then move linearly/quadratically/cubically/on an ellipticalArc").
```xml
<path d="M 0,0 L 100,0" fill="none" stroke="#000000"/>
<path d="M 0,0 Q 150,200 100,100 z" fill="none" stroke="#ff0000"/>
<path d="M 0,0 C 150,200 150,150 100,100 z" fill="none" stroke="#00ff00"/>
<path d="M 0,0 A 150,200 0 0,0 100,100 z" fill="none" stroke="#0000ff"/>
```

<img src="resources/svg1.png">


## Data Visualization

Refer: [Basics](https://codepen.io/crtejaswi/pen/wvMQBpO), [Tutorial](https://observablehq.com/collection/@d3/learn-d3), [Video](https://www.youtube.com/watch?v=TOJ9yjvlapY), [Videos](https://www.youtube.com/watch?v=_8V5o2UHG0E&t=9330s), [Examples](https://observablehq.com/@d3/gallery).


- Live Server
With Node, install/use live-server globally using:
```
npm install -g live-server
live-server
```

# Projects
(currently lifted from https://github.com/tuvtran/project-based-learning#javascript)

- [Build 30 things in 30 days with 30 tutorials](https://javascript30.com)
- [Build an App in Pure JS](https://medium.com/codingthesmartway-com-blog/pure-javascript-building-a-real-world-application-from-scratch-5213591cfcd6)
- [Build a Jupyter Notebook Extension](https://link.medium.com/wWUO7TN8SS)
- [Build A Native Desktop App with JS](https://medium.freecodecamp.org/build-native-desktop-apps-with-javascript-a49ede90d8e9)
- Build a Progressive Web Application (PWA)
  - [Part 1](https://bitsofco.de/bitsofcode-pwa-part-1-offline-first-with-service-worker/)
  - [Part 2](https://bitsofco.de/bitsofcode-pwa-part-2-instant-loading-with-indexeddb/)
  - [Part 3](https://bitsofco.de/bitsofcode-pwa-part-3-push-notifications/)
- [How to Build a Web Framework in Less Than 20 Lines of Code](https://www.pubnub.com/blog/build-yourself-a-web-framework-in-less-than-20-lines-of-code/)
- [Build Yourself a Redux](https://zapier.com/engineering/how-to-build-redux/)
- [How to write your own Virtual DOM](https://medium.com/@deathmood/how-to-write-your-own-virtual-dom-ee74acc13060)
- [Build A Realtime Serverless GraphQL API with WebSockets on AWS](https://andrewgriffithsonline.com/blog/serverless-websockets-on-aws/)

__Node__ <br>

- [Build A Simple Website With Node,Express and MongoDB](https://closebrace.com/tutorials/2017-03-02/the-dead-simple-step-by-step-guide-for-front-end-developers-to-getting-up-and-running-with-nodejs-express-and-mongodb)
- [Build a real-time Markdown Editor with NodeJS](https://scotch.io/tutorials/building-a-real-time-markdown-viewer)
- [Test-Driven Development with Node, Postgres and Knex](http://mherman.org/blog/2016/04/28/test-driven-development-with-node/)
- Write a Twitter Bot in Node.js
  - [Part 1](https://codeburst.io/build-a-simple-twitter-bot-with-node-js-in-just-38-lines-of-code-ed92db9eb078)
  - [Part 2](https://codeburst.io/build-a-simple-twitter-bot-with-node-js-part-2-do-more-2ef1e039715d)
- [Create A Simple RESTFUL Web App](https://closebrace.com/tutorials/2017-03-02/creating-a-simple-restful-web-app-with-nodejs-express-and-mongodb)
- [Build A Simple Search Bot in 30 minutes](https://medium.freecodecamp.org/how-to-build-a-simple-search-bot-in-30-minutes-eb56fcedcdb1)
- [Build A Job Scraping Web App](https://medium.freecodecamp.org/how-i-built-a-job-scraping-web-app-using-node-js-and-indreed-7fbba124bbdc)

__React__ <br>

- [Create Serverless React.js Apps](http://serverless-stack.com/)
- [Create a Trello Clone](http://codeloveandboards.com/blog/2016/01/04/trello-tribute-with-phoenix-and-react-pt-1/)
- [Create a Character Voting App with React, Node, MongoDB and SocketIO](https://www.zcfy.cc/original/create-a-character-voting-app-using-react-node-js-mongodb-and-socket-io)
- [React Tutorial: Cloning Yelp](https://www.fullstackreact.com/articles/react-tutorial-cloning-yelp/)
- [Build a Full Stack Movie Voting App with Test-First Development using Mocha, React, Redux and Immutable](https://teropa.info/blog/2015/09/10/full-stack-redux-tutorial.html)
- [Build a Twitter Stream with React and Node](https://scotch.io/tutorials/build-a-real-time-twitter-stream-with-node-and-react-js)
- Build a Serverless MERN Story App with Webtask.io
  - [Part 1](https://scotch.io/tutorials/build-a-serverless-mern-story-app-with-webtask-io-zero-to-deploy-1)
  - [Part 2](https://scotch.io/tutorials/build-a-serverless-mern-story-app-with-webtask-io-zero-to-deploy-2)
- [Build A Simple Medium Clone using React.js and Node.js](https://codeburst.io/build-simple-medium-com-on-node-js-and-react-js-a278c5192f47)
- [Integrate MailChimp in JS](https://medium.freecodecamp.org/how-to-integrate-mailchimp-in-a-javascript-web-app-2a889fb43f6f)
- [Build A Chrome Extension with React + Parcel](https://medium.freecodecamp.org/building-chrome-extensions-in-react-parcel-79d0240dd58f)
- [Build A ToDo App With React Native](https://blog.hasura.io/tutorial-fullstack-react-native-with-graphql-and-authentication-18183d13373a)
- [Make a Chat Application](https://medium.freecodecamp.org/how-to-build-a-chat-application-using-react-redux-redux-saga-and-web-sockets-47423e4bc21a)
- [Create a News App with React Native](https://medium.freecodecamp.org/create-a-news-app-using-react-native-ced249263627)
- [Learn Webpack For React](https://medium.freecodecamp.org/learn-webpack-for-react-a36d4cac5060)
- [Testing React App With Pupepeteer and Jest](https://blog.bitsrc.io/testing-your-react-app-with-puppeteer-and-jest-c72b3dfcde59)
- [Build Your Own React Boilerplate](https://medium.freecodecamp.org/how-to-build-your-own-react-boilerplate-2f8cbbeb9b3f)
- [Code The Game Of Life With React](https://medium.freecodecamp.org/create-gameoflife-with-react-in-one-hour-8e686a410174)
- [A Basic React+Redux Introductory Tutorial](https://hackernoon.com/a-basic-react-redux-introductory-tutorial-adcc681eeb5e)
- [Build an Appointment Scheduler](https://hackernoon.com/build-an-appointment-scheduler-using-react-twilio-and-cosmic-js-95377f6d1040)
- [Build A Chat App with Sentiment Analysis](https://codeburst.io/build-a-chat-app-with-sentiment-analysis-using-next-js-c43ebf3ea643)
- [Build A Full Stack Web Application Setup](https://hackernoon.com/full-stack-web-application-using-react-node-js-express-and-webpack-97dbd5b9d708)
- [Create Todoist clone with React and Firebase](https://www.youtube.com/watch?v=hT3j87FMR6M)
- Build A Random Quote Machine
  - [Part 1](https://www.youtube.com/watch?v=3QngsWA9IEE)
  - [Part 2](https://www.youtube.com/watch?v=XnoTmO06OYo)
  - [Part 3](https://www.youtube.com/watch?v=us51Jne67_I)
  - [Part 4](https://www.youtube.com/watch?v=iZx7hqHb5MU)
  - [Part 5](https://www.youtube.com/watch?v=lpba9vBqXl0)
  - [Part 6](https://www.youtube.com/watch?v=Jvp8j6zrFHE)
  - [Part 7](https://www.youtube.com/watch?v=M_hFfrN8_PQ)
