notas = [] # Cria uma lista vazia
for i in range(4): # Executa o loop 4 vezes
    notas.append(float(input(f"Digite a nota do {i+1}º bimestre: ")))# A cada iteração, o programa recebe um valor do tipo float, e coloca o valor recebido dentro da lista

media = sum(notas) / len(notas) # Sum: soma todos os valores da lista / # Len: Divide pela quantidade de valores na lista.

print("A média das notas bimestrais é", media) # Exibe o resultado
