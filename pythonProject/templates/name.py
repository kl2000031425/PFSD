from flask import Flask

app = Flask(name)


@app.route("/")
def hello():
    return "Hello World!"


if name == "":
    app.run()

@app.route('/')
def index():
    return render_template('Home.html')