from flask import*
app = Flask(__name__)

@app.route("/")
def signin():
    return render_template("sign in.html")

@app.route("/main")
def main():
    return render_template("main.html", name=request.args.get("name", "world"))


@app.route("/splendor")
def splendor():
    return render_template("splendor.html")

@app.route("/azul")
def azul():
    return render_template("azul.html")

@app.route("/sagrada")
def sagrada():
    return render_template("sagrada.html")


@app.route("/dixit")
def dixit():
    return render_template("dixit.html")

@app.route("/chinatown")
def chinatown():
    return render_template("chinatown.html")

@app.route("/cashandguns")
def cashandguns():
    return render_template("cashandguns.html")


@app.route("/quadropolis")
def quadropolis():
    return render_template("quadropolis.html")

@app.route("/tzaar")
def tzaar():
    return render_template("tzaar.html")

@app.route("/raiders")
def raiders():
    return render_template("raiders.html")


@app.route("/pandemic")
def pandemic():
    return render_template("pandemic.html")