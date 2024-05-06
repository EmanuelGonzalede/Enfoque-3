# Ejemplo de cuantificador existencial en l�gica de primer orden

# Supongamos que queremos verificar si hay alg�n n�mero par en una lista

def hay_numero_par(lista):
    # Cuantificador existencial: hay alg�n elemento x en la lista
    for elemento in lista:
        # Verificar si el elemento es par
        if elemento % 2 == 0:
            return True
    return False

# Lista de ejemplo
numeros = [1, 3, 5, 7, 8, 9]

# Verificar si hay alg�n n�mero par en la lista
resultado = hay_numero_par(numeros)

if resultado:
    print("Hay al menos un numero par en la lista.")
else:
    print("No hay ningun numero par en la lista.")
