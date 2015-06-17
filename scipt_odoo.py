#Auteur:elwan7@gmail.com
#Version de python:3.4
#Date: Juin 2015

import csv, datetime,sys, json

#creer un objet pour chaque entree faire des verfiction sur les entrees et si tout semble ok on valide pour le faire passer en ecriture vers le nouveau fichier et ensuite le mettre dans les logs 
class Ecriture_Comptable (object):
    
    def __init__(self,ligne):
        self.journal=ligne["CJ"]
        self.debit=ligne[" Montant Débit "]
        self.credit=ligne[" Montant Crédit "]
        self.compte_general=ligne["N Compte Général"]
        self.compte_tiers=ligne["N Compte Tiers"]
        self.libelle=ligne["Libellés"]
        self.date=ligne["Date"]
        self.reference=["Référence"]
        self.num_facture=ligne["N Facture"]
        self.num_piece=ligne["N de piéce"]
        self.valide=0
        self.fichier_journal=""
        self.fichier_compte_general="code+nom compte ohada.csv"
        self.fichier_compte_tier=""
        
    def valider(self):
        print(self.journal,self.credit,self.libelle,self.compte_tiers,self.compte_general)
        
        pass
    def ecrire_new_csv(self):
        
        pass
    def ecrire_dans_log(self,error_log):
        with open("odoo.log","a") as f :
            #f.writelines(srt(i))
            f.writelines("-"+"#" * 50 +'\n')
            f.writelines(error_log+'\n')
            
    def verifier_correspondance(self):
       #dict_journaux = Import_Fichier("journaux.json").importer()
       #dict_elements =Import_Fichier(fichier).importer()
       #dict_compte_tier=Import_Fichier("compte_tiers.json").importer()
       #for  items  in dict_elements.keys():
       #    if  element == items :
        #       return True
       #    else:
       #        return False
       #verifier la correspondance des journaux,comptes et si la ligne contient une valeur dans debit ou credit.
       #verification du journal
       #correspondance(self.journal,fichier_journal,"journal")
       #verfiercation compte genral
       self.correspondance(self.compte_general,self.fichier_compte_general,"compte general")
       #verification compte tiers
       #correspondance(self.compte_tiers,fichier_compte_tier,"compte tiers")
       #verification  validite debit ou credit
       if self.debit==0 and self.credit==0 :
           self.ecrire_dans_log("balance incorrecte")
       else:
           return True
       
    def correspondance(self,element,fichier,nature):
        """ Element pour l'objet a verifier ,fichier pour l'object csv a verifier et nature pour differencier un peu la nature des objet a verifier (compte tiers,compte general et journal)"""
        with open(fichier,'r') as f:
            for e in csv.DictReader(f):
                if element==e["code"]:
                    return True
                else:
                    self.ecrire_dans_log("le code "+nature+"est innexistant"+element)
        

                    

#un decorateur pour compter le nombre de fois que une fonction a ete appeler  utile pour compter le nombre d'instance qu'on a traitee 
class NbAppel(object):
    def __init__(self,fonction):
        self.fonction=fonction
        self.appel=0
    def __call__(self,*args):
        self.appel=self.appel +1
        return self.fonction(*args)

class Import_Fichier(object): #lire un fichier json et retourne un dictionnaire
    def __init__(self,fichier):
        self.fichier=fichier
        #self.liste_values=[]
        
    def importer(self):
        with open(self.fichier) as json_ficher:
            return json.load(json_ficher) #retourne un dictionnaire des elements contenu dans le fichier 
        #for values in listejson.items():
        #   self.liste_values.append(values)
        #return self.liste_values
        
class Import_Csv_File(object):
        def __init__(self,fichier):
            self.fichier=fichier
            self.liste_values=[]
            #self.dico={}
        def importer(self):
            with open(self.fichier,'r') as f:
               # self.dico = csv.DictReader(f)
                for row in csv.DictReader(f):
                    self.liste_values.append(row)
            return self.liste_values #retourne une liste de dictionnaire contenant les elements
                                   
#print( type(Import_Fichier("file.json").importer()))
t0 = Import_Csv_File("Test_Fichier_Upload_KFK_1.csv").importer()
o=Ecriture_Comptable(t0[2])
if o.verifier_correspondance():
    o.valider()
#t1 = Import_Csv_File("code+nom compte ohada.csv").importer()
#for i in t1:
    #y=1
    #print(str(y)+'\n')
 #   print (i["code"])
    #y+=1


    
    




