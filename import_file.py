#-*-encoding: utf-8 -*-
#-*-encoding:latin-1-*-
import csv


with open ('Test_Fichier_Upload_KFK_1.csv',newline='',encoding='utf8') as f:
    #reader = csv.reader(f)
    reader = csv.DictReader(f)
    
    #for row in reader:
    #    print(row['id'],row['credit'],row['debit'])
    for row in reader:
        for key,values in row.items():
            print (key,values)
            
        #if row is not None:
        #    print ("Ok")
        #else:
        #    print("NOK")
            
        
