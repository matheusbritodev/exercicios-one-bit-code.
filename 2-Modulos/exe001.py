'''Módulo de strings
Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:

Inverter uma string de trás pra frente.
Retornar apenas letras com índice par.
Retornar apenas letras com índice ímpar.'''

#Inverter Strings.
import modulo001
string = 'Matheus'
print(f'String invertida:\n>', modulo001.inverter(string))

#Retornar apenas letras com índice par.
print(f'Retornar apenas letras com índice par:\n>', modulo001.letrasIndicePar(string))

#Retornar apenas letras com índice impar.
print(f'Retornar apenas letras com índice impar:\n>', modulo001.letrasIndiceImpar(string))