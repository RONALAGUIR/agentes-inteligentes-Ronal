import random
import time

def agente_semaforo():

    estado_actual = 'Rojo'

    while True:
        vehiculos = random.randint(0, 10)
        if vehiculos > 5:
            tiempo = 6 
        else:
            tiempo = 3 

        print(f"Estado: {estado_actual}, Vehículos detectados: {vehiculos}, Tiempo: {tiempo}s")
        time.sleep(tiempo)

        if estado_actual == 'Verde':
            estado_actual = 'Amarillo'
        elif estado_actual == 'Amarillo':
            estado_actual = 'Rojo'
        else:
            estado_actual = 'Verde'

# Ejecutar el agente de semáforo inteligente
if __name__ == "__main__":
    agente_semaforo()