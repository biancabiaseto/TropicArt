from models.vaga import Vaga

def criar_vaga(data):
    try:
        vaga = Vaga(
            titulo=data["titulo"],
            descricao=data["descricao"],
            local=data["local"],
            data=data["data"]
        )
        Vaga.adicionar(vaga)
        return vaga
    except KeyError:
        return None

def listar_vagas():
    return Vaga.listar_todas()

def buscar_vaga_por_id(vaga_id):
    return Vaga.buscar_por_id(vaga_id)

def atualizar_vaga(vaga, data):
    vaga.titulo = data.get("titulo", vaga.titulo)
    vaga.descricao = data.get("descricao", vaga.descricao)
    vaga.local = data.get("local", vaga.local)
    vaga.data = data.get("data", vaga.data)
    return vaga

def deletar_vaga(vaga):
    Vaga.remover(vaga)