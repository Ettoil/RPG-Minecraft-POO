class Mob:
    """ Mob defini par :
        -nom
        -pv
        -xpp
        -wea"""
    def __init__(self,nom,pv,xpp,atk):
        self.nom = nom
        self.__pv = pv
        self.__xpp = xpp
        self.atk = atk
        
    def __str__(self):
        return("Nom : %s, PV: %s, Dégâts: %s" %(self.nom,self.__pv,self.atk))
    
    def get_xpp(self):
        return(self.__xpp)
    
    def damaged(self,atk):
        self.__pv-=atk
        return self
    
    def get_pv(self):
        return(self.__pv)
    
    def reset_pv(self,pv):
        self.__pv=pv
        return(self)
    
    def heal(self,valeur):
        self.__pv+=valeur
        return(self)

class Boss:
    """Boss defini par : 
        -nom
        -pv
        -xpp
        -wea"""
        
    def __init__(self,nom,pv,xpp,atk):
        self.nom = nom
        self.__pv = pv
        self.__xpp = xpp
        self.atk = atk
    def __str__(self):
        return("Nom : %s, PV: %s, Dégâts: %s" %(self.nom,self.__pv,self.atk))
    
    def get_xpp(self):
        return(self.__xpp)
    
    def get_pv(self):
        return(self.__pv)
    
    def damaged(self,atk):
        self.__pv-=atk
        return self
    
    def reset_pv(self,pv):
        self.__pv=pv
        return(self)
    
    def heal(self,valeur):
        self.__pv+=valeur
        return(self)

class Item:
    """ Item defini par :
        -nom
        -att"""
        
    def __init__(self,nom,att):
        self.nom = nom 
        self.att = att
    
    def stats(self):
        return("Nom:",self.nom,"Dégâts:",self.att)
    
class Armor:
    """Armor defini par :
        -nom
        -mhp"""
        
    def __init__(self,nom,mhp):
        self.nom = nom
        self.mhp = mhp
             
    def stats(self):
        return("Nom:",self.nom,"Défense:",self.mhp,"PV en +")
    
                 

