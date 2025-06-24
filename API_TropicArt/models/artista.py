class Artista:
    _id = 1
    artistas = []

    def __init__(self, nome, email, telefone, especialidade):
        self.id = Artista._id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.especialidade = especialidade
        Artista._id += 1

    @classmethod
    def adicionar(cls, artista):
        cls.artistas.append(artista)

    @classmethod
    def listar_todos(cls):
        return cls.artistas

    @classmethod
    def buscar_por_id(cls, artista_id):
        for artista in cls.artistas:
            if artista.id == artista_id:
                return artista
        return None

    @classmethod
    def remover(cls, artista):
        cls.artistas.remove(artista)
