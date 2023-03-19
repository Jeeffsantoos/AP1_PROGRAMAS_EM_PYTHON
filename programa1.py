while True: # Executa o loop infinitamente
    num1 = input("Digite o primeiro número inteiro: ") # Pede para o usuário digitar um número inteiro
    num2 = input("Digite o segundo número inteiro: ") 

    if num1.isdigit() and num2.isdigit(): # Compara os dois valores, caso os dois sejam digitos numéricos, retorna TRUE e a condição é atingida
        num1 = int(num1) # Converte o valor digitado para inteiro
        num2 = int(num2)
        break # Interrompe o loop
    else:
        print("Pelo menos um dos valores digitados não é um número inteiro. Por favor, tente novamente.") # Caso a condição acima não seja satisfeita, reinicia o programa

soma = num1 + num2 # soma as duas variaveis e armazena na variavel soma

print("A soma de", num1, "e", num2, "é igual a", soma) # Exibe o resultado