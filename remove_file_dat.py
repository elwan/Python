# Supprimer les anciens fichiers .dat et garder les n plus rescents

import os
#import glob
#newest = max(glob.iglob(path + '/*.dat'), key=os.path.getctime)
path = '/Users/elwan7/fichier_dat/'
nombre_fichier_recent = 5

os.chdir(path)
fichiers = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
fichiers_dat = []
#anciens= files[0]
for element in fichiers:
    if element.endswith('.dat'):  # rechercher les fichiers terminant par .dat
        fichiers_dat.append(element)

liste_nouveau = fichiers_dat[-nombre_fichier_recent:]  # lister les n nouveau fichier par date de derniere modification
file_to_delete = fichiers_dat
for r in liste_nouveau:
    file_to_delete.remove(r)
if file_to_delete:
    for i in file_to_delete:
        os.remove("{}".format(path + '/' + i))
