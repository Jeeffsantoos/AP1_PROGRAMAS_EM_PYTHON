print('Digite seu gênero:') # Solicita que o usuário digite seu gênero

# Apresenta as opções de gênero disponíveis
print('F para Feminino')
print('M para Masculino\n')

sexo = str(input('Digite M ou F: '))# Lê a entrada do usuário para selecionar o gênero

altura_cm = float(input('Digite sua altura em centímetros: ')) # Lê a entrada do usuário para informar a altura em centímetros

altura_m = altura_cm / 100 # Calcula a altura em metros

# Verifica o gênero informado e calcula o peso ideal
if sexo.lower() == 'm': 
    peso_ideal = (72.7 * altura_m) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura_m) - 44.7
else:
    print('Sexo inválido.')

print(f'Seu peso ideal é {round(peso_ideal, 2)} kg.')# Imprime o resultado do cálculo do peso ideal
