//EJERCICIO FIBONACCI
# Número de términos
n = int(input("Ingresa cuántos términos de Fibonacci quieres: "))

# Inicializar los dos primeros términos
a, b = 0, 1

# Mostrar la serie
print("Serie de Fibonacci:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()  # Salto de línea al final

# Esperar a que el usuario presione Enter antes de cerrar
input("Presiona Enter para cerrar...")