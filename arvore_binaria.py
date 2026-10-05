class NoArvore:
    def __init__(self, nome, idade, telefone, cidade):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, nome, idade, telefone, cidade):
        novo_no = NoArvore(nome, idade, telefone, cidade)

        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, atual, novo_no):
        if novo_no.nome < atual.nome:
            if atual.esquerda is None:
                atual.esquerda = novo_no
            else:
                self._inserir_recursivo(atual.esquerda, novo_no)

        elif novo_no.nome > atual.nome:
            if atual.direita is None:
                atual.direita = novo_no
            else:
                self._inserir_recursivo(atual.direita, novo_no)

    def buscar(self, nome):
        atual = self.raiz

        while atual is not None:
            if nome == atual.nome:
                return atual

            if nome < atual.nome:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None

    def remover(self, nome):
        self.raiz = self._remover_recursivo(self.raiz, nome)

    def _remover_recursivo(self, no, nome):
        if no is None:
            return None

        if nome < no.nome:
            no.esquerda = self._remover_recursivo(no.esquerda, nome)

        elif nome > no.nome:
            no.direita = self._remover_recursivo(no.direita, nome)

        else:
            if no.esquerda is None:
                return no.direita

            if no.direita is None:
                return no.esquerda

            sucessor = no.direita

            while sucessor.esquerda is not None:
                sucessor = sucessor.esquerda

            no.nome = sucessor.nome
            no.idade = sucessor.idade
            no.telefone = sucessor.telefone
            no.cidade = sucessor.cidade

            no.direita = self._remover_recursivo(
                no.direita,
                sucessor.nome
            )

        return no


    def primeiro_alfabetico(self):
        if self.raiz is None:
            return None

        atual = self.raiz

        while atual.esquerda is not None:
            atual = atual.esquerda

        return atual

    def ultimo_alfabetico(self):
        if self.raiz is None:
            return None

        atual = self.raiz

        while atual.direita is not None:
            atual = atual.direita

        return atual
    
def criar_arvore_da_lista(lista):
    arvore = ArvoreBinariaBusca()

    atual = lista.inicio

    while atual is not None:
        arvore.inserir(
            atual.nome,
            atual.idade,
            atual.telefone,
            atual.cidade
        )

        atual = atual.proximo

    return arvore