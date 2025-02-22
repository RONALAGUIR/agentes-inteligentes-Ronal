def sistema_experto_diagnostico():
    print("Bienvenido al Sistema de diagnóstico")
    print("Por favor, responde con 'sí' o 'no' a las siguientes preguntas:\n")

    fiebre = input("¿Tienes fiebre? (sí/no): ").strip().lower()
    tos = input("¿Tienes tos? (sí/no): ").strip().lower()
    dolor_garganta = input("¿Sientes dolor de garganta? (sí/no): ").strip().lower()
    dificultad_respirar = input("¿Tienes dificultad para respirar? (sí/no): ").strip().lower()
    dolor_cabeza = input("¿Tienes dolor de cabeza? (sí/no): ").strip().lower()

    if fiebre == "sí" and tos == "sí" and dificultad_respirar == "sí":
        diagnostico = "Podrías tener una infección respiratoria o COVID-19. Se recomienda consultar a un médico."
    elif fiebre == "sí" and dolor_garganta == "sí":
        diagnostico = "Podrías tener una gripe común."
    elif fiebre == "no" and tos == "sí" and dolor_cabeza == "sí":
        diagnostico = "Podrías tener una alergia."
    elif fiebre == "no" and tos == "no" and dolor_cabeza == "sí":
        diagnostico = "Podrías estar experimentando estrés."
    else:
        diagnostico = "Los síntomas no son concluyentes. Se recomienda visitar a un médico para un diagnóstico más preciso."

    print("\n Diagnóstico:")
    print(diagnostico)

# Ejecutar el sistema
if __name__ == "__main__":
    sistema_experto_diagnostico()
