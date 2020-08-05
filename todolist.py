class TodoList:
    itens = []

    def __init__(self, titulo):
        self.titulo = titulo,

    def imprimir(self):
        print(self.titulo)

    def addItem(self):
        nome = input("Nome da Tarefa: ")
        self.itens.append(Item(nome))
        print(Item(nome).nome)

    def executarTarefa(self):
        nome = input("Nome da Tarefa a ser executada: ")
        for tarefas in self.itens:
            if Item(nome).nome:
                tarefas.executar(nome)


    def tarefasStatus(self):
        for tarefa in self.itens:
            if tarefa.status == True:
                print('Tarefas Executadas: ', tarefa.retornarItem())
            else:
                print('Tarefas Pendentes: ', tarefa.retornarItem())

    def __repr__(self):
        return 'Titulo: {} '.format(
            self.titulo
        )


class Item:
    def __init__(self, nome, status = False):
        self.nome = nome,
        self.status = status

    def retornarItem(self):
        return self.nome, self.status

    def executar(self, n):
        if self.nome.__contains__(n):
            self.status = True


