class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class PessoaJuridica(Pessoa):
    def __init__(self,nome, email, cnpj, razaoSocial):
        self.cnpj = cnpj
        self.razaoSocial = razaoSocial
        super().__init__(nome, email)

    def __repr__(self):
         return 'Nome: {} E-mail:{} CNPJ:{} Razão Social:{} '.format(
            self.nome,
            self.email,
            self.cnpj,
            self.razaoSocial
        )


class PessoaFisica(Pessoa):
    def __init__(self,nome, email, cpf):
        self.cpf = cpf
        super().__init__(nome, email)

    def __repr__(self):
         return 'Nome: {} E-mail:{} CNPJ:{}'.format(
            self.nome,
            self.email,
            self.cpf,
        )

class Autor(Pessoa):
    def __init__(self,nome, email, curriculo):
        self.curriculo = curriculo
        self.artigos = []
        super().__init__(nome, email)

    def __repr__(self):
         return 'Nome: {} Curriculo:{} Artigos:{} E-mail:{}'.format(
            self.nome,
            self.curriculo,
            self.artigos,
            self.email
        )

class Endereco:
    def __init__(self, cidade, uf, rua, lote, cep):
        self.cidade = cidade
        self.uf = uf
        self.rua = rua
        self.lote = lote
        self.cep = cep

class Evento:
    def __init__(self, nome, eventoPrincipal, sigla, dataHoraDeInicio, palavrasChave, logotipo, realizador, endereco):
        self.nome = nome
        self.eventoPrincipal = eventoPrincipal
        self.sigla = sigla
        self.dataHoraDeInicio = dataHoraDeInicio
        self.palavrasChave = palavrasChave
        self.logotipo = logotipo
        self.realizador = realizador
        self.endereco = endereco


class EventoCientifico(Evento):
    def __init__(self, nome, eventoPrincipal, sigla, dataHoraDeInicio, palavrasChave, logotipo, realizador, endereco, issn):
        self.issn = issn
        super().__init__(nome, eventoPrincipal, sigla, dataHoraDeInicio, palavrasChave, logotipo, realizador, endereco)

    def __repr__(self):
        return 'Nome:{} Evento Principal:{} Sigla:{} Data/Hora:{} Palavras Chave:{} Logotipo:{} Pessoa:{} Endereço:{} ISSN:{}'.format(
            self.nome,
            self.eventoPrincipal,
            self.sigla,
            self.dataHoraDeInicio,
            self.palavrasChave,
            self.logotipo,
            self.realizador,
            self.endereco,
            self.issn
        )

class ArtigoCientifico:
    def __init__(self, titulo,  evento):
        self.titulo = titulo
        self.autores = []
        self.evento = evento

    def addAutor(self, Autor):
         self.autores.append(Autor.nome)

    def autores(self):
        for autores in self.autores:
            print(autores)

    def __repr__(self):
        return 'Titulo: {} Autores:{} Evento:{}'.format(
            self.titulo,
            self.autores,
            self.evento,
        )



eventoC = EventoCientifico('nome', 'eventoPrincipal', 'sigla', 'dataHoraDeInicio', 'palavrasChave', 'logotipo', 'realizador', 'endereco', 'issn')
artigo = ArtigoCientifico('TT','evento')
autor = Autor('carol', 'carol@mmgm.com','curicu')
autor2 = Autor('stefani','jskaj','kkskak')
artigo.addAutor(autor)
artigo.addAutor(autor2)
print(artigo)
print(eventoC)