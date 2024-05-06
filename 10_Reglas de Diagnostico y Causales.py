# Ejemplo de regla causal en l�gica de primer orden

# Supongamos que queremos modelar la relaci�n causal entre el consumo de az�car y el aumento de peso.

def aumentar_peso(consumo_azucar):
    # Regla causal: Si el consumo de az�car es alto, entonces se aumenta de peso.
    if consumo_azucar == "Alto":
        return "Aumento de peso"
    else:
        return "No hay aumento de peso"

# Nivel de consumo de az�car
consumo_azucar = "Alto"

# Determinar el efecto en el peso
efecto_peso = aumentar_peso(consumo_azucar)
print("Efecto en el peso:", efecto_peso)
