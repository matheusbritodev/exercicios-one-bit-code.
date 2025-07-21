"""
Classe Produto e método desconto
Desenvolva uma classe em Python para atender as seguintes especificidades de um Produto:

1 - Cada produto deve ter um preço e um nome.

2 - A classe deve ter um método construtor e o método dundle str.

3 - A classe deve ter um método para desconto. O método deve receber o desconto em percentual e realizar o cálculo de quanto ficaria o preço final com o desconto.
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.new_price = 0

    def __str__(self):
        return f"Produto: {self.name} - "

    #FUNÇÃO PARA CALCULAR O PREÇO FINAL COM O DESCONTO APLICADO
    def product_discount(self, discount):
        self.new_price = self.price * (1 - (discount / 100)) #cálculo básico de porcentagem para retornar o preço final com desconto
        return self.new_price                                #utilizamos o 1 para positivar o resultado e evitar números negativos.
    
    #EXIBIÇÃO DOS DADOS DO PRODUTO
    def product_data(self):
        print(f"\n######## DADOS DO PRODUTO #########\nNome do produto: {self.name}\nPreço: R$ {self.price:.2f}\nPreço com desconto: R$ {self.new_price:.2f}\n{"-" * 35}")

#PRODUTO 1
mouse = Product("Mouse Gamer", 195.90)
mouse.product_discount(10) #DESCONTO APLICADO DE 10%
mouse.product_data() #EXIBIR DADOS DO PRODUTO 1

#PRODUTO 2
headset = Product("Headset Havit", 239.99)
headset.product_discount(25) #DESCONTO APLICADO DE 25%
headset.product_data() #EXIBIR DADOS DO PRODUTO 2
