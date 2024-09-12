# Considerações iniciais:

# Limite de saques: 3
# Valor máximo por saque: R$ 500,00

menu = '''

[D] Depositar
        
[S] Sacar
        
[E] Extrato
        
[Q] Sair

'''

LIMITE_SAQUES = 3

VALOR_MAXIMO_POR_SAQUES = 500

saldo = 1500

transacoes = ''

saques_realizados = 0
while True:
    
    opcao = input(menu)
    
    # Encerramento
    if(opcao.lower()) == 'q':
        
        print('Fechando o programa.')
        
        break
    
    # Depositar
    
    elif(opcao.lower()) == 'd':
        
        valor_a_depositar = float(input('Insira o valor do depósito: '))
        
        saldo += valor_a_depositar
        
        transacoes += f'Depósito: R$ {valor_a_depositar:.2f}\n\n'
        
    elif(opcao.lower()) == 's':
        

        if(saques_realizados == LIMITE_SAQUES):
            
            print('Limite de saques diário atingido. Tente novamente amanhã.')
            continue
            
        valor_a_sacar = float(input('Digite o valor do saque: '))
        
        if(valor_a_sacar > VALOR_MAXIMO_POR_SAQUES):
            
            while(valor_a_sacar > VALOR_MAXIMO_POR_SAQUES):
                
                valor_a_sacar = float(input('O valor à ser sacado é maior que o limite. \
                    Digite um valor abaixo de R$500,00 ou insira 0 para cancelar o saque: '))
                
                if valor_a_sacar == 0:
                    break
        
        if(valor_a_sacar == 0):
            
            print('Cancelando saque.')
            continue
        
        if(valor_a_sacar > saldo):
            
            print('Saque cancelado por saldo insuficiente.')
            continue
        
        else:
            
            saldo = saldo - valor_a_sacar
            saques_realizados += 1
            transacoes += f'Saque: R$ {valor_a_sacar:.2f}\n\n'
            print('Saque efetuado com êxito.')
            
    # Extrato
    
    if(opcao.lower() == 'e'):
        
        print(transacoes, f'Saldo: R$ {saldo:.2f}', sep='')
        
    else:
        
        print('Comando inválido. Tente outro novamente')