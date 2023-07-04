from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    # If there is no if else blocks, there would be a no key error.
    # So, request.args is a dictionary.
    if "name" in request.args:
        name = request.args["name"]
    else:
        name = "world"
    return render_template('index.html')
