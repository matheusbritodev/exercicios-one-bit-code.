'''
Cálculo da Distância
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,35 para viagens mais longas.

Aumento salário funcionário
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
'''
#Primeiro exercício
distancia = int(input('Quantos KM você vai percorrer na sua viagem? '))
if distancia <= 200:
    distancia *= 0.50
else:
    distancia*= 0.35
print('Preço da passagem: R${:.2f}'.format(distancia).replace('.', ','))

#Segundo exercício
salario = float(input('Qual o salário do funcionario? '))
if salario <= 1250:
    salario = salario * 0.15 + salario #Cálculo de porcentagem: {(10 e 15) / 100 * salario + salario}.
else:
    salario = salario * 0.10 + salario #Não há necessidade de parênteses por conta da hierarquia dos sinais aritiméticos.
print('Parabéns, vocẽ ganhou um aumento!\nSeu novo salário é: R${:,.2f}'.format(salario).replace(',', '.')) #A vírgula nessa expressão executa a separaão por milhar: "{:,.2f}"