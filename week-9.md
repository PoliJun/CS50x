# Lecture 9 Flask

## Flask
- app.py
- requirements.txt
- static/
- templates/
    - ***Jinja***: double curly braces `{{name}}`
    - not only Jinja, but also whole html: jango-html
    - extends the main layout, just modify the smaller fragments.
- POST and GET
    - POST is send info to the server, just like adding goods to your shopping cart.
    - GET is get info from the server
    - `request.args` is only used for `GET`
    - use `request.form` for `POST`
- Jinja allows you to loop  `<li>` , dictionary:
    > `{% for name in registrants %}{% endfor %}`
- **It is capable to attack the remote server through local browser, if server not veryfied the message that the client's browser send!**

## input types
- text
- radio
- hidden
    > Borowsers can send information to server. So, it is not save even the type is *hidden*. We should authoritize special actions on server side.