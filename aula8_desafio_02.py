clientes = int(input('''
Quantos clientes serão cadastrados
1 ou 2 ou 3 - >>> '''))
if clientes == 1:
    print('Para realizar o cadastro digite as seguintes informações')
    nome1, idade1 = input('Nome Completo: '), int(input('Idade: '))
    print('-----CADASTRO CONCLUIDO-----')
    print('''
Escolha seu Quarto
          
Tipos de Quartos:
0 - Simples: R$100,00 por dia
1 - Duplo: R$150 por dia
2 - Luxo: R$250,00 por dia
''')
    quarto1 = int(input('>>> '))
    if quarto1 == 0:
        quarto1 = 'Simples'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total = dias * 100
    elif quarto1 == 1:
        quarto1 = 'Duplo'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total = dias * 150
    elif quarto1 == 2:
        quarto1 = 'Luxo'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total = dias * 250
    cliente = {
        nome1 : quarto1
    }
    print(cliente)
    print(f'''
Valor total a ser pago por {nome1}

R${valor_total:.2f}

Formas de pagamento
0 - Pix
1 - CC
2 - CD''')
    forma_pag = int(input('>>> '))
    if forma_pag == 0 or forma_pag == 1 or forma_pag == 2:
        print('Agradecemos a preferência \nAproveite a sua Estadia!')
elif clientes == 2:
    print('Para realizar o cadastro digite as seguintes informações')
    nome1, idade1 = input('Nome Completo: '), int(input('Idade: '))
    print('''
Escolha seu Quarto
          
Tipos de Quartos:
0 - Simples: R$100,00 por dia
1 - Duplo: R$150 por dia
2 - Luxo: R$250,00 por dia
''')
    quarto1 = int(input('>>> '))
    if quarto1 == 0:
        quarto1 = 'Simples'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total = dias * 100
    elif quarto1 == 1:
        quarto1 = 'Duplo'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total = dias * 150
    elif quarto1 == 2:
        quarto1 = 'Luxo'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total = dias * 250
    nome2, idade2 = input('Nome Completo: '), int(input('Idade: '))
    print('-----CADASTRO CONCLUIDO-----')
    print('''
Escolha seu Quarto
          
Tipos de Quartos:
0 - Simples: R$100,00 por dia
1 - Duplo: R$150 por dia
2 - Luxo: R$250,00 por dia
''')
    quarto2 = int(input('>>> '))
    if quarto2 == 0:
        quarto2 = 'Simples'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total2 = dias * 100
    elif quarto2 == 1:
        quarto2 = 'Duplo'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total2 = dias * 150
    elif quarto2 == 2:
        quarto2 = 'Luxo'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total2 = dias * 250
    cliente = {
        nome1 : quarto1,
        nome2 : quarto2
    }
    print(cliente)
    print(f'''
Valor total a ser pago por {nome1}

R${valor_total:.2f}

Formas de pagamento
0 - Pix
1 - CC
2 - CD''')
    forma_pag = int(input('>>> '))
    if forma_pag == 0 or forma_pag == 1 or forma_pag == 2:
        print('Agradecemos a preferência \nAproveite a sua Estadia!')
        print(f'''
Valor total a ser pago por {nome2}

R${valor_total2:.2f}

Formas de pagamento
0 - Pix
1 - CC
2 - CD''')
    forma_pag = int(input('>>> '))
    if forma_pag == 0 or forma_pag == 1 or forma_pag == 2:
        print('Agradecemos a preferência \nAproveite a sua Estadia!')
elif clientes == 3:
    print('Para realizar o cadastro digite as seguintes informações')
    nome1, idade1 = input('Nome Completo: '), int(input('Idade: '))
    print('''
Escolha seu Quarto
          
Tipos de Quartos:
0 - Simples: R$100,00 por dia
1 - Duplo: R$150 por dia
2 - Luxo: R$250,00 por dia
''')
    quarto1 = int(input('>>> '))
    if quarto1 == 0:
        quarto1 = 'Simples'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total = dias * 100
    elif quarto1 == 1:
        quarto1 = 'Duplo'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total = dias * 150
    elif quarto1 == 2:
        quarto1 = 'Luxo'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total = dias * 250
    nome2, idade2 = input('Nome Completo: '), int(input('Idade: '))
    print('-----CADASTRO CONCLUIDO-----')
    print('''
Escolha seu Quarto
          
Tipos de Quartos:
0 - Simples: R$100,00 por dia
1 - Duplo: R$150 por dia
2 - Luxo: R$250,00 por dia
''')
    quarto2 = int(input('>>> '))
    if quarto2 == 0:
        quarto2 = 'Simples'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total2 = dias * 100
    elif quarto2 == 1:
        quarto2 = 'Duplo'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total2 = dias * 150
    elif quarto2 == 2:
        quarto2 = 'Luxo'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total2 = dias * 250
        print('Para realizar o cadastro digite as seguintes informações')
    nome3, idade3 = input('Nome Completo: '), int(input('Idade: '))
    print('''
Escolha seu Quarto
          
Tipos de Quartos:
0 - Simples: R$100,00 por dia
1 - Duplo: R$150 por dia
2 - Luxo: R$250,00 por dia
''')
    quarto3 = int(input('>>> '))
    if quarto3 == 0:
        quarto3 = 'Simples'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total3 = dias * 100
    elif quarto3 == 1:
        quarto3 = 'Duplo'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total3 = dias * 150
    elif quarto3 == 2:
        quarto3 = 'Luxo'
        dias = float(input('Quantos dias ficara no Hotel: '))
        valor_total3 = dias * 250
    cliente = {
        nome1 : quarto1,
        nome2 : quarto2,
        nome3 : quarto3,
    }
    print(cliente)
    print(f'''
Valor total a ser pago por {nome1}

R${valor_total:.2f}

Formas de pagamento
0 - Pix
1 - CC
2 - CD''')
    forma_pag = int(input('>>> '))
    if forma_pag == 0 or forma_pag == 1 or forma_pag == 2:
        print('Agradecemos a preferência \nAproveite a sua Estadia!')
        print(f'''
Valor total a ser pago por {nome2}

R${valor_total2:.2f}

Formas de pagamento
0 - Pix
1 - CC
2 - CD''')
    forma_pag = int(input('>>> '))
    if forma_pag == 0 or forma_pag == 1 or forma_pag == 2:
        print('Agradecemos a preferência \nAproveite a sua Estadia!')
        print(f'''
Valor total a ser pago por {nome3}

R${valor_total3:.2f}

Formas de pagamento
0 - Pix
1 - CC
2 - CD''')
    forma_pag = int(input('>>> '))
    if forma_pag == 0 or forma_pag == 1 or forma_pag == 2:
        print('Agradecemos a preferência \nAproveite a sua Estadia!')   

    