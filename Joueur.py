import random

class Joueur:
    
    def __init__(self,nom):
        self.nom = nom
        self.pv = 20 
        self.xp = 0
        self.niv = 0
        self.atk = 2
        self.wea = "Poing"
        self.arm = None
        self.arm_mhp = None
        
    def __str__(self):
        return("Pseudo : %s, PV: %s, Niveau: %s, Arme: %s, Armure: %s ") %(self.nom,self.pv,self.niv,self.wea,self.arm)
        
    def __add__(self,valeur):
        self.xp = self.xp + valeur
        
    def __sub__(self,valeur):
        self.pv = self.pv - valeur
    
    def reset_pv(self):
        if self.arm == None:
            self.pv = 20
        else:
            self.pv = 20 + self.arm_mhp
        return(self)

    def set_heal_combat(self):
        if self.pv < 15:
            self.pv += random.randint(5,15)
        elif self.pv > 25:
            return(self)
        else:
            self.pv += random.randint(1,5)
        return(self)
        