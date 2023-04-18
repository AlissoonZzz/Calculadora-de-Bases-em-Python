import math
import funcoes
while True:
    print('Menu')
    print('[1] Decimal para outras bases\n[2] Outras bases para Decimal\n[0] Sair')
    op = int(input("Digite uma opção: "))
    if op == 0:
        break
    elif op == 1:
        while True:
            print('Decimal para outras bases')
            print('[1] Decimal para Binário\n[2] Decimal para Octal\n[3]Decimal para Hexadecimal\n[0] Sair')
            op = int(input('Digite uma opção: '))
            if op == 0:
                break
            elif op == 1:
                nDecimal = int(input("Digite um Nº decimal: "))
                binario = funcoes.decimal_para_binario(nDecimal)
                print (f"o valor convertido para binario é {binario}")
            elif op == 2:
                nDecimal = int(input('Digite um Nº decimal: '))
                octal = funcoes.decimal_para_octal(nDecimal)
                print (f"o valor convertido para octal é {octal}")
            elif op == 3:
                nDecimal = int(input('Digite um Nº decimal: '))
                hexadecimal = funcoes.decimal_para_hexadecimal(nDecimal)
                print (f"o valor convertido para hexadecimal é {hexadecimal}")
    elif op ==2:
            print('outras bases para decimal')
            print('[1] Binario para Decimal\n[2] octal para Decimal\n[0] Sair')
            op = int(input('Digite uma opção: '))
            if op == 0:
                break
            elif op == 1:
                num = int(input('Digite um número: '))
                n = len(str(num))
                valor_digitado = num
                decimal = 0
                i = 0
                while n > 0:
                    resto = num%10
                    decimal = decimal + (resto * (2**i))
                    n = n - 1
                    i = i + 1
                    num = num//10
                print(f"o numero binario {valor_digitado} em decimal é: {decimal}")
            elif op == 2:
                num=int(input("Digite um numero : ")) 
                dec=funcoes.octdec(num)
                print(f"o numero Octal {num} em decimal é: {dec}")
            else:
                print('Opção inválida')
    else:
        print(("opção inválida"))