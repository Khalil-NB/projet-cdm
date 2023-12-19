import random

class NPC:
   def __init__(self):
      self.force = roulerDes()
      self.agilite = roulerDes()
      self.constitution = roulerDes()
      self.intelligence = roulerDes()
      self.sagesse = roulerDes()
      self.charisme = roulerDes()
      self.classe_d_armure = random.randint(1,12)
      self.nom = "victor"
      self.race = "blanc"
      self.espece = "humain"
      self.point_de_vie = random.randint(1,20)
      self.profession = "guerrier"
      
   def attributs(self):
      print("force:", self.force)
      print("agilité:", self.agilite)
      print("constitution:", self.constitution)
      print("intelligence:", self.intelligence)
      print("sagesse:", self.sagesse)
      print("charisme:", self.charisme)
      print("classe d'armure:", self.classe_d_armure)
      print("nom:", self.nom)
      print("race:", self.race)
      print("espèce:", self.espece)
      print("point de vie:", self.point_de_vie)
      print("profession:", self.profession)

def roulerDes():
   somme = 0
   plusPetit = 6
   for i in range(4):
      de = random.randint(1, 6)
      if (de < plusPetit):
         plusPetit = de
      somme += de
   somme -= plusPetit
   return somme

class Kobold(NPC):
   def __init__(self):
      super().__init__()
      
   def attaquer(self, cible):
      return

   def subir_dommage(self, dommage):
      self.point_de_vie -= dommage
      
class Hero(NPC):
   def __init_(self):
      super().__init__()
      
   def attaquer(self, cible):
      d20 = random.randint(1,20)
      if d20 == 20:
         cible.subir_dommage(random.randint(1,8))
      elif d20 > 1 and d20 < 20:
         if d20 > cible.classe_d_armure:
            cible.subir_dommage(random.randint(1,6))
                     
   def subir_dommage(self, dommage):
      self.point_de_vie -= dommage

# npc = NPC()

# npc.attributs()

print()
kobold = Kobold()
kobold.espece = "kobold"
kobold.race = "vert"
kobold.nom = "glob"
kobold.attributs()
print()

hero = Hero()
hero.nom = "jeff"
hero.attributs()
print()

hero.attaquer(kobold)

print()
kobold.attributs()
print()

hero.attributs()
print()




