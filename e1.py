"""
exercici número 1
"""
positius = 0
negatius = 0
zero = 0

try:
    for i in range(10):
        num = int(input("Posa un nombre: "))

        if num > 0:
            positius = positius + 1
        elif num < 0:
            negatius = negatius + 1
        else:
            zero = zero + 1

    print("Nombre de numeros positius: ", positius)
    print("Nombre de numeros negatius: ", negatius)
    print("Nombre de zeros: ", zero)
except ValueError:
    print("Valor invalid")

print("Fi del programa")
