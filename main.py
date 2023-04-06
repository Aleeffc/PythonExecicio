print('Olá, aqui vamos mostrar o aumento salarial!')
salario = float(input('Qual o sálario do funcionário?'))
aumento = salario + (salario * 13 / 100)
print('O fucionário ganhava R$:{:.2f} e começou a ganhar R${:.2f} com 13% no almento do seu salário'.format(salario , aumento))
valor = aumento - salario
print('O valor que foi acrescentado é de R${:.2f}'.format(valor))
