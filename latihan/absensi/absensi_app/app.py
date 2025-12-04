from flask import Flask
from controllers.absensi_controller import absensi

def create_app():
    app = Flask(__name__)
    app.register_blueprint(absensi)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=5012)
