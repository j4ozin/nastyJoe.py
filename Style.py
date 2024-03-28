import random

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, alvo):
        alvo.vida -= self.ataque
        print(f"{self.nome} atacou {alvo.nome}! {alvo.nome} perdeu {self.ataque} pontos de vida.")
        self.mostrar_vida(alvo)

    def mostrar_vida(self, alvo):
        print(f"{alvo.nome} tem {alvo.vida} pontos de vida.")

class ReiKing(Personagem):
    def __init__(self):
        super().__init__("Rei King", 100, 20)

    def habilidade_especial(self, alvo):
        dano = self.ataque * 2
        alvo.vida -= dano
        print(f"{self.nome} usou sua habilidade especial contra {alvo.nome}! {alvo.nome} perdeu {dano} pontos de vida.")
        self.mostrar_vida(alvo)

class Matue(Personagem):
    def __init__(self):
        super().__init__("Matuê", 80, 25)

    def habilidade_especial(self, alvo):
        dano = random.randint(0, self.ataque)
        alvo.vida -= dano
        print(f"{self.nome} usou sua habilidade especial contra {alvo.nome}! {alvo.nome} perdeu {dano} pontos de vida.")
        self.mostrar_vida(alvo)

def verificar_derrota(personagem):
    if personagem.vida <= 0:
        print(f"{personagem.nome} foi derrotado!")
        return True
    return False

# Criando as instâncias dos personagens
rei_king = ReiKing()
matue = Matue()

# Luta entre os personagens
while True:
    rei_king.habilidade_especial(matue)
    if verificar_derrota(matue):
        break

    matue.habilidade_especial(rei_king)
    if verificar_derrota(rei_king):
        break

# Verificar o vencedor
if rei_king.vida > matue.vida:
    print(f"\n{rei_king.nome} é o vencedor!")
elif matue.vida > rei_king.vida:
    print(f"\n{matue.nome} é o vencedor!")
else:
    print("\nA luta terminou em empate!")
