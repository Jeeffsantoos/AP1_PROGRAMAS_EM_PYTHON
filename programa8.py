lista = []
numero = 0

while numero != -1:
    numero = input('Digite valores inteiros: ')
    
    # Verifica se o usuário digitou um valor vazio e encerra o programa
    if numero == '':
        print('Você digitou um valor vazio e encerrou o programa!')
        break
    
    # Converte o valor para inteiro caso seja um número
    if numero.isdigit() or (numero[0] == '-' and numero[1:].isdigit()): 
        numero = int(numero)
    
    # Verifica se o usuário encerrou o programa
    if numero == -1:
        print('\nVocê encerrou o programa.\n')
        break
    
    # Adiciona o valor à lista caso seja um número inteiro
    elif type(numero) == int: 
        lista.append(numero)
        
    # Caso o usuário tenha digitado um valor textual, encerra o programa
    else:
        print('\nVocê digitou um valor textual e encerrou o programa.\n')
        break

# Mostra a quantidade de valores lidos
print(f'Foram digitados {len(lista)} números.')

# Mostra os valores na ordem em que foram informados
print(f'\nEstes são os valores na ordem em que foram informados:\n')
print(', '.join(str(n) for n in lista))

# Mostra os valores na ordem inversa
lista.reverse()
print(f'\nEstes são os valores na ordem inversa, um embaixo do outro:\n')
for n in lista: 
    print (n)

# Calcula e mostra a soma dos valores
lista_somada = sum(lista)
print(f'\nA soma dos valores da lista é: {lista_somada}')

# Calcula e mostra a média dos valores
media = sum(lista) / len(lista)
print(f'\nA média dos valores informados é: {media:.1f}')

# Calcula e mostra a quantidade de valores acima da média
valores_acima_media = []
for n in lista:
    if n > media:
        valores_acima_media.append(n)
print(f'\nEsta é a quantidade de valores acima da média: {len(valores_acima_media)}')

# Calcula e mostra a quantidade de valores abaixo de sete
abaixo_sete = []
for n in lista:
    if n < 7:
        abaixo_sete.append(n)
print(f'\nEsta é a quantidade de valores abaixo de 7: {len(abaixo_sete)}')

# Encerra o programa
print('\nEncerrando o programa...')