import time

texto = "O heroi hyliano ergueu sua espada mestra e deu com tudo na cabeça do grande mago Dumbledore!"

for letra in texto:
    print(letra, end="", flush=True)
    time.sleep(0.05)

print()


class Personagem:
    def __init__(self,nome, classe, vida, dano):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.dano = dano
    def atacar(self, alvo):
        alvo.vida -= self.dano
        print(f"{self.nome} atacou {alvo.nome}!")
        print(f"{alvo.nome} perdeu {self.dano} de vida!")
        print(f"Vida restante de {alvo.nome}: {alvo.vida}")
        if alvo.vida <= 0:
            print(f"{alvo.nome} desmaiou!")
        
        
class Mago(Personagem):
    def __init__(self, nome, classe, vida, dano, mana):
        super().__init__(nome, "Mago", vida, dano)
        self.mana = mana
        
    def lancar_magia(self, alvo):
        if self.mana >= 50:
            print("Bola de fogo lançada!")
            self.mana -= 50
            print(f"Mana restante {self.mana}")
        else:
            print("Mana insuficiente!")    
  
  
class Heroi(Personagem):
    def __init__(self, nome, classe, vida, dano, forca):
        super().__init__(nome, "Heroi", vida, dano)
        self.forca = forca
        
    def ataque_circular(self, alvo):
        if self.forca >= 75:
            print("HYAAAAAA")
            self.forca -= 75
            print(f"Forca restante {self.forca}")
        else:
            print("Força insuficiente")
        
        
class Paladino(Personagem):
    def __init__(self, nome, classe, vida, dano, mana, fe):
        super().__init__(nome, "Paladino", vida, dano)
        self.mana = mana
        self.fe = fe
    
    def rezar(self, alvo):
        self.alvo = alvo
        if self.fe >= 150:
            print("Que Deus tenha misericórdia de tua alma!!")
            self.fe -= 150
            print(f"Fé restante {self.fe}")
        else:
            print("Fé insuficiente")
    
class Nekomata(Personagem):
    def __init__(self, nome, classe, vida, dano, mana, arte_marcial):
        super().__init__(nome, "Nekomata", vida, dano)
        self.arte_marcial = arte_marcial 
        self.mana = mana
        
  
    def arranhada(self, alvo):
        self.alvo = alvo
        if self.mana >= 65:
            print("Arranhada na cara hehe!")
            self.mana -= 65
            print(f"Mana restante {self.mana}")
        else:
            print("Mana insuficante!")    
  
  
dumbledore = Mago("dumbledore", "mago", 50, 150, 300)  
link = Heroi("Link", "Heroi", 250, 50, 500)
uriel = Paladino("Uriel", "Paladino", 240, 180, 200, 500)
tigresa = Nekomata("Tigresa", "Nekomata", 220, 50, 300, "Kung-Fu")



link.ataque_circular(dumbledore)
dumbledore.atacar(tigresa)
tigresa.atacar(uriel)
uriel.atacar(link)