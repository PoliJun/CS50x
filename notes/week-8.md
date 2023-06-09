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
-   `src` an external js file
    ```html
    <script src="hello.js"></script>
    ```
-   keyup key word
-   document, selector, event listener, parameters(event, function)
    ```js
    document.querySelector('#hello').addEventListener("click", function(){
        ...
    });
    ```
-   navigator, geolocation
    ```js
    navigator.geolocation.getCurrentPosition(function (position) {
        document.write(
            position.coords.latitude + "," + position.coords.longitude
        );
    });
    ```

# Section 8

## HTTP

-   concept of HTTP
    > Hypertext Transfer Protocol
-   code
    > 404, 500

## HTML

-   concept of HTML
    > Hypertext Mark Language
-   structure of the document.
    > forked from <html>, there are <head> and <body> elements
-   style tag
-   table tag
    ```html
    <table>
        <tr>
            <td></td>
            <td></td>
        </tr>
    </table>
    ```

## CSS

-   concept of CSS
    > Cascading Style Sheet  
    > _Cascading_ means inheritance
-   syntax
    ```css
    selector {
        property: value;
    }
    ```
-   id selector
    > `#idName`
-   class selector
    > `.className`
-   color system
    -   hash code
    -   rgb
    -   ...
-   link external css file
    ```html
    <link rel="stylesheet" href="style.css" />
    ```

## JavaScript

-   document.
-   console in browser if things not going right

# Shorts

## Internet Primer

-   IP Address
    -   Uniquely identify itself on Internet
    -   The addressing scheme used by computers is known as IP addressing.
    -   As originally developed, the IP addressing scheme is a unique 32-bit address.
    -   Instead of representing these 32-bit addresses as hexadecimal, w represent them as four clusters of 8 bits using decimal notation.
    -   0-255
    -   IPv6: 128-bits, 16bits \* 8 = 128bits.
-   DHCP
    -   concept of DHCP
        > _Dynamic Host Configuration Protocol_
        > DHCP server. You --> DHCP server --> Internet
-   DNS
    -   Translate Host to IP Address
    -   Distribute
-   Access Points
    -   Router's job. Multiple devices use a same IP address. Connect to the Internet through the router.
    -   The Router have public IP address
-   Protocols
    -   Interact with each other.

## IP

-   IP
    -   concept of IP
        > _Internet Protocol_
    -   Information transfered from A to B
    -   We don't want to physically wire them all together, so this is where routers come back into play.
    -   A router generally knows which IP connected.
    -   The data isn't being sent as one huge block. Data is broken down into pieces.
    -   IP is also known as a connectionless protocol. There is not necessarily a defined path from the sender to the receiver, and vice versa.
    -   Drop packages.

## TCP

-   concept of TCP
    > Transmission Control Protocal
-   TCP/IP, these two protocal are so interrelated, but they are two separate protocals.
-   Garantee dilivery
-   port number, means a special service on the machine
-   indicate how many splits the data is and order them, so they can recunstructed
    -   FTP port 21
    -   SMTP port 25
    -   DNS port 53
    -   HTTP port 80
    -   HTTPS port 443

## HTTP

-   the concepte of HTTP
    > Hypertext Transfer Protocal
-   HTTP is an application layer protocal.
-   specifically dictates the format by which clients **request** web pages from a server, and the format via which servers **return** information to clients.
-   Other application layer protocols
    -   FTP: File Transfer Protocol
    -   SMTP: File Transfer Protocol
    -   DDS: Data Distribution Service
    -   RDP: Remote Desktop Protocol
    -   XMPP: Extensible Message and Presence Protocal
    -   ...
-   You --> HTTP styled format --> cat.com
-   A line of the form
    > `method request-target http-version`  
    > `GET request-target HTTP/1.1`  
    > `POST request-target HTTP/1.1`
-   `GET` and `POST` method

    > GET and POST are two commonly used methods in the HTTP (Hypertext Transfer Protocol) protocol for sending data between a client (e.g., web browser) and a server (e.g., website). Here's a brief explanation of each:
    >
    > GET:
    >
    > -   GET is a method used to retrieve data from a server.
    > -   When making a GET request, the client appends the data to the URL in the form of query parameters.
    > -   GET requests are typically used for fetching data, such as retrieving a webpage or an image.
    > -   Some key characteristics of GET requests include:
    >     -   They are idempotent, meaning that multiple identical requests will have the same result.
    >     -   They can be cached by the client or intermediary servers (e.g., proxy servers).
    >     -   They can be bookmarked or shared as the data is part of the URL.
    >
    > POST:
    >
    > -   POST is a method used to send data to a server to create or update a resource.
    > -   When making a POST request, the data is sent in the body of the request, rather than as part of the URL.
    > -   POST requests are typically used for submitting forms, uploading files, or making changes to a server-side resource.
    > -   Some key characteristics of POST requests include:
    >     -   They are not idempotent, meaning multiple identical requests can have different results.
    >     -   They are not cached by default, but can be cached if specifically allowed by the server.
    >     -   They are not bookmarkable or shareable as the data is not part of the URL.
    >
    > In summary, GET is used for retrieving data, while POST is used for sending data to create or update resources.

-   HTTP status code
    > Sure! Here is a list of some common HTTP status codes:
    >
    > 1xx Informational:
    >
    > -   100 - Continue
    > -   101 - Switching Protocols
    > -   102 - Processing
    >
    > 2xx Success:
    >
    > -   200 - OK
    > -   201 - Created
    > -   202 - Accepted
    > -   204 - No Content
    >
    > 3xx Redirection:
    >
    > -   300 - Multiple Choices
    > -   301 - Moved Permanently
    > -   302 - Found
    > -   304 - Not Modified
    > -   307 - Temporary Redirect
    > -   308 - Permanent Redirect
    >
    > 4xx Client Error:
    >
    > -   400 - Bad Request
    > -   401 - Unauthorized
    > -   403 - Forbidden
    > -   404 - Not Found
    > -   405 - Method Not Allowed
    > -   409 - Conflict
    > -   429 - Too Many Requests
    >
    > 5xx Server Error:
    >
    > -   500 - Internal Server Error
    > -   502 - Bad Gateway
    > -   503 - Service Unavailable
    > -   504 - Gateway Timeout
    >
    > These are just a few examples, and there are many more HTTP status codes. Each status code provides information about the result of the HTTP request, allowing the client or server to understand the outcome of the communication.

## HTML

-   `<head>`
-   `<title>`
-   opening tags and closing tags
-   common HTML tags
    -   `<b>` `</b>`: bold
    -   `<i>` `</i>`: italic
    -   `<u>` `</u>`: underlined
    -   `<p>` `</p>`: paragraph
    -   `<hX>` `</hX>`: headers 1 to 6 smaller
    -   `<ul>` `</ul>`: unordered list
    -   `<ol>` `</ol>`: ordered list
    -   `<li>` `</li>`: items in ordered or unordered list
    -   `<form>` `</form>`:
    -   `<div>` `</div>`
    -   `<input name=X type=Y />`: this is called self closing tag.
    -   `<a href=X>`, `</a>`: anchor tag
    -   `<img src=X ... />`
    -   `<!--,-->` : comment tag
-   HTML will not necessarily fail with syntax errors. it's up to you to be vigilant.

## CSS

-   the concept of CSS
    > Cascading Style Sheet
-   syntax
    ```css
    selector {
        property: value;
    }
    ```
-   selectors
    > Certainly! Here are some of the most commonly used selectors in CSS:
    >
    > 1. Element Selector: Selects elements based on their HTML tag name.
    >    Example: `p { color: blue; }` selects all `<p>` elements.
    >
    > 2. Class Selector: Selects elements based on their assigned class attribute.
    >    Example: `.my-class { font-weight: bold; }` selects elements with `class="my-class"`.
    >
    > 3. ID Selector: Selects a single element based on its unique ID attribute.
    >    Example: `#my-id { background-color: yellow; }` selects the element with `id="my-id"`.
    >
    > 4. Attribute Selector: Selects elements based on their attribute values.
    >    Example: `input[type="text"] { border: 1px solid gray; }` selects `<input>` elements with `type="text"`.
    >
    > 5. Descendant Selector: Selects elements that are descendants of a specific parent element.
    >    Example: `div p { color: red; }` selects all `<p>` elements that are descendants of `<div>`.
    >
    > 6. Child Selector: Selects elements that are direct children of a specific parent element.
    >    Example: `ul > li { list-style-type: square; }` selects `<li>` elements that are direct children of `<ul>`.
    >
    > 7. Pseudo-Class Selector: Selects elements based on a state or condition.
    >    Example: `a:hover { text-decoration: underline; }` selects `<a>` elements when hovered over.
    >
    > 8. Pseudo-Element Selector: Selects and styles a specific part of an element.
    >    Example: `p::first-line { color: red; }` selects and styles the first line of `<p>` elements.
    >
    > 9. Universal Selector: Selects all elements on a web page.
    >    Example: `* { margin: 0; padding: 0; }` selects and applies styles to all elements.
    >
    > These are just a few examples of CSS selectors, and there are many more available. CSS selectors allow you to target specific elements or groups of elements for applying styles and defining the appearance of your web page.
-   common css properties
    -   border: style color width
    -   background-color: [keyword | #<6-digit hex>]
    -   color: [keyword | #<6-digit hex>]
    -   font-size: [absolute size | relative size]
        > can use (small, medium, large), fixed points(10pt, 20pt), percentage(80%), or base off the most recent font size(smaller, larger)
    -   font-family: [font name | generic name]
    -   text-align: [left | right | center | justify]
-   style tags
-   link tags

## JavaScript

-   `<script>` tag
-   Variables
    -   no type specifer.
    -   when a local variable is first declared, preface with the `var` keyword.
-   Conditionals
    -   `if`
    -   `else if`
    -   `else`
    -   `switch`
-   Loops

    -   `for`
    -   `while`
    -   `do-while`

-   Functions
    -   `function` key word
    -   functions can be anonymous.
-   Object
    > object-oriented
    > analogous to struct in C
    > have properties but also methods.
    > object.method() is object-oriented, but function(object) is not.
-   Loops(redux)
    ```js
    for (var key in object) {
        // use object[key] in here
        // or key in here
    }
    ```
-   Functions(redux)
    ```js
    var nums = [1, 2, 3, 4, 5];
    nums = nums.map(function (num) {
        return num * 2;
    });
    ```
-   Events
    -   An _event_ in HTML and JavaScript is a response to user interaction with the web page.
        > click on a button, a page has finished loading, hover over a portion, typed in an input field, etc.
    -   JavaScript has support for _event handlers_, which are callback functions that respond to HTML events.
        > Many HTML elements have support for events as an attribute.

## DOM

-   the concept of DOM
    > Document Object Model
-   document object controls whole page programtically
-   DOM porperties

    > Sure! Here are simple descriptions for each of the DOM properties you mentioned:
    >
    > -   `innerHTML`: Represents the HTML content of an element. It can be used to retrieve or modify the HTML markup inside the element.
    >
    > -   `nodeName`: Gets the name of the node, which is essentially the tag name of an element. For example, if the element is a paragraph `<p>`, the `nodeName` would be `"P"`.
    >
    > -   `id`: Represents the unique identifier of an element. It can be used to access and manipulate specific elements on the page.
    >
    > -   `parentNode`: Gets the parent node of an element. It allows you to traverse up the DOM tree to access and manipulate the parent element of a given element.
    >
    > -   `childNodes`: Represents a collection of child nodes (including elements, text nodes, and comment nodes) of an element. It allows you to access and iterate over the child nodes of an element.
    >
    > -   `attributes`: Represents a collection of attributes of an element. It allows you to access and manipulate the attributes (such as `class`, `src`, `href`, etc.) of an element.
    >
    > -   `style`: Represents the inline CSS styles of an element. It allows you to access and modify the CSS properties of an element, such as setting the background color, width, height, etc.
    >
    > These descriptions should give you a basic understanding of what each property does. Let me know if you have any further questions!

-   DOM methods
    > Certainly! Here are short descriptions for each of the DOM methods you mentioned:
    >
    > -   `getElementById(id)`: Retrieves the first element in the document with the specified `id` attribute. It allows you to access and manipulate a specific element using its unique identifier.
    >
    > -   `getElementsByTagName(tag)`: Retrieves a collection of elements in the document with the specified tag name. It allows you to access and manipulate multiple elements that share the same tag name.
    >
    > -   `appendChild(node)`: Appends a node as the last child of a specified parent node. It allows you to add a new element or node to an existing element, effectively inserting it as the last child.
    >
    > -   `removeChild(node)`: Removes a specified child node from its parent node. It allows you to remove an existing element or node from the DOM structure, effectively deleting it from the document.
    >
    > These descriptions should give you a basic understanding of what each method does. Let me know if you have any further questions!
-   jQuery, an open source library
    -   first example:
        ```js
        $("#colorDiv").css("background-color", "green");
        ```
    -   second example:
        ```js
        $(document).ready(function () {
            $(".jQButton").click(function () {
                $("#colorDiv").css(
                    "background-color",
                    this.innerHTML.toLowerCase()
                );
            });
        });
        ```
