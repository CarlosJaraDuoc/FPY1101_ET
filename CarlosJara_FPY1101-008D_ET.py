import time
import os
import csv
from random import *

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = []
menores = []
medios = []
mayores = []

def asig_al():
    for i in trabajadores:
        sueldo = randint(300000, 2500000)
        sueldos.append(sueldo)
    return i, sueldo
        


def clas_suel():
    for i in sueldos:
        if i < 800000:
            menores.append(i)                       
        elif i >= 800000 and i <= 2000000:
            medios.append(i)            
        elif i > 2000000:
            mayores.append(i)           
    total = sum(sueldos)
    print(f"Sueldos menores a $800.000 TOTAL: {len(menores)}")
    for i in range (len(menores)):     
        print(trabajadores[i], sueldos[i])
    print(f"Sueldos entre $800.000 y $2.000.000: {len(medios)}")
    for i in range (len(medios)):    
        print(trabajadores[i], sueldos[i])
    print(f"Sueldos mayores a $2.000.000: {len(mayores)}")
    for i in range (len(mayores)):       
        print(trabajadores[i], sueldos[i])
    print(f"TOTAL SUELDOS: ${total}")


def stats():
    sueldoMax = max(sueldos)
    sueldoMin = min(sueldos)
    prom = sum(sueldos) / len(sueldos)
    def geo(x):
        media = 1
        for i in x:
            media *= i
        return media ** (1/len(x))
    print(f"El sueldo máximo es {sueldoMax}")
    print(f"El sueldo más bajo es {sueldoMin}")
    print(f"El promedio de sueldos es {prom}")
    print(f"La media geométrica es {geo(sueldos)}")

def report():
    descSalud = []
    descAFP = []
    liquidos = []
    for i in sueldos:
        salud = i * 0.07
        descSalud.append(salud)
        afp = i * 0.12
        descAFP.append(afp)
        resta = salud + afp
        liquido = i - resta
        liquidos.append(liquido)
    print("Nombre Empleado, Sueldo Base, Descuento Salud, Descuento AFP, Sueldo Liquido")
    for i in range (len(sueldos)):        
        print(trabajadores[i], sueldos[i], descSalud[i], descAFP[i], liquidos[i])
    with open ("ReporteSueldos.csv", "w", newline="") as reporte:
        reporteW = csv.writer(reporte)       
        reporteW.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for i in range (len(trabajadores)):
            reporteW.writerow([trabajadores[i] , sueldos[i] , descSalud[i] , descAFP[i] , liquidos[i] ]) 
     

def salir():
        print("Finalizando programa...\nDesarrollado por Carlos Jara\n RUT 20.713.405-8")

def menu():
    while True:
        os.system("cls")
        try:
            print("Seleccione una opción")
            print("1. Asignar sueldos aleatorios")
            print("2. Clasificar sueldos")
            print("3. Ver estadísticas")
            print("4. Reporte de sueldos")
            print("5. Salir del programa")
            op = int(input())
            if op == 1:
                asig_al()
                time.sleep(2)
            elif op == 2:
                clas_suel()
                time.sleep(6)
            elif op == 3:
                stats()
                time.sleep(4)
            elif op == 4:
                report()
                time.sleep(6)
            elif op == 5:
                salir()
                break
            else:
                print("Debe ingresar un valor dentro del rango (1-5)")
                time.sleep(2)
        except ValueError:
            print("Debe ingresar un número, no letras.")
            time.sleep(2)

menu()