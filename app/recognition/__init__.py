import os
import os.path
import logging
from flask import Flask, render_template
from . import recognition

def create_app(test_config=None):    
    app = Flask(__name__, instance_relative_config=True)
    # Configuracion de logs
    handler = logging.StreamHandler() # STDOUT
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(
            app.instance_path,
            "recognition.sqlite"
        )
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def helloworld():
        app.logger.info("Nueva solicitud recibida")
        return render_template("index.html", name="Hello world")
    
    app.register_blueprint(recognition.bp)

    return app
