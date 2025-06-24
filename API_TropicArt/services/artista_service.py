from models.artista import Artista

def criar_artista(data):
    try:
        artista = Artista(
            nome=data["nome"],
            email=data["email"],
            telefone=data["telefone"],
            especialidade=data["especialidade"]
        )
        Artista.adicionar(artista)
        return artista
    except KeyError:
        return None

def listar_artistas():
    return Artista.listar_todos()

def buscar_artista_por_id(artista_id):
    return Artista.buscar_por_id(artista_id)

def atualizar_artista(artista, data):
    artista.nome = data.get("nome", artista.nome)
    artista.email = data.get("email", artista.email)
    artista.telefone = data.get("telefone", artista.telefone)
    artista.especialidade = data.get("especialidade", artista.especialidade)
    return artista

def deletar_artista(artista):
    Artista.remover(artista)
