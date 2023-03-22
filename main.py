print('Hello world')
# "f" é format em python, servindo para adicionar uma variável em meio a uma STRING durante o Print, sendo colocado antes das aspas.

# Soma de Integer
num1 = 10
num2 = 20
total = num1 + num2

print(f'Soma de integer: {total}')

#Soma de Float
n1 = 0.5
n2 = 2
totalFloat = n1 + n2

print(f'Soma de Float: {totalFloat}')

#Soma de String, Agregação
str1 = 'Joao'
str2 = ' Victor'
sumString = str1 + str2

print(f'Soma de String(Agregação): {sumString}')

#Input, por default o valor do input virá como STRING
print('-------------Input---------------')
inputNum1 = int(input('Insira o primeiro número: '))
inputNum2 = int(input('Insira um segundo nomero: '))
totalInput = inputNum1 + inputNum2

print(f'Soma dos inputs: {totalInput}')
print('----------------------------')

# Case if salário, usando 0,1 na multiplicação o salario é aumentado em porcentagem.
# 0.1 = 10%, 0.2 - 20%, e assim por diante
print('---------------Salario-------------')
salary = float(input('Insira seu salário atual: '))

if (salary <= 1000):
  increase = salary + (salary * 0.2)
  print(f'Seu salário sofreu um aumento de 20%, totalizando: {increase}')
elif (salary <= 5000):
  increase = salary + (salary * 0.1)
  print(f'Seu salário sofreu um aumento de 10%, totalizando: {increase}')
print('----------------------------')

#Case boletim, Verifica a media e informa se foi aprovado ou reprovado.
print('--------------Media--------------')
grade1 = float(input('Insira a primeira nota: '))
grade2 = float(input('insira a segunda nota: '))
avg = (grade1 + grade2) / 2

if (avg >= 6):
  print(f'Você foi aprovado!, com uma nota final de {avg}')
elif (avg < 6):
  print(f'Você foi reprovado!, com uma nota final de {avg}')
print('----------------------------')

#case pessoa, verificando se a pessoa é maior de idade.
print('-------------pessoa----------------')
name = input('Insira seu nome: ')
age = int(input('Insira sua idade: '))

if (age >= 18):
  print(f'{name} é maior de idade, tendo {age} anos')
else:
  print(f'{name} não é maior de idade, tendo {age} anos')
print('----------------------------')

#estrutura de repetição, case tabuada
print('--------------Tabuada--------------')
table = int(input('Insira a tabuada que você deseja vizualizar: '))
count = 10

while count != 0:
  soma = table * count
  print(f'{table} x {count} = {soma}')
  count = count - 1
print('----------------------------')

# Break pode ser usado para para um While na falta de uma condicional count.

print('--------------Cadastro pessoa--------------')
while True:
  name = input('insira o nome: ')
  age = int(input('insira a idade: '))
  state = input('insira o estado: ')
  stop = input('Deseja continuar ? (S/N)').upper()

  if (stop == 'N'):
    break
print('----------------------------')
