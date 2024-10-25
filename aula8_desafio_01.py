carrinho = []
valor_total = []
username = input('Digite seu nome de usuario: ') #DevDoces
password = input('Digite sua senha: ') # devdoces08

if username == 'DevDoces' and password == 'devdoces08':
    print('____________Seja bem vindo!!!____________')
    print('''
Selecione o numero respectivo ao produto desejado
          
    0 - Torta de limão
    1 - Torta de maracujá
    2 - Palha Italiana
          ''')
    p1 = int(input('>>> '))
    print('Produto 1 adicionado ao carrinho')
    p2 = int(input('>>> '))
    print('Produto 2 adicionado ao carrinho')
    if p1 == 0 or p1 == 1 or p1 == 2:
        if p1 == 0:
            carrinho.append('Torta de limão')
            valor_total.append(7.50)
        elif p1 == 1:
            carrinho.append('Torta de Maracujá')
            valor_total.append(8.50)
        elif p1 == 2:
            carrinho.append('Palha Italiana')
            valor_total.append(5.75)
    if p2 == 0 or p2 == 1 or p2 == 2:
        if p2 == 0:
            carrinho.append('Torta de limão')
            valor_total.append(7.50)
        elif p2 == 1:
            carrinho.append('Torta de Maracujá')
            valor_total.append(8.50)
        elif p2 == 2:
            carrinho.append('Palha Italiana')
            valor_total.append(5.75)
    if carrinho == carrinho:
        print(f'''
*****FINALIZAÇÃO DA COMPRA*****

    - Produtos selecionados -
              

{carrinho[0]} R${valor_total[0]:.2f}
{carrinho[1]} R${valor_total[1]:.2f}
                         ''')
    valor_do_carrinho = sum(valor_total)
    print(f'''
    TOTAL DA COMPRA - {valor_do_carrinho:.2f}
        ''')
    print('''
   - ESCOLHA A FORMA DE PAGAMENTO - 
    0 - DINHEIRO
    1 - PIX
    2 - CC
    3 - CD                
''')
    forma_pag = int(input('>>> '))
    if forma_pag == 0 or forma_pag == 1 or forma_pag == 2 or forma_pag == 3:
        print('''
              COMPRA FINALIZADA
              Volte Sempre!
              ''')
elif username != 'devdoces08':
    print('''
          Senha incorreta
          Tente Novamente
          ''')
elif password != 'DevDoces':
    print('''
        Nome de Usuário Incorreto
        Tente Novamente
        ''')
else:
    print('''
          Informações de acesso incorretas 
          Tente Novamente
          ''')
    
