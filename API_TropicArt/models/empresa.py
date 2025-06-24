class Empresa:
    _id = 1
    empresas = []

    def __init__(self, nome, cnpj, email, telefone):
        self.id = Empresa._id
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.telefone = telefone
        Empresa._id += 1

    @classmethod
    def adicionar(cls, empresa):
        cls.empresas.append(empresa)

    @classmethod
    def listar_todas(cls):
        return cls.empresas

    @classmethod
    def buscar_por_id(cls, empresa_id):
        for empresa in cls.empresas:
            if empresa.id == empresa_id:
                return empresa
        return None

    @classmethod
    def remover(cls, empresa):
        cls.empresas.remove(empresa)
