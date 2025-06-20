from flask import Flask
from routes.vaga_routes import vaga_bp

app = Flask(__name__)
app.register_blueprint(vaga_bp)

if __name__ == '__main__':
    app.run(debug=True)