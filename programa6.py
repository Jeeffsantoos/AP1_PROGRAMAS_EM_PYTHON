# Recebe o salário e armazena na variável salário
salario = input("Digite seu salário para verificar o seu reajuste: ")
percentual_aumento = ... # Valor será atribuido após a condicional

# Loop para permitir outras tentativas
while True:
    if salario.replace(',', '').isdigit() or salario.replace('.', '').isdigit(): 

        salario_convertido = float(salario.replace(',','.')) 
        break 
    
    else: 
        salario = input('Tente novamente: ')
     
# Verificação de condicionais para atribuição de valores
if salario_convertido <= 280:
    percentual_aumento = 20
    aumento = (salario_convertido * percentual_aumento) / 100
    novo_salario = salario_convertido + aumento

elif salario_convertido > 280 and salario_convertido < 700:
    percentual_aumento = 15
    aumento = (salario_convertido * percentual_aumento) / 100
    novo_salario = salario_convertido + aumento
    
elif salario_convertido >= 700 and salario_convertido < 1500:
    percentual_aumento = 10
    aumento = (salario_convertido * percentual_aumento) / 100
    novo_salario = salario_convertido + aumento
    
elif salario_convertido >= 1500:
    percentual_aumento = 5
    aumento = (salario_convertido * percentual_aumento) / 100
    novo_salario = salario_convertido + aumento
    
# Exibição de Valores
print(f'\nEste era o seu salário antigo: R${salario_convertido:.2f}')
print(f'o percentual de aumento foi de % {percentual_aumento}')
print(f'O aumento foi de R$ {aumento:.2f}')
print(f'\nSeu novo salário: R$ {novo_salario:.2f}')
    
