from atribuicoes_secretario import AtribuicoesSecretario
from atribuicoes_diretor import AtribuicoesDiretor
from atribuicoes_assistente import AtribuicoesAssistente

def exibir_pessoa(pessoa):
    print(f"Nome: {pessoa.nome}")
    print(f"Idade: {pessoa.idade}")
    print(f"Telefone: {pessoa.telefone}")
    print(f"Cidade: {pessoa.cidade}")


# ---------------- SECRETÁRIO ----------------

secretario = AtribuicoesSecretario()

print("\nBem-vindo(a), Secretário(a)!")

while True:
    print("\nEscolha uma operação:")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Exibir quantidade de pessoas cadastradas")
    print("4 - Finalizar operações")

    opcao = input("\nOpção: ")

    if opcao == "1":
        print("\n--- Cadastro de pessoa ---")

        nome = input("Nome: ")
        idade = input("Idade: ")
        telefone = input("Telefone: ")

        pessoa = secretario.cadastrar_pessoa(nome, idade, telefone)

        print("\nPessoa cadastrada com sucesso!")
        exibir_pessoa(pessoa)

    elif opcao == "2":
        nome = input("\nDigite o nome da pessoa: ")
        pessoa = secretario.consultar_pessoa(nome)

        if pessoa is None:
            print("\nPessoa não encontrada.")
        else:
            print("\nPessoa encontrada:")
            exibir_pessoa(pessoa)

    elif opcao == "3":
        print(
            f"\nQuantidade de pessoas cadastradas: "
            f"{secretario.quantidade_pessoas()}"
        )

    elif opcao == "4":
        break

    else:
        print("\nOpção inválida. Digite uma opção entre 1 e 4.")


# ---------------- DIRETOR ----------------

diretor = AtribuicoesDiretor(secretario)

print("\nBem-vindo(a), Diretor(a)!")

while True:
    print("\nEscolha uma operação:")
    print("1 - Editar informações de uma pessoa")
    print("2 - Descadastrar pessoa")
    print("3 - Exibir primeira pessoa em ordem alfabética")
    print("4 - Exibir última pessoa em ordem alfabética")
    print("5 - Finalizar operações")

    opcao = input("\nOpção: ")

    if opcao == "1":
        nome = input("\nNome da pessoa que deseja editar: ")
        pessoa = diretor.consultar_pessoa(nome)

        if pessoa is None:
            print("\nPessoa não encontrada.")
            continue

        print("\nPessoa encontrada:")
        exibir_pessoa(pessoa)

        print("\nO que deseja alterar?")
        print("1 - Nome")
        print("2 - Idade")
        print("3 - Telefone")

        alteracao = input("\nOpção: ")

        if alteracao == "1":
            novo_nome = input("Novo nome: ")
            diretor.alterar_nome(nome, novo_nome)
            print("\nNome alterado com sucesso.")

        elif alteracao == "2":
            nova_idade = input("Nova idade: ")
            diretor.alterar_idade(nome, nova_idade)
            print("\nIdade alterada com sucesso.")

        elif alteracao == "3":
            novo_telefone = input("Novo telefone: ")
            diretor.alterar_telefone(nome, novo_telefone)
            print("\nTelefone alterado com sucesso.")

        else:
            print("\nOpção de alteração inválida.")

    elif opcao == "2":
        nome = input("\nNome da pessoa que deseja descadastrar: ")
        pessoa = diretor.consultar_pessoa(nome)

        if pessoa is None:
            print("\nPessoa não encontrada.")
            continue

        print("\nPessoa encontrada:")
        exibir_pessoa(pessoa)

        confirmacao = input(
            "\nDeseja realmente descadastrar esta pessoa? (S/N): "
        ).upper()

        if confirmacao == "S":
            diretor.descadastrar_pessoa(nome)
            print("\nPessoa descadastrada com sucesso.")

        elif confirmacao == "N":
            print("\nDescadastramento cancelado.")

        else:
            print("\nOpção inválida.")

    elif opcao == "3":
        pessoa = diretor.primeira_pessoa()

        if pessoa is None:
            print("\nNão há pessoas cadastradas.")
        else:
            print("\nPrimeira pessoa em ordem alfabética:")
            exibir_pessoa(pessoa)

    elif opcao == "4":
        pessoa = diretor.ultima_pessoa()

        if pessoa is None:
            print("\nNão há pessoas cadastradas.")
        else:
            print("\nÚltima pessoa em ordem alfabética:")
            exibir_pessoa(pessoa)

    elif opcao == "5":
        print("\nOperações do(a) diretor(a) finalizadas.")
        break

    else:
        print("\nOpção inválida. Digite uma opção entre 1 e 5.")
        
        
# ---------------- ASSISTENTE ----------------

assistente = AtribuicoesAssistente(diretor)

print("\nBem-vindo(a), Assistente!")

while True:
    print("\nEscolha uma operação:")
    print("1 - Menor distância até a cidade de uma pessoa")
    print("2 - Menor distância passando por Indaiatuba")
    print("3 - Cidade mais próxima com moradores cadastrados")
    print("4 - Finalizar programa")

    opcao = input("\nOpção: ")

    if opcao == "1":
        nome = input("\nNome da pessoa: ")

        resultado = assistente.menor_distancia_pessoa(nome)

        if resultado is None:
            print("\nPessoa não encontrada.")
        else:
            pessoa, distancia, caminho = resultado

            print("\nPessoa encontrada:")
            exibir_pessoa(pessoa)

            print("\nMenor caminho:")
            print(" -> ".join(caminho))
            print(f"Distância total: {distancia} km")

    elif opcao == "2":
        nome = input("\nNome da pessoa: ")

        resultado = assistente.menor_distancia_via_indaiatuba(nome)

        if resultado is None:
            print("\nPessoa não encontrada.")
        else:
            pessoa, distancia, caminho = resultado

            print("\nPessoa encontrada:")
            exibir_pessoa(pessoa)

            print("\nMenor caminho passando por Indaiatuba:")
            print(" -> ".join(caminho))
            print(f"Distância total: {distancia} km")

    elif opcao == "3":
        resultado = assistente.cidade_mais_proxima_com_moradores()

        if resultado is None:
            print("\nNão há pessoas cadastradas.")
        else:
            cidade, distancia, caminho, moradores = resultado

            print(f"\nCidade mais próxima: {cidade}")
            print(f"Distância: {distancia} km")
            print("Caminho:")
            print(" -> ".join(caminho))

            print("\nMoradores cadastrados:")

            for pessoa in moradores:
                print()
                exibir_pessoa(pessoa)

    elif opcao == "4":
        print("\nPrograma finalizado.")
        break

    else:
        print("\nOpção inválida. Digite uma opção entre 1 e 4.")