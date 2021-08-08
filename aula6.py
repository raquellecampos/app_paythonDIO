conjunto = {1, 2, 3, 4}
conjunto2 = {4, 5, 6}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
conjunto_diferenca = conjunto.difference(conjunto2)
print('Diferença: {}'.format(conjunto_diferenca))

# conjunto = {1, 2, 3, 4, 5}
# print(type(conjunto))
# conjunto.add(6)
# print(conjunto)
# conjunto.discard(3)
# print(conjunto)