from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def belanja():
    total = None
    if request.method == "POST":
        harga = float(request.form["harga"])
        jumlah = int(request.form["jumlah"])
        # LOGIKA BISNIS: diskon 10% jika belanja > 3 item
        diskon = 0.1 if jumlah > 3 else 0
        total = harga * jumlah * (1 - diskon)

    html = """
    <!DOCTYPE html>
    <html>
    <head><title>Toko Mini</title></head>
    <body>
        <h2>🛒 Toko Mini - Hitung Total Belanja</h2>
        <form method="POST">
            Harga per Item: <input type="number" name="harga" step="0.01" required><br><br>
            Jumlah: <input type="number" name="jumlah" min="1" required><br><br>
            <button type="submit">Hitung Total</button>
        </form>
        {% if total %}
            <h3>Total yang Harus Dibayar: Rp {{ "%.2f"|format(total) }}</h3>
            {% if total < 100000 %}<p><em>Belanja lebih dari 3 item dapat diskon 10%!</em></p>{% endif %}
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(html, total=total)

if __name__ == "__main__":
    app.run(port=5011)