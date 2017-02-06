###################
# Supprimer les anciens fichiers .dat et garder les n plus rescents

import os
#import glob
#newest = max(glob.iglob(path + '/*.dat'), key=os.path.getctime)
path = '/Users/elwan7/fichier_dat/'
nombre_fichier_recent = 5

os.chdir(path)
fichiers = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
#anciens= files[0]
nouveau = files[-nombre_fichier_recent:]
file_to_delete = files
for r in nouveau:
    file_to_delete.remove(r)
if file_to_delete:
    for i in file_to_delete:
        os.remove("{}".format(path + '/' + i))
