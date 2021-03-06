import webbrowser

continuar = True
lista = []
while continuar:
    print('Escolha uma opção:\n'
          '1-Inserir um número na lista.\n'
          '2- Mostra maior e menor número inserido na lista.\n'
          '3-Sair do programa.')
    opcao_str = input()
    try:
        opcao = int(opcao_str)
    except:
        webbrowser.open('https://www.significados.com.br/numeros/')
        print(f'Erro: O valor inserido "{opcao_str}" não é um número! Tente novamente.')
        continue
    if opcao == 1:
        numero_str = input("Insira o número que deseja inserir na lista!")
        try:
            numero = int(numero_str)
            lista.append(numero)
        except:
            print(f"A gente fala número e o cara escreve {numero_str}. Se ajude cara.")
            webbrowser.open('https://www.significados.com.br/numeros/')
        else:
            print(f"Número {numero_str} adicionado com sucesso!")

    elif opcao == 2:
        try:
            print(f"O primeiro elemento da lista é {lista[0]}")
            print(f"O último elemento da lista é {lista[-1]}")
        except:
            print("É necessário no mínímo inserir um elemento na lista.")
    elif opcao == 3:
        print("Programa está encerrando! Salve para os amigos do MEC que estão nos acompanhando.")
        continuar = False
    else:
        print(f'A opção "{opcao_str}" não existe! Tente novamente.')
