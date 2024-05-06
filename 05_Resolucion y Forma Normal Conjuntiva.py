# Ejemplo de conversi�n a Forma Normal Conjuntiva (CNF) en Python
import sympy as sp

# Expresi�n l�gica
expresion = "p or (q and r)"

# Convertir expresi�n a CNF
cnf = sp.to_cnf(expresion)

# Imprimir CNF
print("Forma Normal Conjuntiva (CNF):", cnf)
