import datetime
from time import time
from time import sleep

class Employee(object):
    def __init__(self,name,prenom,age,date_debut,code):
        self.nom=name
        self.prenom=prenom
        self.age=age
        self.date_debut=''
        self.attendance_in=0
        self.attendance_out=0
        self.attendance_mois=''
        self.attendance_annee=''
        self.code=''
        self.shift_normal=0
        self.heure_suplementaire=0

    def is_in(self):
        self.temps_arrivee = time()
        self.attendance_in =self.temps_arrivee
        return self.temps_arrivee
    def is_out(self):
        self.temps_sortie = time()
        
        self.attendance_out =self.temps_sortie
        return self.temps_sortie
    def log(self):
        pass
    
    def validation_shift(self):
        temps_shift=self.temps_sortie - self.temps_arrivee
        if  temps_shift <=20:
            return True
        else:
            self.shift_normal=20
            self.heure_suplementaire =temps_shift - self.shift_normal
            #print (" vous avez fait {} d'heures suplemetaires".format(self.heure_suplementaire))
            return False
            
    def affiche_temps(self):
        if self.validation_shift():
             if self.temps_sortie > self.temps_arrivee:
                  self.pointage= self.temps_sortie - self.temps_arrivee
                  print( "temps de votre shift est de: {} ".format(self.pointage))
        else:
            print (" vous avez fait {} d'heures suplemetaires".format(self.heure_suplementaire))
            

test=Employee("Ndiaye","elwan",27,'01/11/2014',"elwan7")

test.is_in()
sleep(22)
test.is_out()
print("temps d'entree {} \n".format(test.attendance_in))
print("temps de sortie {} \n".format(test.attendance_out))
test.affiche_temps()
print ("votre shift normal est de {}".format(test.shift_normal))
        


        
        
        
        
        
