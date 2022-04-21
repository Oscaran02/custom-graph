import os

from flask import render_template, redirect, url_for, request, Blueprint, current_app as app

from . import models

api_bp = Blueprint('api', __name__, static_url_path="",
                   static_folder="static",
                   template_folder="templates"
                   )

report_data = models.report()
report_data.set_data()


@api_bp.route("/")
@api_bp.route("/home")
@api_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@api_bp.route('/uploader', methods=['GET', 'POST'])
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
@api_bp.route("/data2", methods=['GET'])
def data2():
    # sleep(1)
    return report_data.average_times().to_json()
