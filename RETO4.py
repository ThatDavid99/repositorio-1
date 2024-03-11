#Reto 4 mona
import csv

with open("RETO4.csv", "r") as f :
    norte = 0
    sur = 0
    oriente = 0
    occidente = 0
    leer = csv.reader(f,delimiter=";")
    for r in leer:
        print (r[5])
        if r[5] == "occidente":
          occidente += 1  
        if r[5] == "norte":
          norte += 1 
        if r[5] == "sur":
          sur += 1 
        if r[5] == "oriente":
          oriente += 1    
    
print("Cantidad de usuarios en zona occidente:",occidente)
print("Cantidad de usuarios en zona norte:",norte)
print("Cantidad de usuarios en zona sur:",sur)
print("Cantidad de usuarios en zona oriente:",oriente)
print (sur)
if occidente > norte and occidente > sur and occidente > oriente:
        print ("La zona con mas usuarios es: Occidente")
if norte > occidente and norte > sur and norte > oriente:
        print ("La zona con mas usuarios es: Norte")
if sur > norte and sur > occidente and sur > oriente:
        print ("La zona con mas usuarios es: Sur")
if oriente > norte and oriente > sur and oriente > occidente:
        print ("La zona con mas usuarios es: Oriente")



