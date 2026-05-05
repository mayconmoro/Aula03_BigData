# Calcular o desconto na situação em que compras acima de R$ 250,00 recebem desconto de 16%, caso contrario preço será o mesmo.

#ENTRADA:
valor_compra = float(input('Digite o valor da compra: '))

#PROCESSAMENTO:
print()
print('### DETALHAMENTO DA COMPRA ###')
if valor_compra > 250:
    desconto = valor_compra * 0.16
    valor_final = valor_compra - desconto
    print(f'O valor de compra é R$ {valor_compra} \nO valor da compra com desconto de 16% é: R$ {valor_final} ')

else:
    print(f'O valor da compra é de R$ {valor_compra}')

