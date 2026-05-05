idade = int(input('Digite a sua idade: ')) # 19
 #>, <, >=, <=, != (diferente) ou == (igual)

if idade >= 18:
    print('Você é adulto')
else:
    print('Você é menor de idade')


# Classificação por Pontos se a pontuação for acima de 100 ganha 10 maior que 50 ganha 5 menor que 50 ganha 0
    
pontos = int(input('Informe os pontos: '))

if pontos >= 100:
    total = pontos + 10
    print(f'Excelente! Agora você têm {total} pontos')

elif pontos >= 50:
    total = pontos + 5
    print(f'Bom desempenho! Você tem {total} pontos')

elif pontos >= 30:
    total = pontos + 2
    print(f'Dá para o gasto! Você tem {total} pontos')

else:
    print(f'Treine mais. Pontuação {pontos}')

print()
print('Fim!')


