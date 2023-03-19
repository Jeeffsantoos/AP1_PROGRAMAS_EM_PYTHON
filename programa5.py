# solicita as notas parciais do aluno
nota_1 = input('Digite a primeira nota parcial do aluno: ')
nota_2 = input('Digite a segunda nota parcial do  aluno: ')

# loop para validar se as notas são numéricas
while True:
    if nota_1.replace('.', '').isdigit() and nota_2.replace('.', '').isdigit(): 

        nota1_convertida = float(nota_1) # converte a primeira nota em float
        nota2_convertida = float(nota_2) # converte a primeira nota em float
        media = (nota1_convertida + nota2_convertida) / 2 # calcula a média
        break # converte a primeira nota em float
    
     # caso as notas não sejam numéricas
    else: 
        print('Digite um valor válido.') 
        nota_1 = input('Digite a primeira nota parcial do aluno: ')
        nota_2 = input('Digite a segunda nota parcial do  aluno: ')
        
# condições para verificar se o aluno foi aprovado, reprovado ou aprovado com distinção       

if  media > 10: # mensagem de erro caso a média seja maior que 10
    print('Verifique os valores e tente novamente')
elif media >= 7 and media < 10:
    print('Aprovado')
elif media == 10:
    print('Aprovado com Distinção')
else:
    print('Reprovado')