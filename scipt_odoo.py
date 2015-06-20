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
        self.fichier_journal="journal.csv"
        self.fichier_compte_general="compte_general.csv"
        self.fichier_compte_tier="compte_tiers.csv"
        
    def si_renseigner(self):#les valeurs ci-dessous sont obligatoires et doivent tjrs etre renseignes 
        liste_averifier={'journal':self.journal,'date':self.date,'compte general':self.compte_general,'Numero de piece':self.num_piece,'Libelle':self.libelle}
        for key,values in liste_averifier.items():
            if values is '':
                print ("{} est obligatoire et doit etre renseigner".format(key))
            else:
                return True
            
    def si_montant_est_correcte(self): # si debit est null credit doit avoir une valeur a 0 et visversa  
        eviter={'',0} #controler si les valeurs ne sont pas null ou egale a zero
        if self.debit in eviter  and self.credit in eviter :
            self.ecrire_dans_log("credit ou debit ne doivent pas etre null")
        elif self.debit not in eviter  and self.credit  not in eviter:
            self.ecrire_dans_log("credit ou debit ne doivent pas avoir des valeurs en meme temps ")
        else: 
            return True
    
                
    def valider(self):
        print(self.journal,self.credit,self.libelle,self.compte_tiers,self.compte_general,self.compte_tiers,self.date,self.num_piece,self.debit)
        pass
    def ecrire_new_csv(self):
        with open("new_fichier.cvs","a") as f :
            fieldnames = ['','','','','','','','','','','']
            writer = csv.DictReader(f,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({})

    def ecrire_dans_log(self,error_log):
        with open("odoo.log","a") as f :
            #f.writelines(srt(i))
            f.writelines("-"+"#" * 50 +'\n')
            f.writelines(error_log+'\n')
            
    def verifier_correspondance(self):
       """verifier la correspondance des journaux,comptes generaux et tiers """
       #verification du journal
       v1=self.correspondance(self.journal,self.fichier_journal,"journal")
       #verfiercation compte genral
       v2=self.correspondance(self.compte_general,self.fichier_compte_general,"compte general")
       #verification compte tiers
       #correspondance(self.compte_tiers,fichier_compte_tier,"compte tiers")
       #verification
       if v1 and v2 :
           return True
       
    def correspondance(self,element,fichier,nature):
        """ Element pour l'objet a verifier ,fichier pour l'object csv a verifier et nature pour differencier un peu la nature des objet a verifier (compte tiers,compte general et journal)"""
        self.fichier=fichier
        self.element=element
        self.nature=nature
        self.liste=[]
        with open(self.fichier,'r') as f:
            t=csv.DictReader(f)
            for e in t:
                self.liste.append(e['code'])
            if self.element in set(self.liste):
                return True
            else:
                self.ecrire_dans_log(" le code  "+self.nature+" "+self.element+" est innexistant")
                return False
#un decorateur pour compter le nombre de fois que une fonction a ete appeler  utile pour compter le nombre d'instance qu'on a traitee 
class NbAppel(object):
    def __init__(self,fonction):
        self.fonction=fonction
        self.appel=0
    def __call__(self,*args):
        self.appel=self.appel +1
        return self.fonction(*args)

class Import_Json(object): #lire un fichier json et retourne un dictionnaire
    """ Lire un fichier json et renvoyer les elemens dans un  dictionnaire """
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
    
    """ Lire un fichier CSV et renvoyer une liste de dictionnaire contenant les elements de chaque ligne """
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
o=Ecriture_Comptable(t0[0])
if o.si_renseigner() and o.si_montant_est_correcte() and o.verifier_correspondance():
    o.valider()
#t1 = Import_Csv_File("code+nom compte ohada.csv").importer()
#for i in t1:
    #y=1
    #print(str(y)+'\n')
 #   print (i["code"])
    #y+=1
    




