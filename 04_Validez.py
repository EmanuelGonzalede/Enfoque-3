# Ejemplo de validez y satisfacibilidad de una expresi�n l�gica en Python
def validar_satisfacer(expresion):
    # Verificar validez
    if eval(expresion, {"p": True, "q": True}) and eval(expresion, {"p": True, "q": False}) \
            and eval(expresion, {"p": False, "q": True}) and eval(expresion, {"p": False, "q": False}):
        print("La expresion es valida.")
    else:
        print("La expresion no es valida.")

    # Verificar satisfacibilidad
    if eval(expresion, {"p": True, "q": True}) or eval(expresion, {"p": True, "q": False}) \
            or eval(expresion, {"p": False, "q": True}) or eval(expresion, {"p": False, "q": False}):
        print("La expresion es satisfacible.")
    else:
        print("La expresion no es satisfacible.")

# Expresi�n l�gica
expresion = "p or q"

# Validar y verificar satisfacibilidad de la expresi�n
validar_satisfacer(expresion)
