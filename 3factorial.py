
# Pedir al usuario un número
n = int(input("Ingresa un número: "))

# Calcular el factorial
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# Mostrar el resultado primero
print(f"El factorial de {n} es: {factorial}")

# Mantener la consola abierta hasta que presione Enter
input("Presiona Enter para salir...")