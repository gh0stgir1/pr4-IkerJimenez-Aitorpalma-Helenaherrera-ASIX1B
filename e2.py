"""
exercici número 2
"""
try:
    num = 0
    altura = int(input("Quina es la altura?"))
    if altura < 2 or altura > 9:
        raise ValueError("La altura debe estar entre 2 y 9")
    print(1)
    for i in range(2, altura + 1):
        if i == altura:
            print((str(i) + " ") * altura)
        else:
            print(str(i) + " " * (2 * (i - 1) - 1) + str(i))
except:
    print("Asi no era")
