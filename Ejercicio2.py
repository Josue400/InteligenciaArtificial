import random
import time

class AgenteBuscador:
    def __init__(self, tamano=5):
        self.tamano = tamano
        self.matriz = [[" . " for _ in range(tamano)] for _ in range(tamano)]
        self.pos_x, self.pos_y = 0, 0  # Posición inicial del agente
        self.obj_x, self.obj_y = random.randint(0, tamano-1), random.randint(0, tamano-1)
        self.matriz[self.obj_x][self.obj_y] = " O "  # Colocar el objeto
    
    def mostrar_matriz(self):
        for fila in self.matriz:
            print("".join(fila))
        print("\n")
    
    def mover_agente(self):
        while (self.pos_x, self.pos_y) != (self.obj_x, self.obj_y):
            self.matriz[self.pos_x][self.pos_y] = " . "  # Limpiar posición anterior
            
            if self.pos_x < self.obj_x:
                self.pos_x += 1
            elif self.pos_x > self.obj_x:
                self.pos_x -= 1
            elif self.pos_y < self.obj_y:
                self.pos_y += 1
            elif self.pos_y > self.obj_y:
                self.pos_y -= 1
            
            self.matriz[self.pos_x][self.pos_y] = " A "  # Nueva posición del agente
            
            self.mostrar_matriz()
            time.sleep(0.5)
        
        print("¡Objeto encontrado!\:v/")
        
if __name__ == "__main__":
    agente = AgenteBuscador()
    agente.mostrar_matriz()
    agente.mover_agente()
