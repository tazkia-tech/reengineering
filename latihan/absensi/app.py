from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def absen():
    persen = None
    if request.method == "POST":
        hadir = int(request.form["hadir"])
        sakit = int(request.form["sakit"])
        total_hari = hadir + sakit
        if total_hari == 0:
            persen = 0
        else:
            # LOGIKA BISNIS: kehadiran = hari hadir / total hari efektif
            persen = (hadir / total_hari) * 100

    html = """
    <!DOCTYPE html>
    <html>
    <head><title>Absensi Siswa</title></head>
    <body>
        <h2>📅 Absensi Siswa</h2>
        <form method="POST">
            Hari Hadir: <input type="number" name="hadir" min="0" required><br><br>
            Hari Sakit: <input type="number" name="sakit" min="0" required><br><br>
            <button type="submit">Hitung Persentase Kehadiran</button>
        </form>
        {% if persen is not none %}
            <h3>Persentase Kehadiran: {{ "%.1f"|format(persen) }}%</h3>
            {% if persen < 75 %}<p style="color:red;">⚠️ Tidak memenuhi syarat minimal 75%</p>{% endif %}
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(html, persen=persen)

if __name__ == "__main__":
    app.run(port=5012)