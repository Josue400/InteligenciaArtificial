import time
import random

class SemaforoInteligente:
    def __init__(self):
        self.estado = "rojo"
    
    def detectar_vehiculos(self):
        """Simula la detección de vehículos con un número aleatorio."""
        return random.randint(0, 10)  # Simula entre 0 y 10 vehículos
    
    def cambiar_estado(self):
        """Cambia el estado del semáforo y ajusta la duración según el tráfico."""
        while True:
            vehiculos = self.detectar_vehiculos()
            
            if self.estado == "rojo":
                print("Semáforo en ROJO. Esperando...")
                time.sleep(4)  # Espera fija para rojo
                self.estado = "verde"
            
            elif self.estado == "verde":
                duracion_verde = max(4, min(10, vehiculos))  # Ajusta entre 4 y 10 segundos
                print(f"Semáforo en VERDE. {vehiculos} vehículos detectados. Duración: {duracion_verde} seg.")
                time.sleep(duracion_verde)
                self.estado = "amarillo"
            
            elif self.estado == "amarillo":
                print("Semáforo en AMARILLO. Precaución...")
                time.sleep(2)
                self.estado = "rojo"
            
if __name__ == "__main__":
    semaforo = SemaforoInteligente()
    semaforo.cambiar_estado()
