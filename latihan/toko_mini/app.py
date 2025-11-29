from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def belanja():
    total = None
    
    if request.method == "POST":
        try:
            # Mengambil input dari form
            harga = float(request.form["harga"])
            jumlah = int(request.form["jumlah"])
            
            # LOGIKA BISNIS: diskon 10% jika belanja > 3 item
            diskon = 0.1 if jumlah > 3 else 0
            
            # Hitung total
            total = harga * jumlah * (1 - diskon)
            
        except ValueError:
            # Mencegah error jika input kosong/salah
            total = None

    # Render file HTML yang ada di folder 'templates'
    return render_template('belanja.html', total=total)

if __name__ == "__main__":
    app.run(port=5011, debug=True)