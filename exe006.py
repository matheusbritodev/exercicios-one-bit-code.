'''
Conta letras maiúsculas e minúsculas
Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.

Lista números pares e ímpares de uma lista
Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.
'''

#Primeiro exercício
frase = input('Fale qualquer coisa: ')

def contaPalavras(frase):
    contMai = 0
    contMin = 0
    for i in frase:
        if i.isupper():
            contMai += 1
        elif i.islower():
            contMin += 1  
    titulo1 = 'CONTAGEM DE LETRAS'
    titulo2 = 'CONTAGEM DE MAIÚSCULAS'   
    titulo3 = 'CONTAGEM DE MINÚSCULAS'
    print(f'{titulo1.center(30, '-')}\nEsta frase tem um total de {contMai + contMin} letras.\n{titulo2.center(30, '-')}\nEsta frase tem {contMai} letras maiúsculas.\n{titulo3.center(30, '-')}\nESta frase tem {contMin} letras minúsculas')

contaPalavras(frase)