from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def denda():
    total_denda = None
    if request.method == "POST":
        hari = int(request.form["hari"])
        # LOGIKA BISNIS: denda = hari_keterlambatan × 1000
        if hari < 0:
            total_denda = "Hari tidak boleh negatif"
        else:
            total_denda = hari * 1000

    html = """
    <!DOCTYPE html>
    <html>
    <head><title>Denda Perpustakaan</title></head>
    <body>
        <h2>📚 Hitung Denda Keterlambatan Buku</h2>
        <form method="POST">
            Jumlah Hari Terlambat: <input type="number" name="hari" min="0" required><br><br>
            <button type="submit">Hitung Denda</button>
        </form>
        {% if total_denda %}
            <h3>Denda: 
            {% if total_denda is number %}
                Rp {{ total_denda }}
            {% else %}
                {{ total_denda }}
            {% endif %}
            </h3>
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(html, total_denda=total_denda)

if __name__ == "__main__":
    app.run(port=5014)