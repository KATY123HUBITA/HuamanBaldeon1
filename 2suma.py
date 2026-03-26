//SUMA DE CUADRADOS N=5
n = 5

# Calcular la suma de cuadrados
suma = sum(i**2 for i in range(1, n + 1))

# Mostrar el resultado
print(f"La suma de cuadrados hasta {n} es: {suma}")

# Esperar a que el usuario presione Enter antes de cerrar
input("Presiona Enter para salir...")