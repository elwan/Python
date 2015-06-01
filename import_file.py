import csv
with open ('Test_Fichier_Upload_KFK_1.csv',newline='') as f:
    #reader = csv.reader(f)
    reader = csv.DictReader(f)
    
    #for row in reader:
    #    print(row['id'],row['credit'],row['debit'])
    for row in reader:
       # for key,values in row.items():
        #    print (key,values)
        print (row)   
