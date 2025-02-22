import random
import os
import time

def agente_buscador():
    grid = [[' ' for _ in range(5)] for _ in range(5)]
    
    objeto_x, objeto_y = random.randint(0, 4), random.randint(0, 4)
    agente_x, agente_y = 0, 0 

    grid[objeto_x][objeto_y] = 'O'

    def mostrar_cuadricula():
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("Matriz del Agente Buscador")
        for fila in grid:
            print(' | '.join([f"{celda:^3}" for celda in fila])) 
        print("\n")

    while (agente_x, agente_y) != (objeto_x, objeto_y):
        grid[agente_x][agente_y] = 'R' 
        mostrar_cuadricula()
        time.sleep(0.5) 
        grid[agente_x][agente_y] = ' '

        if agente_x < objeto_x:
            agente_x += 1
        elif agente_x > objeto_x:
            agente_x -= 1
        elif agente_y < objeto_y:
            agente_y += 1
        elif agente_y > objeto_y:
            agente_y -= 1

    grid[agente_x][agente_y] = 'A'
    mostrar_cuadricula()
    print("¡Encontrado!")

#  Ejecutar el agente buscador de objetos
if __name__ == "__main__":
    agente_buscador()
