import os
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    data = [email]
    file_path = os.path.realpath(__file__)
    work_dir = os.path.dirname(file_path)
    file_csv = f"{work_dir}/data.csv"

    with open(file_csv, "a", encoding="utf-8", newline="") as fichier:
            writer = csv.writer(fichier)
            writer.writerow(data)

    return render_template('result.html', email=email)

if __name__ == '__main__':
    app.run(debug=True)