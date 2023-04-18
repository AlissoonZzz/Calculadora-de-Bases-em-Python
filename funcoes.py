import math

def decimal_para_binario(decimal):
    convertido = ''
    while decimal != 1:
        convertido += str(decimal %2) 
        decimal = math.floor(decimal / 2)
    convertido += "1"
    return convertido[::-1]

def decimal_para_octal(decimal): 
    convertido = ''
    while decimal > 8:
        convertido += str(decimal %8) 
        decimal = math.floor(decimal / 8)
    else: 
        convertido += str(decimal)
    return convertido[::-1]


def decimal_para_hexadecimal(decimal): 
    convertido = ''
    hex_codes = { 
        0: "0", 
        1: "1",
        2: "2", 
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "c",
        13: "D",
        14: "E",
        15: "F"
    }

    while decimal > 16:
        convertido += hex_codes[decimal %16] 
        decimal = math.floor(decimal / 16)
    else: 
        convertido += str(decimal)
    return convertido[::-1]
def octdec(num):
    soma=0
    i=0
    while num!=0:
        rem=num%10
        soma+=rem*pow(8,i)
        i+=1
        num=num//10
    return soma
