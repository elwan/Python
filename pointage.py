#python3.4
#test program for system time attendance 
import datetime
from time import time sleep


#create employee object
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
#employee login 
    def is_in(self):
        self.temps_arrivee = time()
        self.attendance_in =self.temps_arrivee
        return self.temps_arrivee
#emplotee logout
    def is_out(self):
        self.temps_sortie = time()
        self.attendance_out =self.temps_sortie
        return self.temps_sortie
#save log in file 
    def log(self):
        pass

#validate a attendance 
    def validation_shift(self):
        temps_shift=self.temps_sortie - self.temps_arrivee #doing difference with arrival time et departure time in seconde
        if  temps_shift <=20: #test if the difference is between 0-20
            return True
        else:
            self.shift_normal=20 #if the difference is greater than 20 hold this variable to 20 
            self.heure_suplementaire =temps_shift - self.shift_normal #calcute the addional time before a normal time 
            #print (" vous avez fait {} d'heures suplemetaires".format(self.heure_suplementaire))
            return False
            
    def affiche_temps(self):
        if self.validation_shift(): #if validation is correcte show information 
             if self.temps_sortie > self.temps_arrivee:
                  self.pointage= self.temps_sortie - self.temps_arrivee
                  print( "temps de votre shift est de: {} ".format(self.pointage))
        else:#else show a additional time 
            print (" vous avez fait {} d'heures suplemetaires".format(self.heure_suplementaire))
            

            
test=Employee("Ndiaye","elwan",27,'01/11/2014',"elwan7")

test.is_in()
sleep(22)
test.is_out()
print("temps d'entree {} \n".format(test.attendance_in))
print("temps de sortie {} \n".format(test.attendance_out))
test.affiche_temps()
print ("votre shift normal est de {}".format(test.shift_normal))
        


        
        
        
        
        
