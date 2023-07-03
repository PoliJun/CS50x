# Lecture 8

## TCP/IP

Router A to B

-   protocol
-   IP address
-   port

## DNS

**Domain Name System**

-   convert domain name to ip address

## HTTP/HTTPS

**Hypertext Transfer Protocal**

-   http is application level protocol, companies use, developer use, customers use
-   `https://www.google.com/` the `/` after the domain means the root of the server, implicity added, this is the default page or folder of the server.
-   URL
    -   Can be a path

## Top Domain Names

-   com
-   org
-   edu
-   gov
-   ...
-   CCTLDs like `.cn` `.uk` `.jp`

## Status Code

-   200 Connection established
-   301 Moved Permanently
-   302 Found
-   304 Not Modified
-   307 Temporary Redirect
-   401 Unauthorized
-   403 Forbidden
-   404 Not Found
-   418 I'm a Teapot
-   500 Internal Server Error
-   503 Service Unavailable

## redirect

## HTML

-   tags and atributes
    -   tags: has start and stops, open and close.
        > `<html>`,`</html>`
    -   attributes: modify the default behavior of a tag.
        > `<html lang="en">`, `lang="en"` is an attribute.
-   element:
    > everything in between a open tag and close tag, is an html element
-   tags have **Hierarchy**
-   data structure
    > ![data-structure-in-memory](https://cs50.harvard.edu/x/2023/notes/8/cs50Week8Slide065.png)
-   the syntax indentions doesn't matter for the machine, just for human to read
-   `<br>` enter key. Not all tags need close tags
-   with `<p></p>` displays similar to `<br>`, but it is more semanticly. Focus on what is, not how you want to display it.
-   `<h1>One</h1>` _h1_ is the biggest, _h6_ is the smallest.
-   list

    ```html
    <ul>
        <li>foo</li>
        <li>bar</li>
        <li>baz</li>
    </ul>
    ```

-   table

    ```html
    <table>
        <tr>
            <td>1</td>
            <td>2</td>
            <td>3</td>
        </tr>
        <tr>
            <td>4</td>
            <td>5</td>
            <td>6</td>
        </tr>
    </table>
    ```

-   image

    ```html
    <img alt="Harvard University" src="harvard.jpg" />
    ```

    > show the alt atribute when the image didn't show.

-   video
    > ```html
    > <video autoplay loop muted width="1280">
    >     <source src="halloween.mp4" type="video/mp4" />
    > </video>
    > ```
-   anchor tag
    > ```html
    > <body>
    >     Visit <a href="https://www.harvard.edu/">https://www.yale.edu/</a>
    > </body>
    > ```
    >
    > **_Move the cursor on the link, you will see the true link to direct if you clik on it. In case of spammer_**
-   meta tag
    > **For compatible view on different devices**
    >
    > ```html
    > <head>
    >     <meta charset="UTF-8" />
    >     <meta
    >         name="viewport"
    >         content="width=device-width, initial-scale=1.0"
    >     />
    >     <title>meta</title>
    > </head>
    > ```
    -   property attribute in meta tag
        > **Tell the browsers what you want to show as default** , used for social media platforms
        > The og tag is a meta tag that is used to define properties of a web page. The og tag is used by social media platforms like Facebook to display information about the web page when it is shared on their platform. The property attribute in the og tag is used to define the property of the web page that you want to set. For example, the og:title property is used to set the title of the web page123.
        >
        > ```html
        > <meta property="og:title" content="CS50" />
        > <meta
        >     property="og:image"
        >     content="Introduction to the intellectual property"
        > />
        > <meta property="og:description" content="CS50 is a collection" />
        > ```
-   key value pairs in addresses
    when do **_submit_**, send the key value pairs(the data in the form) to the server and let it to solve them.

```html
<body>
    <form action="https://www.google.com/search" method="get">
        <input
            autocomplete="off"
            autofocus
            name="q"
            placeholder="Query"
            type="search"
        />
        <input type="submit" value="Google Search" />
    </form>
</body>
```

## CSS

-   properties: key value pairs
-   selectors: type ~, class ~, ID ~, attribute ~
-   style tag, `<style></style>`, and `style` attribute
-   link tag
-   frameworks
-   font-size
-   symbols
    -   `&#169;`: Copyright the **(c)** character
-   there's a concept of cascading
-   `<div></div>`, very common use, just think of different regions
-   header,main,footer. This makes a better design than just using `<div></div>`, which is more semanticly.

    ```html
    <!DOCTYPE html>

    <!-- Uses semantic tags instead of DIVs -->

    <html lang="en">
        <head>
            <title>css</title>
        </head>
        <body style="text-align: center">
            <header style="font-size: large">John Harvard</header>
            <main style="font-size: medium">Welcome to my home page!</main>
            <footer style="font-size: small">
                Copyright &#169; John Harvard
            </footer>
        </body>
    </html>
    ```

-   use `<style></style>` inside of `<head></head>`
-   in CSS,`.centered`: **class selector**
    ```css
    <style>
        .centered
        {
            text-align: center;
        }
        .large
        {
            font-size: large;
        }
        .medium
        {
            font-size: medium;
        }
        .small
        {
            font-size: small;
        }
    </style>
    ```
-   separate file for css
    > use a link tag
    > `<link rel="stylesheet" href="style.css">`
-   frameworks:
    -   bootstrap
-   multiple classes. `<table class="table table-striped">`

## JavaScript

### Lots of events that javascript can listen to

-   blur
-   change
-   click
-   drag
-   focus
-   keyup
-   load
-   mousedown
-   mouseover
-   mouseup
-   submit
-   touchmove
-   unload
-   ...

### Sample Code

```js
function greet() {
    let name = document.querySelector("#name").value;
    alert("hello, ");
}
```

> **`#name`: whose id is _name_**

### in use

-   `onsubmit` attribute.
    > it does not generate the current event. Instead, the submit attribute is used to define a script that will be executed when the submit event occurs.

**JavaScript doesn't care double quotes or single quote, but single quote is more common**

-   use javascript to submit
    ```js
    document.querySelector("form").addEventListener("submit", function () {
        let name = document.querySelector("#name").value;
        alert("hello" + name);
        event.preventDefault();
    });
    ```
    > The `preventDefault()` method is used to stop the default action of an element from happening. For example, it can be used to prevent a submit button from submitting a form or a link from following the URL³.
    >
    > Here's an example of how to use it:
    >
    > ```html
    > <a
    >     href="https://www.google.com"
    >     onclick="event.preventDefault(); alert('You clicked the link')"
    >     >Click me</a
    > >
    > ```
    >
    > In this example, the `preventDefault()` method is used to prevent the link from following the URL and instead show an alert message⁵.
-   prevent the form to submit

    > The `onsubmit` attribute is used to specify which JavaScript code to run when a form is submitted. The >`return false;` statement is used to prevent the form from being submitted¹.

    > Here's an example of how to use it:
    >
    > ```html
    > <form onsubmit="greet(); return false;">
    >     <label for="fname">First name:</label><br />
    >     <input type="text" id="fname" name="fname" /><br />
    >     <label for="lname">Last name:</label><br />
    >     <input type="text" id="lname" name="lname" /><br /><br />
    >     <input type="submit" value="Submit" />
    > </form>
    >
    > <script>
    >     function greet() {
    >         alert("Hello!");
    >     }
    > </script>
    > ```
    >
    > In this example, the `return false;` statement is used to prevent the form from being submitted and instead >show an alert message².

-   **The whole file read from top to bottom, this lead to a problem that when the js code on the top of body,the js code doesn't run because of it doesn't konw the variables below in the html body**
    -   to solve this problem. add a special event listener.
        > ```js
        > document.addEventListener("DOMContentLoaded", function () {
        >     // code to run
        > });
        > ```
- `src` an external js file
    ```html
    <script src="hello.js"></script>
    ```
- keyup key word
- document, selector, event listener, parameters(event, function)
    ```js
    document.querySelector('#hello').addEventListener("click", function(){
        ...
    });
    ```
- navigator, geolocation 
    ```js
    navigator.geolocation.getCurrentPosition(function(position){
        document.write(position.coords.latitude + "," + position.coords.longitude);
    })
    ```