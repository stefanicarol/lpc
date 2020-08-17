class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __repr__(self):
        return 'Nome: {} E-mail: {}'.format(
            self.nome,
            self.email
        )

class PessoaJuridica(Pessoa):
    def __init__(self, nome, email, cnpj, razaoSocial):
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
    def __init__(self, nome, email, cpf):
        self.cpf = cpf
        super().__init__(nome, email)

    def __repr__(self):
         return 'Nome: {} E-mail:{} CNPJ:{}'.format(
            self.nome,
            self.email,
            self.cpf
        )

class Autor(Pessoa):
    def __init__(self, nome, email, curriculo):
        self.curriculo = curriculo
        self.artigos = []
        super().__init__(nome, email)

    def imprime(self):
        print('Artigos: ')
        for item in self.artigos:
            print('  ', item)

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

    def __repr__(self):
        return 'Cidade: {} UF: {} Rua: {} Lote: {} CEP: {}'.format(
            self.cidade,
            self.uf,
            self.rua,
            self.lote,
            self.cep
        )

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

    def __repr__(self):
        return 'Nome: {} Evento Principal: {} Sigla: {} Data/Hora de inicio: {} Palavras Chave: {} Logotipo: {} Realizador: {} Endereço: {}'.format(
            self.nome,
            self.eventoPrincipal,
            self.sigla,
            self.dataHoraDeInicio,
            self.palavrasChave,
            self.logotipo,
            self.realizador,
            self.endereco
        )

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
         Autor.artigos.append(self.titulo)

    def imprime(self):
        print('Autores: ')
        for item in self.autores:
            print('  ', item)

    def __repr__(self):
        return 'Titulo: {} Autores:{} Evento:{}'.format(
            self.titulo,
            self.autores,
            self.evento
        )



