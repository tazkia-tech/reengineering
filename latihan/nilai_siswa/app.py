from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        uts = float(request.form["uts"])
        uas = float(request.form["uas"])
        tugas = float(request.form["tugas"])
        # LOGIKA BISNIS: formula nilai akhir (UTS 30%, UAS 50%, Tugas 20%)
        nilai_akhir = 0.3 * uts + 0.5 * uas + 0.2 * tugas
        grade = "A" if nilai_akhir >= 85 else "B" if nilai_akhir >= 75 else "C" if nilai_akhir >= 60 else "D"
        result = {"nilai": round(nilai_akhir, 2), "grade": grade}

    html = """
    <!DOCTYPE html>
    <html>
    <head><title>Hitung Nilai Siswa</title></head>
    <body>
        <h2>🔢 Hitung Nilai Akhir Siswa</h2>
        <form method="POST">
            UTS: <input type="number" name="uts" step="0.1" required><br><br>
            UAS: <input type="number" name="uas" step="0.1" required><br><br>
            Tugas: <input type="number" name="tugas" step="0.1" required><br><br>
            <button type="submit">Hitung</button>
        </form>
        {% if result %}
            <h3>Hasil:</h3>
            <p>Nilai Akhir: {{ result.nilai }}</p>
            <p>Grade: {{ result.grade }}</p>
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(port=5010)