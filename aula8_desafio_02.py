# - *Cadastro de Cliente:*
# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 cliente.*
print('''
Fara reserva para quantas pessoas:
1 ou 2 ou 3''')
i = int(input('>>> '))
if i == 1:
    cliente1, idade1 = input('Digite seu nome: '), int(input('Digite sua idade: '))
    cliente = {
        cliente1 : idade1
    }
    print('Cliente Cadastro com Sucesso!')
    print(cliente)
    print('''
Escolha o tipo do seu quarto
Simples ou Duplo ou Luxo:''')
    q1 = input('>>> ')
       
elif i == 2:
    cliente1, idade1 = input('Digite seu nome: '), int(input('Digite sua idade: '))
    cliente2, idade2 = input('Digite seu nome: '), int(input('Digite sua idade: '))
    cliente = {
        cliente1 : idade1,
        cliente2 : idade2
    }
    print('Clientes Cadastro com Sucesso!')
    print(cliente)
    q1 = input('>>> ')
    q2 = input('>>> ')
elif i == 3:
    cliente1, idade1 = input('Digite seu nome: '), int(input('Digite sua idade: '))
    cliente2, idade2 = input('Digite seu nome: '), int(input('Digite sua idade: '))
    cliente3, idade3 = input('Digite seu nome: '), int(input('Digite sua idade: '))                   
    cliente = {                                                                                      
        cliente1 : idade1,
        cliente2 : idade2,
        cliente3 : idade3
    }
    print('Clientes Cadastro com Sucesso!')
    print(cliente)

# - *Reservas de Quartos:*
# ***O sistema deve oferecer 3 tipos de quartos:***  
# ***"Simples", "Duplo" e "Luxo".***

# ***Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***

# - ***Cálculo da Estadia:***

# ***O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***

# Exemplo: 

#  ***valor_cliente3 = preco_duplo * cliente3_dias***

# *Pagamento:*

# *O sistema deve exibir o valor total a ser pago por cada cliente após a aplicação do desconto.*

# *Regras Adicionais:
# Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.*

# ***O sistema não deve usar loops (for, while) nem funções.**
# O código deve considerar todos os casos possíveis de escolha dos clientes.*