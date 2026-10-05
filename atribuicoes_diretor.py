from arvore_binaria import criar_arvore_da_lista


class AtribuicoesDiretor:
    def __init__(self, secretario):
        self.arvore = criar_arvore_da_lista(secretario.lista)

    def consultar_pessoa(self, nome):
        return self.arvore.buscar(nome)

    def alterar_nome(self, nome_atual, novo_nome):
        pessoa = self.arvore.buscar(nome_atual)

        if pessoa is None:
            return False

        idade = pessoa.idade
        telefone = pessoa.telefone
        cidade = pessoa.cidade

        self.arvore.remover(nome_atual)
        self.arvore.inserir(novo_nome, idade, telefone, cidade)

        return True

    def alterar_idade(self, nome, nova_idade):
        pessoa = self.arvore.buscar(nome)

        if pessoa is None:
            return False

        pessoa.idade = nova_idade
        return True

    def alterar_telefone(self, nome, novo_telefone):
        pessoa = self.arvore.buscar(nome)

        if pessoa is None:
            return False

        pessoa.telefone = novo_telefone
        return True

    def descadastrar_pessoa(self, nome):
        pessoa = self.arvore.buscar(nome)

        if pessoa is None:
            return False

        self.arvore.remover(nome)
        return True

    def primeira_pessoa(self):
        return self.arvore.primeiro_alfabetico()

    def ultima_pessoa(self):
        return self.arvore.ultimo_alfabetico()