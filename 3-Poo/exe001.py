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
        self.avaliacoes = 0
        self.total_avaliadores = 0

    #FUNÇÃO PARA CALCULAR ASOMATIVA DAS AVALIACÕES E A QUANTIDADETOTAL DE USUÁRIOS QUE VÃO AVALIAR
    def avaliacao_usuario(self, nota):
        if 0 <= nota <= 10:
            self.avaliacoes += nota #somar cada avaliação fornecida
            self.total_avaliadores += 1 #contabilizar cada avaliação bem sucedida para descobrir o número total de usuários que avaliaram
        else:
            # Informa sobre o erro, mas não quebra o programa
            print(f"Erro: A nota {nota} é inválida e não foi registrada. Por favor, use um valor entre 0 e 10.")
        

    #FUNÇÃO PARA CALCULAR A MÉDIA DAS AVALIAÇÕES
    def media_avaliacao(self):
        self.media = self.avaliacoes / self.total_avaliadores
        return self.media

    #FUNÇÃO PARA EXIBIR AS INFORMAÇÕES DO FILME
    def info_tec(self):
        print(f"\n---Informações do Filme---\n")
        print(f"Nome do filme: {self.nome}\nAno de lançamento: {self.anoDeLancamento}\nIncluído no plano: {self.incluidoNoPlano}\nAvaliação: {self.media:.1f} ({self.total_avaliadores} avaliações)\nDuração do filme em Min: {self.duracao}\n\n{"#" * 71}")

#DADOS DO FILME 1
como_treinar_seu_dragao = Filme("Como treinar o seu dragão: Live Action", 2025, True, 185)

#avaliação dos usuários do FILME 1
como_treinar_seu_dragao.avaliacao_usuario(9.1)
como_treinar_seu_dragao.avaliacao_usuario(8.4)

#média da avaliação dos usuários do FILME 1
como_treinar_seu_dragao.media_avaliacao()

#DADOS DO FILME 2
madagascar = Filme("Madagascar", 2005, True, 86)

#avaliação dos usuários do FILME 2
madagascar.avaliacao_usuario(7.5)
madagascar.avaliacao_usuario(9.8)

#média da avaliação dos usuários do FILME 2
madagascar.media_avaliacao()

#Informações dos filmes
como_treinar_seu_dragao.info_tec()
madagascar.info_tec()