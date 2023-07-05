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
-   AJAX
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
- placeholder `(?)`, a list placeholder.