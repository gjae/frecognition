import logging
from flask import Flask


app = Flask(__name__)

# Configuracion de logs
handler = logging.StreamHandler() # STDOUT
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
handler.setFormatter(formatter)

app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)


@app.route("/")
def helloworld():
    app.logger.info("Nueva solicitud recibida")
    return "Hello world"


if __name__ == "__main__":
    app.run(debug=True)