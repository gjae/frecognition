import os
import os.path
from uuid import uuid4
from flask import Blueprint, request, send_from_directory, current_app, redirect, url_for, flash


bp = Blueprint(
    "recognition",
    __name__,
    url_prefix="/images"
)

@bp.route("/upload", methods=("POST", ))
def hello_images():
    if request.method.lower() == "post":
        if not os.path.exists("./photos"):
            os.mkdir("./photos")
        if not os.path.exists("./known_pictures"):
            os.mkdir("./known_pictures")

        f = request.files["foto"]
        file_name = request.form.get("file_name", "MAXIMO DECIMO MERIDIO")
        if file_name != "":
            f.save(f"./known_pictures/{file_name}.png")
        else:
            f.save(f"./photos/{str(uuid4())}.png")

    return {"error": False, "message": "Imagen cargada"}

@bp.route("/upload/manual/", methods=("POST", ))
def manual_upload_image():
    if request.method.lower() != "post":
        return redirect(url_for("helloworld"))
    
    if not os.path.exists("./photos"):
        os.mkdir("./photos")
    if not os.path.exists("./known_pictures"):
        os.mkdir("./known_pictures")

    f = request.files["foto"]
    file_name = request.form.get("file_name", "MAXIMO DECIMO MERIDIO")
    if file_name != "":
        f.save(f"./known_pictures/{file_name}.png")
    else:
        f.save(f"./photos/{str(uuid4())}.png")

    flash(
        "La imagen ha sido correctamente cargada",
        "success"
    )
    return redirect(url_for("helloworld"))




@bp.route("/photos/<filename>")
def sarve_photo(filename):
    return send_from_directory("."+current_app.config["UPLOAD_FOLDER"], filename)