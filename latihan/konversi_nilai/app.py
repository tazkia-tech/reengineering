from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def konversi():
    angka = None
    if request.method == "POST":
        huruf = request.form["huruf"].upper()
        # LOGIKA BISNIS: mapping nilai huruf → angka
        mapping = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "E": 0.0}
        angka = mapping.get(huruf, "Nilai tidak valid")

    html = """
    <!DOCTYPE html>
    <html>
    <head><title>Konversi Nilai</title></head>
    <body>
        <h2>🔤 Konversi Nilai Huruf ke Angka</h2>
        <form method="POST">
            Nilai Huruf (A-E): <input type="text" name="huruf" maxlength="1" required><br><br>
            <button type="submit">Konversi</button>
        </form>
        {% if angka %}
            <h3>Nilai Angka: {{ angka }}</h3>
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(html, angka=angka)

if __name__ == "__main__":
    app.run(port=5013)