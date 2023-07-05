# Lecture 9 Flask

## Flask

-   app.py
-   requirements.txt
-   static/
-   templates/
    -   **_Jinja_**: double curly braces `{{name}}`
    -   not only Jinja, but also whole html: jango-html
    -   extends the main layout, just modify the smaller fragments.
-   POST and GET
    -   POST is send info to the server, just like adding goods to your shopping cart.
    -   GET is get info from the server
    -   `request.args` is only used for `GET`
    -   use `request.form` for `POST`
-   Jinja allows you to loop `<li>` , dictionary:
    > `{% for name in registrants %}{% endfor %}`
-   **It is capable to attack the remote server through local browser, if server not veryfied the message that the client's browser send!**

## input types

-   text
-   radio
-   hidden
    > Borowsers can send information to server. So, it is not save even the type is _hidden_. We should authoritize special actions on server side.

## `Cookie: session=value`: How Google knows you are logged in. 

-   A new tag
    -   HTTP/1.1 200 OK
    -   Content-Type: text/html
    -   Set-Cookie: session=value
        > This is the new tag.
- This is what sent:
    > GET / HTTP/1.1 
    > HOST: gmail.com
    > Cookie: session=value
- session is a dictionary
- session's life cycle is configurable
## API 
- concept of API
    > Application Programming Interface
- Usage:
    - How you use a function
    - How you use a service, Data, Date
- AJAX
    - concept of AJAX
        > Asynchronous, JavaScript and XML
    - It is a tech whereby you don't have to submit forms anymore.
    - Asynchronous: 
        > Understand this way, waiting for some time to execute, so execute background
- JSON
    - concept of JSON
        > JavaScript Object Notation
    - curly braces means an object.
    - square braces means a list.
    - there are `property: value` pairs in an object.