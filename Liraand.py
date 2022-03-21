# Primeiro and

meta_loja = int(input('Entre com a meta da loja: '))
meta_funcionario = int(input('Entre com a meta do funcionário: '))
vendas_loja = int(input('Entre com as vendas da loja: '))
vendas_funcionario = int(input('Entre com as vendas do funcionário: '))

if vendas_loja >= meta_loja and vendas_funcionario >= meta_funcionario:
    bonus = vendas_funcionario * 0.03
    print('O vendedor ganhou um bônus de {}.'.format(bonus))

