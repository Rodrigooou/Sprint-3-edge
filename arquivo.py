# Importando Biblioteca
import random
import time

while True:
    # Simula a detecção de movimento (1 para detecção, 0 para não detecção)
    motion_detected = random.choice([0, 1])

    if motion_detected:
        print("Movimento detectado!")

    # Aguarda um intervalo de tempo (simula a detecção em intervalos regulares)
    time.sleep(random.uniform(1, 5))
