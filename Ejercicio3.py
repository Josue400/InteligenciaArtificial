import random

import random

def diagnosticar(sintomas):
    """Sistema experto básico para diagnóstico según síntomas."""
    reglas = {
        frozenset(["fiebre", "tos", "dificultad para respirar"]): "Posible infección respiratoria grave. Consulte a un médico.",
        frozenset(["fiebre", "dolor de cabeza"]): "Podría ser una gripe o infección viral. Descanse y manténgase hidratado.",
        frozenset(["dolor de garganta", "tos"]): "Posible resfriado común. Tome líquidos y descanse.",
        frozenset(["dolor abdominal", "náuseas"]): "Podría ser una indigestión o infección estomacal."
    }
    
    for claves, diagnostico in reglas.items():
        if claves.issubset(sintomas):
            return diagnostico
    
    return "Síntomas no reconocidos en la base de datos. Consulte a un especialista."

if __name__ == "__main__":
    print("Bienvenido al sistema experto de diagnóstico.")
    try:
        entrada = input("Ingrese sus síntomas separados por coma: ").lower()
        sintomas_usuario = set(s.strip() for s in entrada.split(","))
        print(f"Síntomas ingresados: {', '.join(sintomas_usuario)}")
        resultado = diagnosticar(sintomas_usuario)
        print(f"Diagnóstico: {resultado}")
    except Exception as e:
        print(f"Error al procesar la entrada: {e}")

