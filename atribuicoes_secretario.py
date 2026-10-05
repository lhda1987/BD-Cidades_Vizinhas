import csv
import random

from lista_encadeada import ListaEncadeada


class AtribuicoesSecretario:
    def __init__(self):
        self.lista = ListaEncadeada()
        self.cidades = self.carregar_cidades()

    def carregar_cidades(self):
        cidades = []

        with open("cidades_vizinhas.csv", "r", encoding="utf-8-sig") as arquivo:
            leitor = csv.reader(arquivo, delimiter=";")

            for linha in leitor:
                if len(linha) >= 2:
                    cidade1 = linha[0].strip()
                    cidade2 = linha[1].strip()

                    if cidade1 not in cidades:
                        cidades.append(cidade1)

                    if cidade2 not in cidades:
                        cidades.append(cidade2)

        return cidades

    def cadastrar_pessoa(self, nome, idade, telefone):
        cidade = random.choice(self.cidades)
        self.lista.inserir(nome, idade, telefone, cidade)
        return self.lista.buscar(nome)

    def consultar_pessoa(self, nome):
        return self.lista.buscar(nome)

    def quantidade_pessoas(self):
        return self.lista.quantidade()