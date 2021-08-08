a = int(input('Entre com um valor:'))
b = int(input('entre com outro valor'))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma)) #mostra o tipo da variavel
soma = str(soma) #converte int em string
print(type(soma))
print('soma: ' + str(soma))
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)
print('Soma: {soma}. \nSubtracao: {subtracao}'
      .format(soma=soma, subtracao=subtracao))
# x = '1'
# soma2 = int(x) + 1
# print(soma2)