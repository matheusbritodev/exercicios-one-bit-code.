'''
Substituindo caractere repetido

Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '#', exceto o próprio primeiro caractere

Ex:
fifa 23 → fi#a 23

restart→ resta#t

Substituindo caractere repetido

Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.

Ex:
abc xyz → xyc abz
'''
#Primeiro exercício
name = 'Fifa 23'
character = name[0].lower()
new = name.replace(character, '#')
print(character.capitalize() + new[1:])

#Segundo exercício
lista = 'abc xyz'
print(lista[:2] + lista[6:] + lista[3:6] + lista[2:3])
