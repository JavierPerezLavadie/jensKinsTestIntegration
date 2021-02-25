import sys;
import os;
from genericpath import exists


pathOfClientFile = 'client.txt';
print(pathOfClientFile);

separator = ";";

dataNombreForeachlin = 4;

def get_file_name(filePath):
    fileName =os.path.basename(filePath)
    print('Nom du fichier:',fileName)
    return fileName

def isExisteFile(filePath):
    exist = False
    if os.path.exists(filePath) > 0:
        exist = True
        print('Le fichier:',exist)
    return exist

def isEmPtyFile(filePath):
    isEmPtyFile = False
    if os.path.getsize(filePath) > 0:
        isEmPtyFile = True
    print("La taille du fichier est",isEmPtyFile)

def checkDataNumberForEachLin(filePath):
    checkDataNumber = True
    with open (filePath, 'r') as filin:
        lignes = filin.readlines()
        for ligne in lignes : 
            datas = ligne.split(separator)
            if len (datas) < dataNombreForeachlin:
                print(datas)
                checkDataNumber = False
                return checkDataNumber

if __name__ =='__main__':
    isExisteFile(pathOfClientFile)
    get_file_name(pathOfClientFile)
    isEmPtyFile(pathOfClientFile)
    print(checkDataNumberForEachLin(pathOfClientFile))
    










