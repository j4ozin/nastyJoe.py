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

class FredericoBerel(Personagem):
    def __init__(self):
        super().__init__("Frederico Berel", 90, 18)

    def habilidade_especial(self, alvo):
        dano = self.ataque * 2
        alvo.vida -= dano
        print(f"{self.nome} usou sua habilidade especial contra {alvo.nome}! {alvo.nome} perdeu {dano} pontos de vida.")
        self.mostrar_vida(alvo)

class BogaDoMaruim(Personagem):
    def __init__(self):
        super().__init__("Boga do Maruim", 85, 22)

    def habilidade_especial(self, alvo):
        dano = self.ataque * 3
        alvo.vida -= dano
        print(f"{self.nome} usou sua habilidade especial contra {alvo.nome}! {alvo.nome} perdeu {dano} pontos de vida.")
        self.mostrar_vida(alvo)

class PequenoSapeka(Personagem):
    def __init__(self):
        super().__init__("Pequeno Sapeka", 95, 17)

    def habilidade_especial(self, alvo):
        dano = random.randint(0, self.ataque)
        alvo.vida -= dano
        print(f"{self.nome} usou sua habilidade especial contra {alvo.nome}! {alvo.nome} perdeu {dano} pontos de vida.")
        self.mostrar_vida(alvo)

class LuLadrao(Personagem):
    def __init__(self):
        super().__init__("LuLadrao", 75, 28)

    def habilidade_especial(self, alvo):
        dano = self.ataque * 2
        alvo.vida -= dano
        print(f"{self.nome} usou sua habilidade especial contra {alvo.nome}! {alvo.nome} perdeu {dano} pontos de vida.")
        self.mostrar_vida(alvo)

class JohnnieWalker(Personagem):
    def __init__(self):
        super().__init__("Johnnie Walker", 105, 15)

    def habilidade_especial(self, alvo):
        dano = random.randint(0, self.ataque)
        alvo.vida -= dano
        print(f"{self.nome} usou sua habilidade especial contra {alvo.nome}! {alvo.nome} perdeu {dano} pontos de vida.")
        self.mostrar_vida(alvo)

# Criando as instâncias dos personagens
rei_king = ReiKing()
matue = Matue()
frederico_berel = FredericoBerel()
boga_do_maruim = BogaDoMaruim()
pequeno_sapeka = PequenoSapeka()
lu_ladrao = LuLadrao()
johnnie_walker = JohnnieWalker()

# Lista de personagens para a luta
personagens = [rei_king, matue, frederico_berel, boga_do_maruim, pequeno_sapeka, lu_ladrao, johnnie_walker]

# Luta entre os personagens
while len(personagens) > 1:
    personagem_atacante = random.choice(personagens)
    personagem_alvo = random.choice([p for p in personagens if p != personagem_atacante])
    personagem_atacante.habilidade_especial(personagem_alvo)

    # Remover personagem se foi derrotado
    personagens = [p for p in personagens if p.vida > 0]

# Verificar o vencedor
vencedor = personagens[0]
print(f"\n{vencedor.nome} é o vencedor!")
