''''Escreva um programa com as seguintes especificações:
Uma variável “valor_compras” que receba um valor do tipo float, representando
o valor total das compras.
Uma variável “desconto” que receba um valor do tipo float, representando o
desconto a ser aplicado sobre o valor total das compras.
Uma variável “quantidade_itens”, que represente a quantidade de itens que
foram comprados.
Seu programa deve imprimir dois resultados:
1. O valor final das compras, considerando o desconto aplicado.
2. O custo médio de cada item (considerando o valor final das compras).'''


valor_compras=float(input('Digite o valor total das compras: '))
desconto = float(input('Digite o valor do desconto: '))
quantidade_de_itens = float(input('Digite a qtde de itens que foram comprados: '))

print(f'O valor final será de R${valor_compras-desconto}, já considerando o desconto de R${desconto}')
print(f'O custo médio de cada item foi de R${(valor_compras-desconto)/quantidade_de_itens}')

