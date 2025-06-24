from flask import Blueprint, jsonify, request
from services import empresa_service

empresa_bp = Blueprint('empresa_bp', __name__)

@empresa_bp.route('/empresas', methods=['POST'])
def criar_empresa():
    data = request.json
    empresa = empresa_service.criar_empresa(data)
    if empresa:
        return jsonify(vars(empresa)), 201
    return jsonify({"error_code": "INVALID_DATA", "message": "Dados da empresa inválidos ou incompletos."}), 400

@empresa_bp.route('/empresas', methods=['GET'])
def listar_empresas():
    empresas = empresa_service.listar_empresas()
    return jsonify([vars(e) for e in empresas]), 200

@empresa_bp.route('/empresas/<int:empresa_id>', methods=['GET'])
def buscar_empresa(empresa_id):
    empresa = empresa_service.buscar_empresa_por_id(empresa_id)
    if empresa:
        return jsonify(vars(empresa)), 200
    return jsonify({"error_code": "NOT_FOUND", "message": "Empresa não encontrada."}), 404

@empresa_bp.route('/empresas/<int:empresa_id>', methods=['PUT'])
def atualizar_empresa(empresa_id):
    empresa = empresa_service.buscar_empresa_por_id(empresa_id)
    if empresa:
        data = request.json
        empresa = empresa_service.atualizar_empresa(empresa, data)
        return jsonify(vars(empresa)), 200
    return jsonify({"error_code": "NOT_FOUND", "message": "Empresa não encontrada."}), 404

@empresa_bp.route('/empresas/<int:empresa_id>', methods=['DELETE'])
def deletar_empresa(empresa_id):
    empresa = empresa_service.buscar_empresa_por_id(empresa_id)
    if empresa:
        empresa_service.deletar_empresa(empresa)
        return '', 204
    return jsonify({"error_code": "NOT_FOUND", "message": "Empresa não encontrada para exclusão."}), 404
