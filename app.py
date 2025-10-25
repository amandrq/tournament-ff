from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

CSV_FILE = "data_pendaftar.csv"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Ambil data dari form
    id_ff = request.form["id_ff"]
    username = request.form["username"]
    nama_squad = request.form["nama_squad"]
    nomor_wa = request.form["nomor_wa"]
    anggota1 = request.form["anggota1"]
    anggota2 = request.form["anggota2"]
    anggota3 = request.form["anggota3"]
    anggota4 = request.form["anggota4"]

    # Cek apakah file CSV sudah ada
    file_exists = os.path.isfile(CSV_FILE)

    # Simpan data ke file CSV
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Jika file baru, tulis header kolom
        if not file_exists:
            writer.writerow([
                "ID FF", "Username", "Nama Squad", "Nomor WA",
                "Anggota 1", "Anggota 2", "Anggota 3", "Anggota 4"
            ])
        # Tulis data peserta baru
        writer.writerow([
            id_ff, username, nama_squad, nomor_wa,
            anggota1, anggota2, anggota3, anggota4
        ])

    # Redirect ke YouTube (ganti link-nya dengan milikmu)
    return redirect("https://youtube.com/@byamanrse?si=3XZMoPCVXsZCFWjQ")

if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
