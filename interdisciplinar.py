op = 'valorPadrao0'

def converter(dec = int):
    val = ''
    decimal = dec
    while dec != 0:
        if divisor == 16:
            match r: 
                case 10: r = 'A'
                case 11: r = 'B'
                case 12: r = 'C'
                case 13: r = 'D'
                case 14: r = 'E'
                case 15: r = 'F'
        r = dec % divisor
        val = str(r) + val
        dec = dec // divisor
    print(f'{decimal}¹\u2070 convertido para base {divisor} é: {val}')
    
decimal = int(input('Entrada:\nDigite um número Inteiro e Decimal: '))
if decimal > 0:
    op = int(input(f'Para qual base você deseja converter o número {decimal}?' + 
                    '\n\b[1 - Binário; 2 - Octadecimal ou 3 - Hexadecimal]: '))
    
print('\nSaída:')
match op:
    case 'valorPadrao0':
        print('Valor inválido!\nO valor digitado não pode ser menor ou igual a zero!')
    case 1:
        divisor = 2
        converter(decimal)
    case 2:
        divisor = 8
        converter(decimal)
    case 3:
        divisor = 16
        converter(decimal)
    case _:
        print('Valor inválido!\nO valor digitado deve estar dentro de [1, 2 e 3]!')