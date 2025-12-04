from flask import Blueprint, render_template, request
from services.absensi_service import hitung_kehadiran

absensi = Blueprint("absensi", __name__)

@absensi.route("/", methods=["GET", "POST"])
def index():
    persen = None
    if request.method == "POST":
        hadir = int(request.form["hadir"])
        sakit = int(request.form["sakit"])
        persen = hitung_kehadiran(hadir, sakit)

    return render_template("absen.html", persen=persen)
