from flask import Flask, render_template
from data.students import STUDENTS

app = Flask(__name__)

@app.route("/")
def index():
    # Hanya mengarahkan data ke template — logika minimal
    return render_template("index.html", students=STUDENTS)

if __name__ == "__main__":
   app.run(port=5002, debug=True)