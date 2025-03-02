import os
import os.path
from uuid import uuid4
from flask import Blueprint, request


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
        f = request.files["foto"]
        f.save(f"./photos/{str(uuid4())}.png")

    return {"error": False, "message": "Imagen cargada"}