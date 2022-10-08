# Version 1

from flask import Flask, render_templaate, request

app = flask(__name__)

@app_route("/")
def index():
    return render_template("index.html")

# Version 2

from flask import Flask, render_templaate, request

app = flask(__name__)

@app_route("/")
def index():
    name = request.argv.get("name")
    return render_template("index.html", name=name)

# Version 3 

from flask import Flask, render_templaate, request

app = flask(__name__)

@app_route("/")
def index():
    return render_template("index.html")

@app.route("/greet")
def greet():
    name = request.args.get("name") 
    return render_template("greet.html", name=name)


# Version 4


from flask import Flask, render_templaate, request

app = flask(__name__)

@app_route("/")
def index():
    return render_template("index.html")

@app.route("/greet" methods=["POST"])
def greet():
    name = request.args.get("name", "world") 
    return render_template("greet.html", name=name)


# Version 5


from flask import Flask, render_templaate, request

app = flask(__name__)

@app_route("/")
def index():
    return render_template("index.html")

@app.route("/greet" methods=["POST"])
def greet():
    name = request.form.get("name", "world") 
    return render_template("greet.html", name=name)