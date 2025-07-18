"""
Advinhe o Número

Escreva um programa em Python que gera um número aleatório para que o usuário tente acertar o número. Algumas sugestões para o programa:
Utilizar um laço de repetição para que o programa execute até que o usuário informe um número referente a opção para sair do programa.
Utilizar o módulo random para gerar valores aleatórios dentro de um intervalo. Ex: 1 a 10.
Lê o número que o usuário digitar via input e comparar se é o mesmo número que o programa sorteou.
"""

import random

#Função para gerar o número e retornar se chegou próximo ou não de acertar
def gerar_num():
    chance = 3 #O usuário tem 3 tentativas para acertar
    number = random.randint(1, 10)
    while chance > 0:
        user_choice = int(input("Digite um número de 1 a 10:\n> "))
        chance -= 1 #A cada erro diminui uma tentativa
        if user_choice == number:
            print(f"Parabéns! Você acertou!\nO número sorteado foi: {number}.")
            break #Esse break permite que o usuário retorne para o menu inicial e decida se quer jogar novamente ou não
        elif user_choice > number:
            print("Muito alto!")
        elif user_choice < number:
            print("Muito baixo!")
        elif chance == 0:
            print(f"Tentativas esgotadas! O número sorteado foi: {number}\nGAME OVER.")
            break #Esse break permite que o usuário retorne para o menu inicial e decida se quer jogar novamente ou não
        else:
            pass

game_title = "JOGO DA ADVINHAÇÃO"
#Menu do jogo
while True:
    print(f"\n{game_title.center(53, "=")}")
    #Opção de jogar ou asir do jogo
    choice = input("Você tem 3 tentativas para advinhar o número sorteado.\n\n1 - Jogar\n2 - Sair\n> ")
    if choice == "1":
        gerar_num()
    elif choice == "2":
        print("Sessão finalizada com sucesso!")
        break
    else:
        print("Opção inválida!\nEscolha entre uma das duas opções. (ex: 1)")
