class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class PessoaJuridica(Pessoa):
    def __init__(self,nome, email, cnpj, razaoSocial):
        self.cnpf = cnpj
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
    def __init__(self,nome, email, curriculo, artigos):
        self.curriculo = curriculo
        self.artigos = artigos
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
        self.cidade = cidade,
        self.uf = uf,
        self.rua = rua,
        self.lote = lote,
        self.cep = cep,

class Evento:
    def __init__(self, nome, eventoPrincipal, sigla, dataHoraDeInicio, palavrasChave, logotipo, realizador, endereco):
        self.titulo = nome,
        self.eventoPrincipal = eventoPrincipal,
        self.sigla = sigla,
        self.dataHoraDeInicio = dataHoraDeInicio,
        self.palavrasChave = palavrasChave,
        self.logotipo = logotipo,
        self.realizador = realizador,
        self.endereco = endereco


class EventoCientifico(Evento):
    def __init__(self, nome, eventoPrincipal, sigla, dataHoraDeInicio, palavrasChave, logotipo, realizador, Endereco, titulo, autores, evento):
        self.titulo = titulo,
        self.autores = autores,
        self.evento = evento
        super().__init__(nome, eventoPrincipal, sigla, dataHoraDeInicio, palavrasChave, logotipo, realizador, Endereco)


class ArtigoCientifico:
    def __init__(self, titulo, autores, evento):
        self.titulo = titulo,
        self.autores = autores,
        self.evento = evento,
