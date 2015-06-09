#Auteur:elwan7@gmail.com
#Version de python:3.4
#Date: Juin 2015

import csv, datetime,sys, json

#creer un objet pour chaque entree faire des verfiction sur les entrees et si tout semble ok on valide pour le faire passer en ecriture vers le nouveau fichier et ensuite le mettre dans les logs 
class Ecriture_Comptable (object):
    def __init__(self,journal,debit,credit,compte):
        self.journal=journal
        self.debit=debit
        self.credit=credit
        self.compte=compte
        self.valide=0
    def valider(self):
        pass
    def ecrire_new_csv(self):
        pass
    def ecrire_dans_log(self):
        pass
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
        
    class Import_csv_file(object):
        def __init__(self,fichier):
            self.fichier=fichier
            self.liste_values=[]
        def importer(self):
            with open(self.fichier,'r') as f:
               dico= csv.DictReader(f)
            for items in dico:
                self.liste_values.append(items)
            return self.liste_values #retourner une liste de dictionnaire
                       
            
#print( type(Import_Fichier("file.json").importer()))

            
        
