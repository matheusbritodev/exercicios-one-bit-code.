'''
Contagem Regressiva
Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.

Tabuada
Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
'''

#Primeiro exercício
import winsound
import time
audio = "python/audio/mixkit-censorship-beep-1082.wav"
for num in range(10, -1, -1):
    print(num)
    try:
        winsound(2500, 500)

    except Exception as e:
        print(f"Erro ao tocar o som: {e}")
        print(f"Verifique se o arquivo '{audio}' existe e está no caminho correto.")
        print("Se estiver no Linux/macOS, pode ser necessário instalar 'mpv' ou 'gstreamer'.")
    time.sleep(1)
    if num == 0:
        print('beep!')
        

#Segundo exercício
num = int(input('Digite um número: '))
print(f'Tabuada do número: {num}')
for i in range(1, 21):
    final = i * num
    print(f'{num} x {i:02} = {final}')