from flask import Flask, render_template_string

app = Flask(__name__)

# Data hardcoded di dalam file utama
students_data = [
    {"id": 1, "name": "Andi", "major": "TKJ"},
    {"id": 2, "name": "Budi", "major": "RPL"},
    {"id": 3, "name": "Citra", "major": "MM"}
]

# HTML langsung di dalam kode Python (anti-pattern)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Daftar Siswa - Versi Lama</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f9f9f9; }
        h1 { color: #333; }
        ul { list-style: none; padding: 0; }
        li { background: white; margin: 8px 0; padding: 12px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .id { color: #888; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>Daftar Siswa (Versi Lama - Sebelum Reengineering)</h1>
    <ul>
    {% for s in students %}
        <li>
            <div class="id">ID: {{ s.id }}</div>
            <strong>{{ s.name.upper() }}</strong> — Program: {{ s.major }}
        </li>
    {% endfor %}
    </ul>
    <p><em>Catatan: Nama di-uppercase dan label "Program" digunakan (tidak konsisten).</em></p>
</body>
</html>
"""

@app.route("/")
def index():
    # Semua dalam satu fungsi: data + logika + tampilan
    return render_template_string(HTML_TEMPLATE, students=students_data)

if __name__ == "__main__":
    app.run(port=5001, debug=True)