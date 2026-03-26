
# Pedir al usuario un número
n = int(input("Ingresa un número: "))

# Calcular el factorial
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# Mostrar el resultado
print(f"El factorial de {n} es: {factorial}")

# Esperar a que el usuario presione Enter antes de cerrar
input("Presiona Enter para salir...")