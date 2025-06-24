from flask import Flask
from routes.vaga_route import vaga_bp
from routes.empresa_route import empresa_bp
from routes.artista_route import artista_bp

app = Flask(__name__)
app.register_blueprint(vaga_bp)
app.register_blueprint(empresa_bp)
app.register_blueprint(artista_bp)

if __name__ == '__main__':
    app.run(debug=True)
