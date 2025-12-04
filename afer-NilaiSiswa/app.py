from flask import Flask, render_template, request
from logika_nilai import hitung_nilai_akhir, tentukan_grade

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
    
        uts = float(request.form["uts"])
        uas = float(request.form["uas"])
        tugas = float(request.form["tugas"])
        nilai_akhir = hitung_nilai_akhir(uts, uas, tugas)
        grade_huruf = tentukan_grade(nilai_akhir)
        result = {"nilai": round(nilai_akhir, 2), "grade": grade_huruf}


    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(port=5010)