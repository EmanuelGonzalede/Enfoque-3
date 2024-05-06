# Ejemplo de generaci�n de tabla de verdad a partir de una expresi�n l�gica en Python
import itertools

# Expresi�n l�gica y variables
expresion = "(p or q) and (not p)"
variables = ["p", "q"]

# Generar todas las combinaciones posibles de valores para las variables
combinaciones = list(itertools.product([True, False], repeat=len(variables)))

# Evaluar la expresi�n l�gica para cada combinaci�n de valores
resultados = []
for combinacion in combinaciones:
    valores = dict(zip(variables, combinacion))
    resultado = eval(expresion, valores)
    resultados.append(resultado)

# Imprimir tabla de verdad
print("Tabla de Verdad:")
for i, combinacion in enumerate(combinaciones):
    print(f"{combinacion} -> {resultados[i]}")
