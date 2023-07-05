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
-   This is what sent:
    > GET / HTTP/1.1
    > HOST: gmail.com
    > Cookie: session=value
-   session is a dictionary
-   session's life cycle is configurable

## API

-   concept of API
    > Application Programming Interface
-   Usage:
    -   How you use a function
    -   How you use a service, Data, Date
-   Ajax
    -   concept of AJAX
        > Asynchronous, JavaScript and XML
    -   It is a tech whereby you don't have to submit forms anymore.
    -   Asynchronous:
        > Understand this way, waiting for some time to execute, so execute background
-   JSON
    -   concept of JSON
        > JavaScript Object Notation
    -   curly braces means an object.
    -   square braces means a list.
    -   there are `property: value` pairs in an object.

# Section 9

## Flask & Jinja

[THE LIBRARY OF BABEL](https://libraryofbabel.info/)

-   dunder name: `__name__`
    -   this is a special python veriable, refers to the name of this file.
        > ```python
        > app=Flask(__name__)
        > ```
        >
        > the `__name__` means that to build a flask app based on this file
-   route
    -   `"/"`, means the user's request.
        > ```python
        > @app.route("/", methods=["GET"])
        > def index():
        >    return render_template("index.html")
        > ```
        >
        > When user request `/`, execute the function `index()`
-   GET and POST
    > retrieve and send data
-   Jinja
    > double curly braces  
    > `<p>{{string}}</p>`  
    > `return render_template("index.html", string="some string")`
-   `random.seed()`: can return the same sequence whith `seed()`
    -   with this feature, we can get the same content when we repeatedly input a same page number.
        > Sure. The `random.seed()` function in Python is used to initialize the random number generator. The random number generator needs a number to start with (a seed value), to be able to generate a random number. By default the random number generator uses the current system time.
        >
        > ```python
        > import random
        >
        > def main():
        >   # Seed the random number generator with the current time.
        >   random.seed()
        >
        >   # Print out 10 random numbers.
        >   for i in range(10):
        >     print(random.random())
        >
        > if __name__ == "__main__":
        >   main()
        > ```
        >
        > The output of this code will be a sequence of 10 random numbers. However, if you run the code again, you will get a different sequence of random numbers. This is because the random number generator is seeded with the current system time, which is different every time you run the code.
        >
        > You can use the `random.seed()` function to seed the random number generator with a specific value. This will ensure that the same sequence of random numbers is generated every time you run the code. For example, the following code will generate the same sequence of random numbers every time you run it:
        >
        > ```python
        > import random
        >
        > def main():
        >   # Seed the random number generator with the number 42.
        >   random.seed(42)
        >
        >   # Print out 10 random numbers.
        >   for i in range(10):
        >     print(random.random())
        >
        > if __name__ == "__main__":
        >   main()
        > ```
        >
        > The output of this code will always be the same, regardless of when you run it.
        >
        > The `random.seed()` function can be useful for debugging or testing your code. If you want to reproduce the results of your code, you can seed the random number generator with the same value every time you run the code. This will ensure that you are testing the same code with the same random numbers.
        >
        > Here are some additional things to keep in mind about the `random.seed()` function:
        >
        > -   The seed value can be any number, but it is usually a good idea to use a number that is easy to remember.
        > -   The seed value does not have to be a random number. You can seed the random number generator with any number, including a specific number like 42.
        > -   The seed value is not used to generate random numbers directly. The seed value is used to initialize the random number generator, which then generates random numbers.
        >
        > I hope this explanation is helpful. Let me know if you have any other questions.
-   `try` and `except`

    ```py
    page = request.form.get("page")

    try:
        page=int(page)
    except ValueError:
        return render_template("index.html", random_string="please enter a number!")

    if page < 0:
        return render_template("index.html", random_string="Please enter a number larger than zero!")

    ```

## Database

-   `import SQL` and `db.execute("SQL statements")`
-   placeholders. `(?)` vs `?`
    > `(?)` is preferred

# Shorts

## Flask

-   Web frameworks make this process much easier
-   Some of the most popular frameworks: Django, Pyramid and Flask.

-   Decorator

    > In Python, a decorator is a design pattern tool that allows you to modify the functionality of a function by wrapping it in another function. The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it[^1^][2].
    >
    > Decorators provide a simple syntax for calling higher-order functions[^2^][3]. They are used to modify or inject code in functions or classes without changing the source code of the original function or class[^3^][1].
    >
    > I hope this helps. Let me know if you have any other questions.

    > _Here is an example of a decorator in Python that prints the time taken by a function to execute:_
    >
    > ```python
    > import time
    >
    > def timing_decorator(func):
    >     def wrapper(*args, **kwargs):
    >         start_time = time.time()
    >         result = func(*args, **kwargs)
    >         end_time = time.time()
    >         print(f"Elapsed time: {end_time - start_time}")
    >         return result
    >     return wrapper
    >
    > @timing_decorator
    > def my_function():
    >     time.sleep(1)
    >
    > my_function()
    > ```
    >
    > This code defines a decorator called `timing_decorator` that takes a function as an argument and returns a > new function that measures the time taken by the original function to execute. The `@timing_decorator` syntax is used to apply the decorator to the `my_function` function[^1^][4].

    > I hope this helps. Let me know if you have any other questions.

-   Data can be passed in via URLs, akin to using HTTP GET.
    ```py
    @app.route("/show/<number>")
    def show(number):
        return "You passed in {}".format(number)
    ```
-   Data can be passed in via HTML forms
    > as with HTTP POST, but we need to indicate that Flask should respond to HTTP POST requests explicitly.
-   `GET`: show the form; `POST`: trans data via the form
    ```py
    @app.route("/login", methods=["GET", "POST"]))
    def login():
        if request.method == "POST":
            # do one thing
        else:
            # do a different thing
    ```
-   flask useful functions example:
    -   `url_for()`
        > Sure. The `url_for()` function in Flask is used to generate URLs for specific functions in your application. This can be useful for generating links in your templates, or for redirecting users to different parts of your application.
        >
        > The `url_for()` function takes two arguments: the name of the function you want to generate a URL for, and any keyword arguments that you want to pass to the function. For example, the following code would generate a URL for the `index` function, with the `name` keyword argument set to "John Doe":
        >
        > ```python
        > from flask import url_for
        >
        > def index(name):
        >     return "Hello, {}!".format(name)
        >
        > url = url_for("index", name="John Doe")
        > ```
        >
        > The `url_for()` function will return a string that represents the URL for the function. This string can be used in your templates, or it can be passed to the `redirect()` function to redirect users to a different part of your application.
        >
        > Here are some of the benefits of using the `url_for()` function:
        >
        > -   It makes your code more dynamic and flexible.
        > -   It helps to prevent hard-coded URLs in your templates.
        > -   It makes it easier to change the URLs in your application without having to update all of your templates.
        >
        > I hope this helps! Let me know if you have any other questions.
    -   `redirect()`
    -   `session()`
    -   `render_template()`

## Ajax

-   concept of Ajax:
    > formerly Asynchronous JavaScript and XML  
    > for now, we commonly use JSON instead of XML
-   usage:
    > Allows us to refresh fragments of a page rather than a whole page.
-   `XMLHttpRequest`
    > Central to our ability to asynchronously update our pages is to make use of a special Javascript object called an `XMLHttpRequest`.
    ```js
    var xhttp = new XMLHttpRequest();
    ```
- *onreadystatechange*
    > After obtaining your new object, you need to define its onreadystatechange behavior.  
    > This is a function(typically an anonymous function) called when the asynchronous HTTP request has completed, and thus typically defines what is expected to change on your site.
- `XMLHttpRequest`s have two additional properties
    - `readyState`: will change from *1* to *4*
    - `status`: will (hopefully) be `200(OK)`
- `open()` and `send()`  
    > Then just make your asynchronous request using the open() method to define the request and the send() method to actually send it.
    > *There's a slightly different way to do this syntactically with jQuery!*