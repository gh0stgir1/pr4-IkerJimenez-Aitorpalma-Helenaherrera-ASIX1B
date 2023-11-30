"""
E3
29/11/23 
"""

try:
    limite = int(input("Posa un límit: "))

    suma_senars = 0
    suma_parells = 0

    for num in range(1, limite + 1):

        if num % 2 == 0:
            suma_parells += num
        else:
            suma_senars += num

    print("Suma nombres senars: ", suma_senars)
    print("Suma nombres parells: ", suma_parells)
except ValueError:
    print("Valor invalid")

print("Fi del programa")

