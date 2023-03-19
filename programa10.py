relatorio = [] # cria uma lista para armazenar os valores de prestação pagos

# função que calcula o valor da prestação com juros
def valorPagamento (valor_prestacao_convertido, dias_atraso_convertido):
    if dias_atraso_convertido == 0:
        nova_prestacao = valor_prestacao_convertido
        return nova_prestacao
    if dias_atraso_convertido > 0:
        nova_prestacao = valor_prestacao_convertido + (valor_prestacao_convertido * 0.03) + ( dias_atraso_convertido * (valor_prestacao_convertido * 0.001))
        return nova_prestacao

# loop principal do programa    
while True:
    
    # solicita informações ao usuário
    valor_prestacao = input('Digite o valor da prestação: ')
    
    # encerra o programa se o valor digitado for 0
    if valor_prestacao == '0':
        break
    
    dias_atraso = input('Digite quantos dias estão em atraso: ')
    
    
    # verifica se o valor digitado para dias em atraso é válido (é um número positivo)
    if dias_atraso.isdigit():
        dias_atraso_convertido = int(dias_atraso)
    else: 
        print('Valor inválido')
        continue
    
    # verifica se o valor digitado para dias em atraso é válido (é um número positivo)
    if int(dias_atraso) < 0:
        print('Valor inválido.')
        continue

    # converte a vírgula para ponto, se houver
    if ',' in valor_prestacao:
        valor_prestacao = valor_prestacao.replace(',', '.')
            
    # verifica se o valor digitado para a prestação é válido (é um número positivo)
    if not valor_prestacao.replace('.', '').isdigit():
        print('Valor inválido.')
        continue
    
    # verifica se o valor digitado para a prestação é válido (é um número positivo)
    if int(valor_prestacao) < 0:
        print('Valor inválido.')
        continue
    
    valor_prestacao_convertido = float(valor_prestacao)  # converte o valor da prestação para float
    
    nova_prestacao = valorPagamento(valor_prestacao_convertido, dias_atraso_convertido)  # calcula o valor da nova prestação com juros
    
    relatorio.append(nova_prestacao) # adiciona o valor da nova prestação à lista de relatório
    
    print(f'\nValor pago: R$ {nova_prestacao}\n') # exibe o valor da nova prestação na tela

# exibe o relatório do dia com o número de operações e valor total arrecadado
print(f'\nRelatório do dia.\n')
print(f'Número de operaçãoes efetuadas: {len(relatorio)}')
print(f'Valor total arrecadado: R$ {sum(relatorio):.2f}\n')

# exibe uma mensagem de agradecimento ao usuário
print('Muito obrigado por utilizar este programa!!!')

    
    
    