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
        
    def valider(self):
        
        pass
    def ecrire_new_csv(self):
        
        pass
    def ecrire_dans_log(self,error_log):
        with open("odoo.log","a") as f :
            #f.writelines(srt(i))
            f.writelines("-"+"#" * 50 +'\n')
            f.writelines(Error_log+'\n')
            
    def verifier_correspondance(self,element,fichier):
       #dict_journaux = Import_Fichier("journaux.json").importer()
       dict_elements =Import_Fichier(fichier).importer()
       #dict_compte_tier=Import_Fichier("compte_tiers.json").importer()
       for  items  in dict_elements.keys():
           if  element == items :
               return True
           else:
               return False
           

#un decorateur pour compter le nombre de fois que une fonction a ete appeler  utile pour compter le nombre d'instance qu'on a traitee 
class NbAppel(object):
    def __init__(self,fonction):
        self.fonction=fonction
        self.appel=0
    def __call__(self,*args):
        self.appel=self.appel +1
        return self.fonction(*args)

class Import_Fichier(object):
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
        def __init__(self):
            #self.fichier=fichier
            self.liste_values=[]
            self.dico={}
        def importer(self,fichier):
            with open(fichier,'r') as f:
                self.dico = csv.DictReader(f)
                for row in self.dico:
                    self.liste_values.append(row)
            return self.liste_values #retourne une liste de dictionnaire contenant les elements
                                   
#print( type(Import_Fichier("file.json").importer()))
t = Import_Csv_File().importer("Test_Fichier_Upload_KFK_1.csv")
print (t)
