from models.empresa import Empresa

def criar_empresa(data):
    try:
        empresa = Empresa(
            nome=data["nome"],
            cnpj=data["cnpj"],
            email=data["email"],
            telefone=data["telefone"]
        )
        Empresa.adicionar(empresa)
        return empresa
    except KeyError:
        return None

def listar_empresas():
    return Empresa.listar_todas()

def buscar_empresa_por_id(empresa_id):
    return Empresa.buscar_por_id(empresa_id)

def atualizar_empresa(empresa, data):
    empresa.nome = data.get("nome", empresa.nome)
    empresa.cnpj = data.get("cnpj", empresa.cnpj)
    empresa.email = data.get("email", empresa.email)
    empresa.telefone = data.get("telefone", empresa.telefone)
    return empresa

def deletar_empresa(empresa):
    Empresa.remover(empresa)
