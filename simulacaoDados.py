import random
import time

def rolar_dado(numero_faces):
    time.sleep(0.5)  # Adiciona um pequeno atraso para tornar a simulação mais realista
    return random.randint(1, numero_faces)

def jogar_dados(numero_dados, numero_faces):
    resultados = []
    for _ in range(numero_dados):
        resultado = rolar_dado(numero_faces)
        resultados.append(resultado)
    return resultados

# Exemplo de uso:
numero_dados = 3
numero_faces = 20  # Aumentamos o número de faces para tornar a simulação mais aleatória

resultados = jogar_dados(numero_dados, numero_faces)
print("Resultados:", resultados)
print("Soma dos resultados:", sum(resultados))
