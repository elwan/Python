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
        self.fichier_compte_si_tier="si_compte_tiers.csv"
        self.fichier_compte_tier ="compte_tiers.csv"
        self.fichier_correspondance_compte_tiers="correspondance_compte_tiers.csv"
        self.ligne_retourne=ligne 
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
    def si_valeur_est_positive(self):
        """ verifier si montant est correcte avant  de verifier  la negativite de la valeur
retourne vrai si la valeur est positive et retourne faux si la valeur est negative  """
        if len(self.debit) > 0:#voir d'abord  si la ligne n'est pas vide 
            if self.debit[0] is '-':#on test si le premier caractere est un signe negatif 
                self.ecrire_dans_log("Valeur de debit ne doit pas etre negative")
                return False
            else:
                return True
        else:
            if self.credit[0] is '-':
                self.ecrire_dans_log("valeur de debit ne doit pas etre negative")
                return False
            else:
                return True
                           
    def valider(self):
        #print(self.journal,self.credit,self.libelle,self.compte_tiers,self.compte_general,self.compte_tiers,self.date,self.num_piece,self.debit)
        #pass
        if self.si_renseigner() and self.si_montant_est_correcte() and self.verifier_correspondance():
    
            if self.si_valeur_est_positive():
                if self.si_compte_tiers():
                    #print("compte tiers")
                    #o.valider()
                    return self.ligne_retourne
                else:
                    #print("pas de compte tiers")
                    #o.valider()
                    return self.ligne_retourne
            else:
                print("pas de valeur negative")

        
    def ecrire_new_csv(self):
        with open("new_fichier.cvs","a") as f :
            fieldnames = ['id','date','journal','name','period','line_id/account_id','line_id/name','line_id/debit','line_id/credit','line_id/x_numerofacture','ref','partner']
            writer = csv.DictReader(f,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({})

    def ecrire_dans_log(self,error_log):
        with open("odoo.log","a") as f :
            #f.writelines(srt(i))
            f.writelines("-"+"#" * 50 +'\n')
            f.writelines(error_log+'\n')
            
    def verifier_correspondance(self):
       """verifier la correspondance des journaux et des comptes generaux  """
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

    def si_compte_tiers(self):
        """ Verifier si compte compte general  est ossociee a un compte tiers et vefifier si le compte tiers associer au compte general existe """
        self.liste=[]
        self.vide={'',0}
        with open(self.fichier_compte_si_tier,'r') as f:
            t = csv.DictReader(f)
            for e in t :
                self.liste.append(e['code'])
            if self.compte_general in set(self.liste):
                if self.compte_tiers in self.vide:
                    self.ecrire_dans_log("Compte tiers doit etre obligatoirement renseigner")
                    return False
                else:
                    if self.correspondance(self.compte_tiers,self.fichier_compte_tier,"Compte tiers"):
                         #return True
                        if self.si_compte_tiers_correspond():
                          return True
                        else:
                            self.ecrire_dans_log("Correspondance compte tiers compte generale invalide ")
                            return False
                    else:
                        #self.ecrire_dans_log("La valeur du  compte tier est invalide ")
                        return False
            else:
                return True 
    
    #def si_compte_tier_existe(self):
    #    """ verifier si le compte tier associer au compte general existe """
    #    self.liste=[]
    #    with open(self.fichier_compte_tier,'r') as f :
    #        t = csv.DictReader(f)
    #        for e in t :
    #            self.liste.append(e['code'])
    #        if self.compte_tiers in set(self.liste):
    #            return True
    #        else:
    #            return False
    def si_compte_tiers_correspond(self):
        """ verifie si le compte tiers est asssocie au bon compte general dans la configuration de odoo"""
        self.test =[self.compte_tiers,self.compte_general]
        self.petit_liste=[]
        #self.grand_liste=[]
        with open(self.fichier_correspondance_compte_tiers,'r') as f:
            t=csv.reader(f)
            next(t) #sauter le header
            for e in t :
                self.petit_liste.append(e[:-1]) #recuper une partie de la liste et sauter le dernier element
                
        if [a for a in self.petit_liste if set(self.test)==set(a)]: #comparer les deux ensembles et revoi le couple (cpte tiers compte general si la comparaison est vrai 
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
            self.dico = csv.DictReader(f)
            for row in self.dico:
                self.liste_values.append(row)
        
        return self.liste_values #retourne une liste de dictionnaire contenant les elements
                                   
#print( type(Import_Fichier("file.json").importer()))
t = Import_Csv_File("test_import.csv").importer()
#o=Ecriture_Comptable(t0[42])
#print(o.si_compte_tiers_correspond())
#print(o.valider())
#print ("OK")
#print (len(t0))
###if o.si_renseigner() and o.si_montant_est_correcte() and o.verifier_correspondance():
    
#    if o.si_valeur_est_positive():
#        if o.si_compte_tiers():
#            print("compte tiers")
#            o.valider()
#            print(o.ligne_retourne)
#        else:
#            print("pas de compte tiers")
#            o.valider()
#            print(o.ligne_retourne)
#    else:
#        print("pas de valeur negative")
#
def  ecriture(t):    
    liste=[]
    for i in t:
        liste.append(Ecriture_Comptable(i).valider())
    return liste
l=ecriture(t)
print(len(l))
print(type(l))
#print(t)
#for i in ecriture():
#   if i['N de piéce'] is not '':
#        print(i['N de piéce'])
#l=[{'c': 14, 'a': 7, 'd': 15}, {'c': 10, 'a': 7, 'd': 13}, {'c': 16, 'a': 7, 'd': 17}, {'c': 18, 'a': 7, 'd': 19}]
def update_(liste):
    dico=dict()
    liste_=[]
    for i in liste:
        if i is not None:
            i.update({'period':i['Date'][3:]})
            liste_.append(i)
    return liste_

print(update_(l))

#for i in  ecriture():
#    print (i['Date'][3:])
def regrouper_ecriture(liste):
    x=[]
    y=[]
    i=0
    for row in liste:
        print(row['N de piéce'])
    #for i in set(y):
    #    x.append([a for a in liste if a['N de piéce']==i])
    #return y

#groupe = regrouper_ecriture(liste)
#print(type(groupe))
#print(groupe)
#copy_groupe = groupe
#print (len(copy_groupe))
#print (len(copy_groupe[1]))
#print (copy_groupe[1])


def balance(liste):
    somme_credit=0
    somme_debit=0
    #D=[a for a in liste if a[' Montant Débit '] is not '']
    #C=[a for a in liste if a[' Montant Crédit '] is not '']
    #return C,D 
    for element in liste:    
        if element[' Montant Débit '] is not {'',0} :
            somme_debit +=int(element[' Montant Débit '])
        else:
            somme_credit +=int(element[' Montant Crédit '])
    return somme_credit,somme_debit

#print(balance(copy_groupe[0]))
