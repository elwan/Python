#-*-coding:utf-8 -*-
#cvs process to make right csv file for uploading journal item in odoo
import csv, sys,codecs

#print (sys.getdefaultencoding())


with open ('Test_Fichier_Upload_KFK_1.csv','r') as f:
        reader = csv.reader(f)
        #reader = csv.DictReader(f)

            #for row in reader:
                #    print(row)
        #for row in reader:
        #    for key,values in row.items():
        #        print (key,values)
        try:
            for row in reader:
                print (row)
        except csv.Error as e:
            sys.exit('file {}, line {} : {}'.format(filename,reader.line_num,e))
            
def validation(liste):
    liste=[]
    
