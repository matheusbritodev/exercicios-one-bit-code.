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

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Nome: {self.name.capitalize()}\nTelefone: {self.phone}\nE-mail: {self.email}"

class ContactBook:
    def __init__(self):
        self.lista = {}

    def addContact(self):
        name = input(f"\nAdicionando novo contato:\n\nNome: ").lower()
        if name in self.lista:
            print(f"\nEste contato já existe na sua agenda!\n")
            return
        phone = input(f"Telefone: ")
        email = input(f"E-mail: ")
        newContact = Contact(name=name, phone=phone, email=email)
        self.lista[name] = newContact
        print(f"\n{name.capitalize()} foi adicionado a sua agenda!\n")

    def listContact(self):
        print("\n--- Lista de Contatos ---")
        if not self.lista:
            print(f"Sua lista está vazia.")
        else:
            for contact_object in self.lista.values():
                print(contact_object)
                print("-------------------------")

    def searchContact(self):
        nameToSearch = input(f"Buscar contato:\n>").lower()
        contact_found = self.lista.get(nameToSearch)
        if contact_found:
            print("\n--- Contato Encontrado ---")
            print(contact_found)
            print("--------------------------\n")
        else:
            print(f"\nContato não encontrado na agenda.\n")

    def removeContact(self):
        nameToRemove = input(f"Qual contato deseja excluir?\n>").lower()
        if nameToRemove in self.lista:
            del self.lista[nameToRemove]
            print(f"{nameToRemove.capitalize()} foi removido da agenda!")
        else:
            print(f"Contato não encontrado na agenda.")
