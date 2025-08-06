"""
Cadastro de Viagem

Desenvolva um mini cadastro de viagem que tenha os seguintes requisitos:

1 - Usuário deve informar o seu nome para cadastrar uma viagem.

2 - Usuário deve selecionar um destino com base nas instâncias de objetos da classe viagem.

3 - Deve ser apresentado uma mensagem indicando que o a cadastro da viagem no destino específico foi feito com sucesso.
"""

class Viagem:
    def __init__(self):
        self.nome = ""
        self.lugar = None
        

class Destino(Viagem):
    def __init__(self):
        super().__init__()
        self.opcoes = ["Japão", "EUA", "Turquia"]

    def solicitarNome(self):
        self.nome = input(f"Digite seu nome completo:\n>")
        return self.nome

    def escolhaLugar(self):
        print(f"\nEscolha o número correspondente ao seu destino de interesse:")
        for x in enumerate(self.opcoes, start = 1):
            print(x)
        self.lugar = int(input(f"\nQual o seu destino?\n>"))

    def infoViagem(self):
        divisoria = "STATUS DE VIAGEM"
        print(f"\n{divisoria.center(35, "-")}\nViagem agendada com sucesso!\nNome: {self.nome} \nDestino: {self.opcoes[self.lugar - 1]}\n\n{"-" * 35}")

    def executarCadastro(self):
        self.solicitarNome()
        self.escolhaLugar()
        self.infoViagem()


cadastro = Destino()
cadastro.executarCadastro()