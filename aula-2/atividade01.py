num = int(input('Usuário, digite um número: '))
antecessor = num - 1
sucessor = num + 1
print(f'O número escolhido foi {num}, o antecessor é {antecessor} e o sucessor é {sucessor}')

# ---------------------------------------------------------------------------------------------

num = int(input('Usuário, digite um número: '))
print(f'O número escolhido foi {num}, o antecessor é {num - 1} e o sucessor é {num + 1}')

# ---------------------------------------------------------------------------------------------

salario = float(input('Digite seu salário: R$ '))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f'O aumento foi de: R$ {aumento:.2f} - O novo salário é de: R$ {novo_salario:.2f}')