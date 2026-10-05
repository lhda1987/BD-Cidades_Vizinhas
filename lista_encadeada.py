class No:
    def __init__(self, nome, idade, telefone, cidade):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir(self, nome, idade, telefone, cidade):
        novo_no = No(nome, idade, telefone, cidade)

        if self.inicio is None:
            self.inicio = novo_no
        else:
            atual = self.inicio

            while atual.proximo is not None:
                atual = atual.proximo

            atual.proximo = novo_no

    def buscar(self, nome):
        atual = self.inicio

        while atual is not None:
            if atual.nome == nome:
                return atual

            atual = atual.proximo

        return None

    def quantidade(self):
        contador = 0
        atual = self.inicio

        while atual is not None:
            contador += 1
            atual = atual.proximo

        return contador