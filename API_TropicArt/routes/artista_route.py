from flask import Blueprint, jsonify, request
from services import artista_service

artista_bp = Blueprint('artista_bp', __name__)

@artista_bp.route('/artistas', methods=['POST'])
def criar_artista():
    data = request.json
    artista = artista_service.criar_artista(data)
    if artista:
        return jsonify(vars(artista)), 201
    return jsonify({"error_code": "INVALID_DATA", "message": "Dados do artista inválidos ou incompletos."}), 400

@artista_bp.route('/artistas', methods=['GET'])
def listar_artistas():
    artistas = artista_service.listar_artistas()
    return jsonify([vars(a) for a in artistas]), 200

@artista_bp.route('/artistas/<int:artista_id>', methods=['GET'])
def buscar_artista(artista_id):
    artista = artista_service.buscar_artista_por_id(artista_id)
    if artista:
        return jsonify(vars(artista)), 200
    return jsonify({"error_code": "NOT_FOUND", "message": "Artista não encontrado."}), 404

@artista_bp.route('/artistas/<int:artista_id>', methods=['PUT'])
def atualizar_artista(artista_id):
    artista = artista_service.buscar_artista_por_id(artista_id)
    if artista:
        data = request.json
        artista = artista_service.atualizar_artista(artista, data)
        return jsonify(vars(artista)), 200
    return jsonify({"error_code": "NOT_FOUND", "message": "Artista não encontrado."}), 404

@artista_bp.route('/artistas/<int:artista_id>', methods=['DELETE'])
def deletar_artista(artista_id):
    artista = artista_service.buscar_artista_por_id(artista_id)
    if artista:
        artista_service.deletar_artista(artista)
        return '', 204
    return jsonify({"error_code": "NOT_FOUND", "message": "Artista não encontrado para exclusão."}), 404
