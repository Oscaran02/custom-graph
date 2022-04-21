import os
from time import sleep

from flask import render_template, redirect, url_for, Flask, request
from flask_cors import CORS

from models import report

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')
CORS(app)
app.config["DEBUG"] = False
app.config['host'] = '0.0.0.0'
app.config['port'] = 5000
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}

report_data = report()
report_data.set_data()


@app.route("/")
@app.route("/home")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.filename = f.filename.split('.')[1]
        f.filename = "data." + f.filename
        filename = (os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        f.save(filename)
        f.close()
        report_data.set_data()
        # sleep(5)
        return redirect(url_for('dashboard'))


# Tiempos promedio
@app.route("/data2", methods=['GET'])
def data2():
    # sleep(1)
    return report_data.average_times().to_json()
