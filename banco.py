# Considerações iniciais:

# Limite de saques: 3
# Valor máximo por saque: R$ 500,00

from datetime import datetime
datetime.time

usuarios = list()

contas = list()

# Funções:

def sacar(saldo, valor_a_sacar, saques_realizados, transacoes, LIMITE_SAQUES, VALOR_MAXIMO_POR_SAQUES, cpf, numero_da_conta):
    
    usuario = filtrar_usuario(cpf)
    
    conta = filtrar_conta(cpf, numero_da_conta)
    
    if usuario and conta:
            
        if(saques_realizados == LIMITE_SAQUES):
                
            
            print('Limite de saques diário atingido. Tente novamente amanhã.')
            return saldo, transacoes, saques_realizados
                    
        if(valor_a_sacar > VALOR_MAXIMO_POR_SAQUES):
                
            while(valor_a_sacar > VALOR_MAXIMO_POR_SAQUES):
                    
                valor_a_sacar = float(input('O valor à ser sacado é maior que o limite. \
                    Digite um valor abaixo de R$500,00 ou insira 0 para cancelar o saque: '))
                    
                
                if(valor_a_sacar == 0):
                    
                    print('Cancelando saque.')
                    return saldo, transacoes, saques_realizados
                
        if(valor_a_sacar > saldo):
                
            print('Saque cancelado por saldo insuficiente.')
            return saldo, transacoes, saques_realizados
            
        saldo = saldo - valor_a_sacar
                
        saques_realizados += 1
            
        horario_atual = datetime.now()
        
        horario_atual_formatado = horario_atual.strftime('%d/%m/%y às %H:%M')
            
        transacoes += f'Saque realizado em: {horario_atual_formatado}, de valor: R$ {valor_a_sacar:.2f}\n\n'
                
        print('Saque efetuado com êxito.')
            
        return saldo, transacoes, saques_realizados
    
    else:
        return saldo, transacoes, saques_realizados
    
def depositar(saldo, valor_a_depositar,transacoes, cpf, numero_da_conta):
    
    usuario = filtrar_usuario(cpf)
    
    conta = filtrar_conta(cpf, numero_da_conta)
    
    if usuario and conta:    
        
        saldo += valor_a_depositar
            
        horario_atual = datetime.now()
            
        horario_atual_formatado = horario_atual.strftime('%d/%m/%y às %H:%M')
            
        transacoes += f'Depósito realizado em: {horario_atual_formatado}, de valor R$ {valor_a_depositar:.2f} \
                        por {usuario["nome"]} na conta {conta["numero_da_conta"]}\n\n'
        
        print('Depósito efetuado com êxito.')

    return saldo, transacoes

def criar_usuario():
    
    cpf = int(input('Digite seu CPF (apenas números): '))
    
    if len(usuarios) != 0:
        
        for usuario in usuarios:
            
            if cpf == usuario['cpf']:
                
                print('Já existe um usuário com esse cpf. Cancelando processo.')
                
                return
        
    nome = input('Digite seu nome completo: ')
    
    data_de_nascimento = input('Informe sua data de nascimento (dia/mês/ano): ')
        
    endereco = input('Informe seu endereço: ')
    
    usuario_novo = {'cpf': cpf, 'nome': nome, 'data_de_nascimento': data_de_nascimento, 
                    'endereco':endereco, 'contas':[]}
    
    return usuario_novo

def criar_contas():
    
    if len(usuarios) == 0:
        
        print('Não há usuários para criar contas. Crie um usuário para poder criar contas.')
        return
    
    cpf_inserido = int(input('Digite seu CPF (apenas números): '))
    
    usuario = filtrar_usuario(cpf_inserido)
    
    if usuario:
        
        agencia = input('Digite a agência da sua nova conta: ')
            
        numero_da_conta = len(usuario['contas']) + 1
            
        usuario['contas'].append(numero_da_conta)
            
        nova_conta = {'agencia': agencia, 'numero_da_conta':numero_da_conta, 
                      'usuario': usuario, 'saldo': 0.0, 'transacoes': '', 'saques realizados': 0}
            
        return nova_conta
        

    print('CPF não encontrado. Verifique se o CPF indicado está correto.')
    return
          
def listar_contas():
    
    if len(usuarios) == 0:
        
        print('Sistema sem usuários, logo não há contas registradas.')
        return
    
    cpf_inserido = int(input('Digite seu CPF (apenas números): '))
    
    contas_encontradas = 0
    
    for usuario in usuarios:
        
        if(cpf_inserido == usuario['cpf']):
            
            for conta in contas:
                
                if usuario == conta['usuario']:
                    
                    contas_encontradas =+ 1
                    print(conta)
    
    if(contas_encontradas) == 0:
        
        print('Não há contas registradas para este usuário.')
        return
    
    return
    
    
    return

def filtrar_usuario(cpf):
    
    for usuario in usuarios:
        
        if cpf == usuario['cpf']:
        
            return usuario
    
    print('Usuario não encontrado.')
    return False

def mostrar_extrato(cpf, conta):
    
    usuario = filtrar_usuario(cpf)
    
    conta = filtrar_conta(cpf, conta)
    
    if usuario and conta:
        
        print(conta['transacoes'], f'Saldo: R$ {conta["saldo"]:.2f}', sep='')
        return
    
    return

def filtrar_conta(cpf, conta_inserida):

    for conta in contas:
        
        if conta['usuario']['cpf'] == cpf and conta['numero_da_conta'] == conta_inserida:
        
            return conta
    print('Conta não encontrada.')
    
    return False

def main():
    
    LIMITE_SAQUES = 3

    VALOR_MAXIMO_POR_SAQUES = 500

    menu = '''

    [D] Depositar
            
    [S] Sacar
            
    [E] Extrato
            
    [Q] Sair

    [NU] Novo usuário

    [NC] Nova conta

    [L] Listar contas

    '''

    while True:
        
        opcao = input(menu)
        
        # Encerramento
        if(opcao.lower()) == 'q':
            
            print('Fechando o programa.')
            
            break
        
        # Depositar
        
        if(opcao.lower()) == 'd':
            
            if len(usuarios) == 0:
                
                print('Sem usuários para realizar depósito.')
                
                continue
            
            cpf_inserido = int(input('Digite seu CPF: '))
            
            conta_inserida = int(input('Digite o número da sua conta: '))
            
            usuario = filtrar_usuario(cpf_inserido)
            
            conta = filtrar_conta(cpf_inserido, conta_inserida)
            
            if usuario and conta:
                    
                valor_a_depositar = float(input('Insira o valor do depósito: '))
                
                conta['saldo'], conta['transacoes'] = depositar(conta['saldo'], valor_a_depositar, conta['transacoes'], usuario['cpf'], conta['numero_da_conta'])
                
            continue
            
        # Sacar
        
        if(opcao.lower()) == 's':
            
            if len(usuarios) == 0:
                
                print('Sem usuários para realizar saques.')
                
                continue
            
            cpf_inserido = int(input('Digite seu CPF: '))
            
            conta_inserida = int(input('Digite o número da sua conta: '))
            
            usuario = filtrar_usuario(cpf_inserido)
            
            conta = filtrar_conta(cpf_inserido, conta_inserida)
            
            if usuario and conta:
                
                valor_a_sacar = float(input('Digite o valor do saque: '))
                
                conta['saldo'], conta['transacoes'], conta['saques realizados'] = sacar(conta['saldo'], valor_a_sacar, conta['saques realizados'] , conta['transacoes'],
                                                            LIMITE_SAQUES, VALOR_MAXIMO_POR_SAQUES, cpf_inserido, conta_inserida)
                
            continue
        
        # Extrato
        
        if(opcao.lower() == 'e'):
            
            if len(usuarios) == 0:
                
                print('Sem usuários para ver extrato.')
                
                continue
            
            usuario = int(input('Digite seu CPF: '))
            
            conta = int(input('Digite o número da sua conta: '))
            
            mostrar_extrato(usuario, conta)
            
            continue
        
        # Novo usuario
        
        if(opcao.lower() == 'nu'):
            
            novo_usuario = criar_usuario()
            
            usuarios.append(novo_usuario)
            
            continue
        
        # Nova conta
        if(opcao.lower()) == 'nc':
            
            nova_conta = criar_contas()
            
            if nova_conta == None:
                continue
            
            else:
                contas.append(nova_conta)
                
                print(contas)
                
                continue
        
        # Listar contas
        
        if(opcao.lower()) == 'l':
            
            listar_contas()
            continue
        
        else:
            
            print('Comando inválido. Tente outro novamente')
            
            
main()