from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world"))
    return render_template("index.html")


# @app.route("/index.html")
# def index():
    # If there is no if else blocks, there would be a no key error.
    # So, request.args is a dictionary.
    # if "name" in request.args:
    #     name = request.args["name"]
    # else:
    #     name = "world"

    # or just use
    # This wouldn't throw an error, just return a  none.Default value is "world".
    # name = request.args.get("name", "world")
#     return render_template('index.html')

# @app.route("/greet", methods=["POST"])
# def greet():
#     return render_template('greet.html', name=request.args.get("name", "world"))
