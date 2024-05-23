from Class import Mob
from Class import Item
from Class import Armor
from Class import Boss
from Joueur import Joueur
import random
import csv

mobs = []
with open('Class/mob.csv',newline="") as csvfile:
    donnees = csv.DictReader(csvfile, delimiter=";")
    for uneligne in donnees:
        mobs.append(dict(uneligne))
mob=[None for i in range(len(mobs))]
for i in range(len(mobs)):
    mob[i] = Mob(mobs[i]['nom'],float(mobs[i]['pv']),int(mobs[i]['xpp']),float(mobs[i]['atk']))

mobs_boss=[]
with open('Class/mob_boss.csv',newline="") as csvfile:
    donnees = csv.DictReader(csvfile, delimiter=";")
    for uneligne in donnees:
        mobs_boss.append(dict(uneligne))
mob_b=[None for i in range(len(mobs_boss))]
for i in range(len(mobs_boss)):
    mob_b[i] = Boss(mobs_boss[i]['nom'],int(mobs_boss[i]['pv']),int(mobs_boss[i]['xpp']),float(mobs_boss[i]['atk']))

items = []        
with open('Class/item.csv',newline="") as csvfile:
    donnees = csv.DictReader(csvfile, delimiter=";")
    for uneligne in donnees:
        items.append(dict(uneligne))        
item=[None for i in range(len(items))]
for i in range(len(items)):
    item[i] = Item(items[i]['nom'],float(items[i]['att']))
    
armors = []        
with open('Class/armor.csv',newline="") as csvfile:
    donnees = csv.DictReader(csvfile, delimiter=";")
    for uneligne in donnees:
        armors.append(dict(uneligne))        
armor=[None for i in range(len(armors))]
for i in range(len(armors)):
    armor[i] = Armor(armors[i]['nom'],int(armors[i]['mhp']))
    
def tri_boss(l):
    "pour le tri ne prenez pas la liste avec les instances, prenez la liste mobs_boss"
    "tri par selection"
    for i in range(0,len(l)-1):
        m=i
        for j in range(i+1, len(l)):
            if float(l[j]["pv"])/float(l[j]["atk"])<=float(l[m]["pv"])/float(l[m]["atk"]):m=j
        l[m],l[i]=l[i],l[m]
    return(l)   
def tri_mobs(l):
    "pour le tri ne prenez pas la liste avec les instances, prenez la liste mobs"
    "tri par selection"
    for i in range(0,len(l)-1):
        m=i
        for j in range(i+1, len(l)):
            if float(l[j]["atk"])<=float(l[m]["atk"]) and float(l[j]["pv"])<=float(l[m]["pv"]) :m=j
        l[m],l[i]=l[i],l[m]
    return(l)

def tri_items(t):
    "pour le tri ne prenez pas la liste avec les instances, prenez la liste items"
    "tri par insertion"
    for i in range(len(t)):
        valeur = t[i]["att"]
        j=i
        while j > 0 and float(valeur) < float(t[j-1]["att"]):
            t[j]["att"]=t[j-1]["att"]
            j-=1
        t[j]["att"]=valeur
    return(t)
def tri_armors(t):
    "pour le tri ne prenez pas la liste avec les instances, prenez la liste armors"
    "tri par insertion"
    for i in range(len(t)):
        valeur = t[i]["mhp"]
        j=i
        while j > 0 and float(valeur) < float(t[j-1]["mhp"]):
            t[j]["mhp"]=t[j-1]["mhp"]
            j-=1
        t[j]["mhp"]=valeur
    return(t)
f=3
y= random.randint(2,4)
print ("Salutation, à toi jeune aventurier !")
print ("Tu es tombé dans un monde similaire au monde de Minecraft.")
print ("Pour reussir à rester en vie tu vas devoir faire face à des mobs et des boss.")
x=input(str("D'abord quel est ton pseudo? "))             
j=Joueur(x)
print ("Tres beau pseudo",x,"je suis jaloux")
print ("|━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|")
print("|",j,"|")
print ("|━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|")
print (x,"voici tes PV et ton Niveau. Pour le moment tu te bas avec tes poings et tu n'as pas d'armure. ")
print("")
print("Te voilà prêt à affronter des monstres de l'Univers de Minecraft !")
print("Ton but sera de battre",y,"fois des boss")

print("\nVeuillez entrer 'tour_de_combat(j,y,f)' pour commencer le jeu")



def tour_de_combat(j,y,f):
    global mob
    global mob_b
    if y==0:
        print("")
        print("Bravo tu as fini le jeu !!!!!")
        print("Merci d'avoir joué, en espérant que le jeu t'aies plu")
        return("By Pikalex and Romz")
    c=0
    j.reset_pv()
    while c<10:
        m = random.choice(mob)
        print("")
        print("Attention un",m.nom,"approche!")
        if f>0:
            print("Tu peux fuir encore",f,"fois")
        if f==0:
            print("Tu ne peux plus fuir")
        r = input("Veux-tu l'affronter ? (oui/non)      ")
        if r == "oui":
            print("OK")
        elif r =="non":
            if f==0:
                print("Tu ne peux plus fuir, tu es obligé de l'affronter !")
            else:
                f-=1
                print("Courons et prions pour qu'on en croise un autre moins fort")
                return(tour_de_combat(j,y,f))
                
        c+=1
        pv_m=m.get_pv()
        if j.pv < 5:
            o=input("En es-tu sûr? Tu veux pas abandonner? Vu tes PV, il va être difficile de survivre...    (oui/non)       ")
            if o == "oui":
                print("Merci d'avoir joué, tu t'es quand même bien défendu")
                print("En espérant que le jeu t'aies plu...")
                print("Fin de jeu")
                return("By Pikalex and Romz")
            elif o=="non":
                print("J'admire ton courage, force à toi!")
        if j.niv >5:
            m.heal(10)
            m.atk+=2
        if j.niv >9:
            m.heal(15)
            m.atk+=2
        combat(j,m,pv_m)
        if j.pv < 0:
            print("Merci d'avoir joué, tu t'es quand même bien défendu")
            print("En espérant que le jeu t'aies plu...")
            print("Fin de jeu")
            return("By Pikalex and Romz")
        else:
            print("Tu as vaincu le",m.nom)
            print("")
            xp(j,m.get_xpp())
        
    if c==10:
        j.reset_pv()
        b = random.choice(mob_b)
        r = input("Attention un Boss approche veux-tu l'affronter? (oui/non)      ")
        if r =="non":
            print("Dommage un Boss tu peux pas le fuir! Allez prend ton courage à deux mains, tu peux le faire!")
        print("Le Boss qui t'affronte est le",b.nom)
        print("Je vais t'aider tiens, je vais te remettre plein en pv")
        print("Te voilà maintenant à",j.pv, "PV")
        pv_b=b.get_pv()
        if j.niv >5:
            b.heal(10)
        if j.niv >9:
            b.heal(15)
        combat_boss(j,b,5,pv_b)
        if j.pv < 0:
            print("Merci d'avoir joué, tu t'es quand même bien défendu")
            print("En espérant que le jeu t'aies plu...")
            print("Fin de jeu")
            return("By Pikalex and Romz")
        else:
            print ("Tu as réussi à battre le ",b.nom,"!!!")
            print("Voici ses stats ==> ",b)
            xp(j,b.get_xpp())
            c=0
            print("Je te soigne entièrement pour que tu puisses poursuivre ton aventure!")
            return(tour_de_combat(j,(y-1)),3)
        
        

def combat(j,m,pv_m):
    if m.get_pv() <= 0:
        print (m.nom," est mort")
        j.set_heal_combat()
        m.reset_pv(pv_m)
        return(j.pv)
    
    elif j.pv < 0:
        print("Tu es mort")
        print("Il restait au Mob",m.get_pv(),"PV")
        m.reset_pv(pv_m)
        print("Ses stats ==> ",m)
        print("Fin de Jeu")
        return(j.pv)
    
    else:
        print(m.get_pv(),"PV du Mob")
        print("Il te reste ",j.pv,"PV")
        j - m.atk
        return(combat(j,m.damaged(j.atk),pv_m))        

def combat_boss(j,b,p,pv_b):
    if j.pv < 0:
        print ("Tu es mort")
        print("Il restait au Boss",b.get_pv(),"PV")
        b.reset_pv(pv_b)
        print("Ses stats ==> ",b)
        return(j.pv)
    elif b.get_pv() <= 0:
        j.set_heal_combat()
        b.reset_pv(pv_b)
        return(j.pv)
    else:
        print("Boss:",b.get_pv(),"PV")
        p-=1
        if p==0:
            p=5
            print("Il te reste:",j.pv,"PV")
            j - b.atk
        return(combat_boss(j,b.damaged(j.atk),p,pv_b))
    
    
def equipement_arme(j,wea):
    j.atk = wea.att
    j.wea = wea.nom
    
def equipement_armure(j,arm):
    j.pv += arm.mhp
    j.arm_mhp = arm.mhp
    j.arm = arm.nom

def xp(j,xp):
    j + xp
    while j.xp >= 35:
        j.niv+=1
        j.xp-=35 
        if j.niv == 1:
            a=input("tu as la possibilité d'avoir une épée en bois, la veux-tu ? ")
            if a == "oui":
                equipement_arme(j,item[0])
                print("Voici les stats de ta nouvelle arme",item[0].stats())
            else:
                print("tu as gagné",xp," d'xp")                                        
        elif j.niv == 2:
            a=input("tu as la possibilité d'avoir une armure en cuir, la veux-tu ? ")
            if a == "oui":
                equipement_armure(j,armor[0])
                print("Voici les stats de ta nouvelle armure",armor[0].stats())
            else:
                print("tu as gagné",xp," d'xp")
        elif j.niv == 5:
            a=input ("tu as la possibilité d'avoir une épée en or, la veux-tu ? ")
            if a == "oui":
                equipement_arme(j,item[3])
                print("Voici les stats de ta nouvelle arme",item[3].stats())
            else:
                print("tu as gagné",xp," d'xp")
        elif j.niv == 6:
            a=input("tu as la possibilité d'avoir une armure en or ,la veux-tu ? ")
            if a == "oui":
                equipement_armure(j,armor[3])
                print("Voici les stats de ta nouvelle armure",armor[3].stats())
            else:
                print("tu as gagné",xp," d'xp")
        elif j.niv == 8:
             a=input("tu as la possibilité d'avoir une épée en pierre ,la veux-tu ? ")
             if a == "oui":
               equipement_arme(j,item[1])
               print("Voici les stats de ta nouvelle arme",item[1].stats())
             else:
                print("tu as gagné",xp," d'xp")
        elif j.niv == 10:
            a=input ("tu as la possibilité d'avoir une armure en maille ,la veux-tu ? ")
            if a == "oui":
                equipement_armure(j,armor[1])
                print("Voici les stats de ta nouvelle armure",armor[1].stats())
            else:
                print("tu as gagné",xp," d'xp")
        elif j.niv == 11:
            a=input ("tu as la possibilité d'avoir une épée en fer ,la veux-tu ? ")
            if a == "oui":
                equipement_arme(j,item[2])
                print("Voici les stats de ta nouvelle arme",item[2].stats())
            else:
                print("tu as gagné",xp," d'xp")
        elif j.niv == 13:
            a=input ("tu as la possibilité d'avoir une armure en fer ,la veux-tu ? ")
            if a == "oui":
               equipement_armure(j,armor[2])
               print("Voici les stats de ta nouvelle armure",armor[2].stats())
            else:
                print("tu as gagné",xp," d'xp")
        elif j.niv == 16:
            a=input ("tu as la possibilité d'avoir une épée en diamant ,la veux-tu ? ")
            if a == "oui":
               equipement_arme(j,item[4])
               print("Voici les stats de ta nouvelle arme",item[4].stats())
            else:
                print("tu as gagné",xp," d'xp")
        elif j.niv == 18:
            a=input ("tu as la possibilité d'avoir une armure en diamant ,la veux-tu ? ")
            if a == "oui":
                equipement_armure(j,armor[4])
                print("Voici les stats de ta nouvelle armure",armor[4].stats())
            else:
                print("tu as gagné",xp," d'xp")
    print("Tu es à",j.pv,"PV et tu as gagné",xp,"points d'xp et tu es niveau",j.niv)