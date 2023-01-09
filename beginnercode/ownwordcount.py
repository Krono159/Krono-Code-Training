import csv
import string
counter = 0
type = 0
wordcounter = {}
try:
    file = open('./begginercode/test.txt').read()
    type = 1
except:
    print("no se pudo abrir el archivo... error code: 1")
    file = input("ingrese una frase:  \t\t\n")
    type = 2
words = file.split()

for e in words:
    count = wordcounter.get(e,0)
    count +=1
    counter += 1
    wordcounter[e] = count

if type == 1:
    print("el archivo tiene: ",counter," palabras")
elif type == 2: 
    print("la frase ",file," tiene ",counter," palabras")
else:
    print("error desconocido")