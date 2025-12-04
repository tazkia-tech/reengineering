from flask import Flask, render_template, request
from services.denda_service import hitung_denda

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def denda():
    total = None
    if request.method == "POST":
        hari = int(request.form["hari"])
        total = hitung_denda(hari)

    return render_template("index.html", total=total)

if __name__ == "__main__":
    app.run(port=5014, debug=True)
