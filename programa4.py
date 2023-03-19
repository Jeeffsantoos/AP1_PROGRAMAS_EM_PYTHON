# Loop para não parar aplicação em caso de "erro"
while True:

    # Solicita valores ao usuário
    ganho_por_hora = input('Quanto você ganha por hora? ')
    horas_por_mes = input('Quantas horas você trabalha por mês? ')

    # Condicional que verifica se o valor digitado foi numérico
    if ganho_por_hora.isdigit() and horas_por_mes.isdigit():
        ganho_convertido = int(ganho_por_hora)
        horas_convertida = int(horas_por_mes)
        break
    
    # Tratamento para caso o valor digitado contenha "." e tratamento de erro
    try:
        ganho_convertido = float(ganho_por_hora.replace(',', '.'))
        horas_convertida = float(horas_por_mes.replace(',', '.'))
        break
    
    except ValueError:
        print("\nEntrada inválida. Por favor, digite um valor numérico.\n")
        continue
        
# Calculos percentuais
salario_bruto = ganho_convertido * horas_convertida
ir = (salario_bruto /100) * 11
inss = (salario_bruto /100) * 8
sindicato = (salario_bruto /100) * 5
   
salario_liquido = salario_bruto - ir - inss - sindicato

# Exibição dos valores
print(f'\nSeu salário bruto é R${salario_bruto:.2f}\n')
print(f'Você pagou R$ {inss:.2f} ao inss')
print(f'Você pagou R$ {sindicato:.2f} ao sindicato')
print(f'Você pagou R$ {ir:.2f} de imposto de renda\n')
print(f'Seu salário liquído será de R${salario_liquido:.2f}')


