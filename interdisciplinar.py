op = 'x'

decimal = int(input('Entrada:\nDigite um número Inteiro e em base Decimal: '))
if decimal > 0:
    op = int(input(f'Para qual base você deseja converter o número {decimal}?' + 
                    '\n\b[1 - Binário; 2 - Octadecimal ou 3 - Hexadecimal]: '))

print('\nSaída:')
if op == 1: divisor = 2
elif op == 2: divisor = 8
elif op == 3: divisor = 16
else: 
    divisor = 0
    print('Valor inválido!\nO valor digitado deve estar dentro de [1, 2 e 3]!')

resultado = ''
dec = decimal
if not divisor == 0:
    while dec != 0:
        r = dec % divisor
        if divisor == 16:
            match r: 
                case 10: r = 'A'
                case 11: r = 'B'
                case 12: r = 'C'
                case 13: r = 'D'
                case 14: r = 'E'
                case 15: r = 'F'
        resultado = str(r) + resultado
        dec = dec // divisor
    print(f'{decimal}¹\u2070 convertido para base {divisor} é: {resultado}')
