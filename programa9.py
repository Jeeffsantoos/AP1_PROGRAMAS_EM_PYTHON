# lista de faixas salariais
lista_salarios = [
    [200, 299],
    [300, 399],
    [400, 499],
    [500, 599],
    [600, 699],
    [700, 799],
    [800, 899],
    [900, 999],
    [1000, float('inf')]  # faixa salarial a partir de R$ 1000
]

# contador de vendedores por faixa salarial
contadores = [0] * len(lista_salarios)

while True:
    vendas = input("Digite o valor das vendas da semana (ou 'q' para sair): ")
    if vendas == 'q':
        break
    
    # converte valor das vendas para float
    if ',' in vendas:
        vendas = vendas.replace(',', '.')
    if not vendas.replace('.', '').isdigit():
        print('Valor inválido.')
        continue
    vendas_convertido = float(vendas)

    # calcula o salário do vendedor
    salario = vendas_convertido * 0.09 + 200

    # incrementa o contador de vendedores na faixa salarial correspondente
    for i, faixa in enumerate(lista_salarios):
        if salario >= faixa[0] and salario <= faixa[1]:
            contadores[i] += 1
            break

# exibe os resultados
for i, faixa in enumerate(lista_salarios):
    if faixa[1] == float('inf'):
        print(f'Vendedores com salário a partir de R${faixa[0]}: {contadores[i]}')
    else:
        print(f'Vendedores com salário entre R${faixa[0]} e R${faixa[1]}: {contadores[i]}')
