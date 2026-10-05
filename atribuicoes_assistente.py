from grafo import Grafo


class AtribuicoesAssistente:
    def __init__(self, diretor):
        self.arvore = diretor.arvore

        self.grafo = Grafo()
        self.grafo.carregar_csv("cidades_vizinhas.csv")

        self.cidade_escola = "Guarujá"
        self.cidade_intermediaria = "Indaiatuba"

    def consultar_pessoa(self, nome):
        return self.arvore.buscar(nome)

    def menor_distancia_pessoa(self, nome):
        pessoa = self.arvore.buscar(nome)

        if pessoa is None:
            return None

        distancia, caminho = self.grafo.menor_caminho(
            self.cidade_escola,
            pessoa.cidade
        )

        return pessoa, distancia, caminho

    def menor_distancia_via_indaiatuba(self, nome):
        pessoa = self.arvore.buscar(nome)

        if pessoa is None:
            return None

        distancia1, caminho1 = self.grafo.menor_caminho(
            self.cidade_escola,
            self.cidade_intermediaria
        )

        distancia2, caminho2 = self.grafo.menor_caminho(
            self.cidade_intermediaria,
            pessoa.cidade
        )

        distancia_total = distancia1 + distancia2

        caminho_total = caminho1 + caminho2[1:]

        return pessoa, distancia_total, caminho_total

    def pessoas_da_arvore(self):
        pessoas = []

        def percorrer(no):
            if no is None:
                return

            percorrer(no.esquerda)
            pessoas.append(no)
            percorrer(no.direita)

        percorrer(self.arvore.raiz)

        return pessoas

    def cidade_mais_proxima_com_moradores(self):
        pessoas = self.pessoas_da_arvore()

        if not pessoas:
            return None

        cidades = {}

        for pessoa in pessoas:
            if pessoa.cidade not in cidades:
                cidades[pessoa.cidade] = []

            cidades[pessoa.cidade].append(pessoa)

        melhor_cidade = None
        menor_distancia = float("inf")
        melhor_caminho = []

        for cidade in cidades:
            distancia, caminho = self.grafo.menor_caminho(
                self.cidade_escola,
                cidade
            )

            if distancia < menor_distancia:
                menor_distancia = distancia
                melhor_cidade = cidade
                melhor_caminho = caminho

        if melhor_cidade is None:
            return None

        return (
            melhor_cidade,
            menor_distancia,
            melhor_caminho,
            cidades[melhor_cidade]
        )