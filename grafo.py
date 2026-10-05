import csv
import heapq


class Grafo:
    def __init__(self):
        self.adjacencias = {}

    def adicionar_aresta(self, cidade1, cidade2, distancia):
        if cidade1 not in self.adjacencias:
            self.adjacencias[cidade1] = []

        if cidade2 not in self.adjacencias:
            self.adjacencias[cidade2] = []

        self.adjacencias[cidade1].append((cidade2, distancia))
        self.adjacencias[cidade2].append((cidade1, distancia))

    def carregar_csv(self, nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8-sig") as arquivo:
            leitor = csv.reader(arquivo, delimiter=";")

            for linha in leitor:
                if len(linha) >= 3:
                    cidade1 = linha[0].strip()
                    cidade2 = linha[1].strip()

                    try:
                        distancia = float(
                            linha[2].strip().replace(",", ".")
                        )
                    except ValueError:
                        continue

                    self.adicionar_aresta(
                        cidade1,
                        cidade2,
                        distancia
                    )

    def menor_caminho(self, origem, destino):
        distancias = {
            cidade: float("inf")
            for cidade in self.adjacencias
        }

        distancias[origem] = 0

        fila = [(0, origem, [])]

        while fila:
            distancia_atual, cidade_atual, caminho = heapq.heappop(fila)

            if distancia_atual > distancias[cidade_atual]:
                continue

            novo_caminho = caminho + [cidade_atual]

            if cidade_atual == destino:
                return distancia_atual, novo_caminho

            for vizinha, peso in self.adjacencias[cidade_atual]:
                nova_distancia = distancia_atual + peso

                if nova_distancia < distancias[vizinha]:
                    distancias[vizinha] = nova_distancia

                    heapq.heappush(
                        fila,
                        (nova_distancia, vizinha, novo_caminho)
                    )

        return float("inf"), []