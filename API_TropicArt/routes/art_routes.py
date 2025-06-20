from flask import Blueprint, jsonify, request
from services import vaga_service

vaga_bp = Blueprint('vaga_bp', __name__)

@vaga_bp.route('/vagas', methods=['POST'])
def criar_vaga():
    data = request.json
    vaga = vaga_service.criar_vaga(data)
    if vaga:
        return jsonify(vars(vaga)), 201
    return jsonify({"error_code": "INVALID_DATA", "message": "Dados da vaga inválidos ou incompletos."}), 400

@vaga_bp.route('/vagas', methods=['GET'])
def listar_vagas():
    vagas = vaga_service.listar_vagas()
    return jsonify([vars(v) for v in vagas]), 200

@vaga_bp.route('/vagas/<int:vaga_id>', methods=['GET'])
def buscar_vaga(vaga_id):
    vaga = vaga_service.buscar_vaga_por_id(vaga_id)
    if vaga:
        return jsonify(vars(vaga)), 200
    return jsonify({"error_code": "NOT_FOUND", "message": "Vaga não encontrada."}), 404

@vaga_bp.route('/vagas/<int:vaga_id>', methods=['PUT'])
def atualizar_vaga(vaga_id):
    vaga = vaga_service.buscar_vaga_por_id(vaga_id)
    if vaga:
        data = request.json
        vaga = vaga_service.atualizar_vaga(vaga, data)
        return jsonify(vars(vaga)), 200
    return jsonify({"error_code": "NOT_FOUND", "message": "Vaga não encontrada."}), 404

@vaga_bp.route('/vagas/<int:vaga_id>', methods=['DELETE'])
def deletar_vaga(vaga_id):
    vaga = vaga_service.buscar_vaga_por_id(vaga_id)
    if vaga:
        vaga_service.deletar_vaga(vaga)
        return '', 204
    return jsonify({"error_code": "NOT_FOUND", "message": "Vaga não encontrada para exclusão."}), 404