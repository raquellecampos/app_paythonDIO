lista = [1, 23, 5, 7]  #lista sempre dentro de []
lista_animal = ['cachorro', 'gato', 'elefante']
print(lista)
print(lista_animal[2])

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla)) #quantidade
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
#
# print(sum(lista))   #soma
# print(max(lista))   #maior valor
# print(min(lista))    #menor valor
#
# print(min(lista_animal))   #ordem alfabetica



# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
#
# lista_animal.reverse()
# print(lista_animal)

# if 'lobo' in lista_animal:
#     print('Existe!')
# else:
#     print('Não existe! Más vamos adicionar :)')
#     lista_animal.append('lobo')  #incluir na lista
#     print(lista_animal)

# lista_animal.pop()  #retira o ultimo das pilha, ou passa parâmetro
# print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)