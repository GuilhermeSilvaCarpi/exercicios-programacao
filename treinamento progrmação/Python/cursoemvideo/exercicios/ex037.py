#aula 12
n = int(input('um numero inteiro: '))

print('uma base de converção: ')
print('[1]Binário\n[2]Octal\n[3]Hexadecimal')
resposta = int(input('input: '))

if resposta == 1:
    print(bin(n)[2:])
elif resposta == 2:
    print(oct(n)[2:])
elif resposta == 3:
    print(hex(n)[2:])
else:
    print('opção invalida')
