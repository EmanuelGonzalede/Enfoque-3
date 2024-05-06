# Ejemplo de conversión a Forma Normal Conjuntiva (CNF) en Python
import sympy as sp

# Expresión lógica
expresion = "p or (q and r)"

# Convertir expresión a CNF
cnf = sp.to_cnf(expresion)

# Imprimir CNF
print("Forma Normal Conjuntiva (CNF):", cnf)
