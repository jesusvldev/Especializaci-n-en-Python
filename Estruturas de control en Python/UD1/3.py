#3) Comprobador de divisibilidade
a = int(input("Introduce o primeiro número: "))
b = int(input("Introduce o segundo número: "))
print(f"Resto de {a} % {b} =", a % b)



a = int(input("Introduce o primeiro número: "))
b = int(input("Introduce o segundo número: "))

if b == 0:
    print("Non se pode dividir entre 0.")
elif a % b == 0:
    print(f"O número {a} é divisible por {b}.")
else:
    print(f"O número {a} non é divisible por {b}.")
