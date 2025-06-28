'''
Contagem Regressiva
Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.

Tabuada
Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
'''

#Primeiro exercício
import winsound
import time
for num in range(10, -1, -1):
    print(num)
    winsound(2500, 500)
    time.sleep(1)
    if num == 0:
        print('beep!')
        

#Segundo exercício
num = int(input('Digite um número: '))
print(f'Tabuada do número: {num}')
for i in range(1, 21):
    final = i * num
    print(f'{num} x {i:02} = {final}')