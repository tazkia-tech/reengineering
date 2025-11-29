from flask import Flask, render_template, request

app = Flask(__name__)

# --- Logika Bisnis (Model/Service) ---
def konversi_nilai_ke_angka(huruf):
    """
    Memetakan nilai huruf (A-E) ke nilai angka (IPK).
    """
    mapping = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "E": 0.0}
    
    return mapping.get(huruf.strip().upper()) 

# --- View Function (Controller) ---
@app.route("/", methods=["GET", "POST"])
def konversi():
    nilai_angka = None
    huruf_input = None
    
    if request.method == "POST":
        huruf_input = request.form.get("huruf", "")
        
        nilai_angka = konversi_nilai_ke_angka(huruf_input)
    
    return render_template("konversi.html", 
                           nilai_angka=nilai_angka, 
                           huruf_input=huruf_input)

if __name__ == "__main__":
    app.run(port=5013, debug=True)