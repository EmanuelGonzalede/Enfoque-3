# Ejemplo de un sistema experto en diagn�stico m�dico utilizando l�gica de primer orden

# Base de conocimiento: Relaci�n entre s�ntomas y posibles enfermedades
base_conocimiento = {
    "Fiebre": ["Gripe", "Infeccion"],
    "Dolor de cabeza": ["Migra�a", "Tension"],
    "Tos": ["Resfriado", "Bronquitis"]
}

# Funci�n para diagnosticar enfermedades basadas en s�ntomas
def diagnosticar_enfermedad(sintomas):
    enfermedades_posibles = []
    for sintoma in sintomas:
        if sintoma in base_conocimiento:
            enfermedades_posibles.extend(base_conocimiento[sintoma])

    enfermedades_posibles = list(set(enfermedades_posibles))  # Eliminar duplicados

    return enfermedades_posibles

# S�ntomas del paciente
sintomas_paciente = ["Fiebre", "Tos"]

# Diagnosticar enfermedades basadas en los s�ntomas del paciente
enfermedades_diagnosticadas = diagnosticar_enfermedad(sintomas_paciente)

# Imprimir las enfermedades diagnosticadas
if enfermedades_diagnosticadas:
    print("El paciente podria tener las siguientes enfermedades:")
    for enfermedad in enfermedades_diagnosticadas:
        print(enfermedad)
else:
    print("No se encontraron enfermedades que coincidan con los sintomas del paciente.")
