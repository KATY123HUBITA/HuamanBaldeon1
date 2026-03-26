//EJERCICIO FIBONACCI
# Pedir al usuario el número de términos
n = int(input("Ingresa cuántos términos de Fibonacci quieres: "))

# Inicializar los dos primeros términos
a, b = 0, 1
fibonacci = []

# Generar la serie de Fibonacci
for _ in range(n):
    fibonacci.append(a)
    a, b = b, a + b

# Mostrar el resultado
print("Serie de Fibonacci:")
print(fibonacci)

# Esperar a que el usuario presione Enter antes de cerrar
input("Presiona Enter para salir...")