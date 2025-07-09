"""
Advinhe o Número

Escreva um programa em Python que gera um número aleatório para que o usuário tente acertar o número. Algumas sugestões para o programa:
Utilizar um laço de repetição para que o programa execute até que o usuário informe um número referente a opção para sair do programa.
Utilizar o módulo random para gerar valores aleatórios dentro de um intervalo. Ex: 1 a 10.
Lê o número que o usuário digitar via input e comparar se é o mesmo número que o programa sorteou.
"""

import random

def gerar_num():
    tentativas = 3
    number = random.randint(1, 10)
    while tentativas > 0:
        num_selecionado = int(input("Digite um número de 1 a 10:\n> "))
        tentativas -= 1
        if num_selecionado == number:
            print(f"Parabéns! Você acertou!\nO número sorteado foi: {number}.")
            break
        elif num_selecionado > number:
            print("Muito alto!")
        elif num_selecionado < number:
            print("Muito baixo!")
        if tentativas == 0:
            print(f"Tentativas esgotadas! O número sorteado foi: {number}\nGAME OVER.")
            break
        elif num_selecionado == number:
            print(f"Parabéns! Você acertou!\nO número sorteado foi: {number}.")
            break
        else:
            pass

while True:
    print(f"\nJogo da Advinhação:\nVocê tem 3 tentativas para advinhar o número sorteado.\n\n1 - Jogar\n2 - Sair")
    choice = input("> ")
    if choice == "1":
        gerar_num()
    elif choice == "2":
        print("Sessão finalizada com sucesso!")
        break
    else:
        print("Opção inválida!\nEscolha entre uma das duas opções. (ex: 1)")

