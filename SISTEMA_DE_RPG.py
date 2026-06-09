import ramdom
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
        alvo.vida -= self.dano
        if self.mana >= 50:
            print(f"{self.nome} lançou uma magia em {alvo.nome}!")
            self.mana -= 50
            print(f"{alvo.nome} perdeu {self.dano} de vida!")
            print(f"Vida restante de {alvo.nome}: {alvo.vida}")
            print(f"Mana restante de {self.nome}: {self.mana}")
        else:
            print("Mana insuficiente!")    

  
  
class Heroi(Personagem):
    def __init__(self, nome, classe, vida, dano, forca):
        super().__init__(nome, "Heroi", vida, dano)
        self.forca = forca
        
    def ataque_circular(self, alvo):
        if self.forca >= 75:
            print("HYAAAAAA")
            print(f"{self.nome} realizou um ataque circular em {alvo.nome}!")
            print(f"{alvo.nome} perdeu {self.dano} de vida!")
            print(f"Vida restante de {alvo.nome}: {alvo.vida}")
            print(f"Força restante de {self.nome}: {self.forca}")
            self.forca -= 75
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
            print(f"{self.nome} rezou por {alvo.nome}!")
            print(f"{alvo.nome} recuperou {self.dano} de vida!")
            self.alvo.vida += self.dano
            print(f"Vida atual de {alvo.nome}: {alvo.vida}")
            self.fe -= 150
            print(f"Fé restante de {self.nome}: {self.fe}")
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
            print(f"{self.nome} arranhou {alvo.nome} com suas garras afiadas!")
            print(f"{alvo.nome} perdeu {self.dano} de vida!")
            self.alvo.vida -= self.dano
            print(f"Vida restante de {alvo.nome}: {alvo.vida}")
            self.mana -= 65
            print(f"Mana restante de tigresa: {self.mana}")
        else:
            print("Mana insuficante!")    
  
  
dumbledore = Mago("dumbledore", "mago", 50, 150, 300)  
link = Heroi("Link", "Heroi", 250, 50, 500)
uriel = Paladino("Uriel", "Paladino", 240, 180, 200, 500)
tigresa = Nekomata("Tigresa", "Nekomata", 220, 50, 300, "Kung-Fu")



link.ataque_circular(dumbledore)
dumbledore.lancar_magia(tigresa)
tigresa.arranhada(uriel)
uriel.rezar(link)