numero_convertido = ... # Inicializa a variável `numero_convertido` com um valor vazio.

# Loop `while True` para garantir que o usuário digite um número válido entre 1 e 10.
while True:
    numero = input('Escolha um número inteiro entre 1 e 10 para ver sua tabuada ')
    
    # Verifica se a entrada do usuário é um valor numérico inteiro e está entre 1 e 10.
    if  int(numero) >= 1 and int(numero) <= 10 and numero.isnumeric():
        numero_convertido = int(numero)
        break 
    else:
        # Exibe uma mensagem de erro se o usuário digitar um valor inválido.
        print('Digite um valor numérico inteiro e que esteja entre 1 e 10')
        continue 

# Exibe a tabuada correspondente ao número escolhido pelo usuário.
print(f'\nTabuada de {numero_convertido}\n')

# Loop `for` para exibir a tabuada do número escolhido pelo usuário.
for multiplicador in range(1, 11):
    resultado = numero_convertido * multiplicador
    print(f'{numero_convertido} X {multiplicador} = {resultado}')