'''
Agendamento de desligamento
Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.

/s: para desligar (shutdown).

/r: para reiniciar (restart).

/t [segundos]: para definir um tempo de espera em segundos antes da ação.

/a: para abortar um desligamento agendado.
'''
import modulo002

while True:
    opcao = input("\n\nEscolha a opção que você deseja executar no seu PC:\n\n1 - Agendar desligamento do PC\n2 - Agendar reinício do PC\n3 - Cancelar agendamento\n4 - Desligar PC instantaneamente\n5 - Reiniciar PC instantaneamente\n6 - Sair\n>")

    if opcao == "1":
        #Agendar desligamento do PC.
        minutos_str = int(input("Digite em quantos minutos o computador deve ser desligado:\n>"))
        tempo_convertido = minutos_str * 60
        modulo002.Desligar(tempo_convertido)
        print(f"\nSeu PC está agendado para desligar em {minutos_str} minutos!\n")

    elif opcao == "2":
        #Agendar reinício do PC.
        minutos_str = int(input("Digite em quantos minutos o computador deve ser reiniciado:\n"))
        tempo_convertido = minutos_str * 60
        modulo002.Reiniciar(tempo_convertido)
        print(f"\nSeu PC está agendado para reiniciar em {minutos_str} minutos!\n")


    elif opcao == "3":
        #Cancelar qualquer agendamento existente.
        modulo002.Cancelar()
        print("\nO agendamento foi cancelado!")

    elif opcao == "4":
        #Desligar instantaneamente
        modulo002.DesligarAgora()
        print("\nPC desligando...")

    elif opcao == "5":
        #Reiniciar instantaneamente
        modulo002.ReiniciarAgora()
        print("\nPC reiniciando...")

    elif opcao == "6":
        escolha = input("Tem certeza que deseja sair?\n\n1 - Sim\n2 - Não\n>")
        if escolha == "1":
            print("Obrigado por utilizar o nosso programa. Até a próxima!")
            break
        else:
            pass
    else:
        print("\nOpção inválida! Você precisa escolhar um número para selecionar a opção desejada!\n(ex: 3)\n")