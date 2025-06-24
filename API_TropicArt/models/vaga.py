class Vaga:
    _id = 1
    vagas = []

    def __init__(self, titulo, descricao, local, data):
        self.id = Vaga._id
        self.titulo = titulo
        self.descricao = descricao
        self.local = local
        self.data = data
        Vaga._id += 1

    @classmethod
    def adicionar(cls, vaga):
        cls.vagas.append(vaga)

    @classmethod
    def listar_todas(cls):
        return cls.vagas

    @classmethod
    def buscar_por_id(cls, vaga_id):
        for vaga in cls.vagas:
            if vaga.id == vaga_id:
                return vaga
        return None

    @classmethod
    def remover(cls, vaga):
        cls.vagas.remove(vaga)
