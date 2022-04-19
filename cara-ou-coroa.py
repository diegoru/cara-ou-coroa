import random

# Gera um núme ro aleatório entre 0 e 1
jogar = random.randint(0,1)

# Define se deverá imprimir cara ou coroa
if jogar == 0:
    print("Cara")
else:
    print("Coroa")