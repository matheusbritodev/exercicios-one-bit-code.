"""
Agenda de Contatos
Desenvolva uma agenda de contatos utilizando Programação Orientada a Objetos. O programa deve seguir as especificidades:

1 - Ter uma classe Contact contendo os atributos: name, phone e email

2 - Ter uma classe ContactBook contendo quatro métodos:
a. Um método para adicionar contato.
b. Um método para listar contatos.
c. Um método para buscar contatos.
d. Um método para remover contatos.

3 - Criar um arquivo principal para a aplicação que deve instanciar as duas classes criadas anteriormente e desenvolver e chamar cada um dos métodos desenvolvidos de acordo com a opção escolhida.
"""

from exe004 import ContactBook

schedule = ContactBook()
done = True

while done == True:
    print(f"AGENDA\n1 - Adicionar novo contato\n2 - Remover contato\n3 - Listar todos os contatos\n4 - Buscar contato\n5 - Sair\n")

    try:
        choice = int(input(f"Digite a opção desejada:\n>"))

        if choice > 5 or choice < 0: print(f"\nOpção Inválida\n")
        if choice == 1: schedule.addContact() 
        if choice == 2: schedule.removeContact()
        if choice == 3: schedule.listContact()
        if choice == 4: schedule.searchContact() 
        if choice == 5:
            confirm = input(f"Tem certeza que deseja sair? (s/n)\n>").lower()
            done = False if confirm == "s" else done

    except ValueError:
            print("\n[ERRO] Por favor, digite apenas um número correspondente à opção.")