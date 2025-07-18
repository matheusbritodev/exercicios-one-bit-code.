"""Avaliação e Média da Nota de Filmes

Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes. Segue o escopo das funcionalidades:

Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de um filme passando uma nota com parâmetro e que essa nota seja salva no atributo específico da classe.

Assim que uma avaliação for realizada, deve ser incrementado o total de avaliadores daquele filme. Obs: Considere criar um atributo específico para esse fim.

Para cada filme ter uma nota de avaliação média que consiste na divisão do total de avaliação pelo total de avaliadores."""

class Filme:
    def __init__(self, nome, anoDeLancamento, incluidoNoPlano, duracao ):
        self.nome = nome
        self.anoDeLancamento = anoDeLancamento
        self.incluidoNoPlano = incluidoNoPlano
        self.duracao = duracao

    def avaliacaoUsuario(self):
        nota = float(input(f'\nO que achou de assistir "{self.nome}"? Deixe uma avaliação abaixo, onde:\n 0 = "Eu odiei o filme!"\n10 = "Eu amei o filme!"\n\nDe 0 a 10 minha nota para{self.nome} é: \n>'))
        self.nota = nota

    def info_tec(self):
        print(f"\n{"#" * 71}\n\n---Informações do Filme---\n")
        print(f"Nome do filme: {self.nome}\nAno de lançamento: {self.anoDeLancamento}\nIncluído no plano: {self.incluidoNoPlano}\nAvaliação: {self.nota}\nDuração do filme: {self.duracao}\n\n{"#" * 71}")

#FILME 1
como_treinar_seu_dragao = Filme("Como treinar o seu dragão: Live Action", 2025, True, 185)
como_treinar_seu_dragao.avaliacaoUsuario()
como_treinar_seu_dragao.info_tec()

#FILME 2
madagascar = Filme("Madagascar", 2005, True, 86)
madagascar.avaliacaoUsuario()
madagascar.info_tec()