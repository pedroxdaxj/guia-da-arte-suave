from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guia-jiujitsu")
def guia_jiujitsu():
    return render_template("pdf1.html")

@app.route("/download")
def download():
    return render_template("download.html")

if __name__ == "__main__":
    app.run(debug=True)
