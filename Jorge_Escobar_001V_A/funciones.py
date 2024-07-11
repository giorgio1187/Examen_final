import random
import csv


def asignar_sueldos(trabajadores):#asiganamos aleatoriamente

    sueldos = {}
    
    for trabajador in trabajadores:

        sueldo = random.randint(300000,2500000)

        sueldos[trabajadores] = sueldo
    print("Sueldos asignados exitosamente. ")
    print(sueldos)

    return sueldos



def clasificar_sueldos(sueldos): #se define tres listas, para guardar los datos de los distintos sueldos y poder agruparlos, y asi mostrarlos.
    menor_800 = {}
    entre_800_2000 = {}
    mayor_2000 = {}


    for trabajador,sueldo in sueldo.items():
        if sueldo < 800000:
            menor_800 [trabajador]=sueldo
        elif  sueldo <= 2000000:
            entre_800_2000[trabajador]=sueldo
        else:
            sueldo > 2000000
            mayor_2000[trabajador]=sueldo

    print("sueldos menores a 800000, Total", len(menor_800))
    for trabajador,sueldo in menor_800.items():
        print("Nombre del trabajador",trabajador,"Sueldo", sueldo)

    print("sueldos entre 800000 y 2000000, Total", len(entre_800_2000))
    for trabajador,sueldo in entre_800_2000.items():
        print("Nombre del trabajador",trabajador,"Sueldo", sueldo)

    print("sueldos mayores a 2000000, Total", len(mayor_2000))
    for trabajador,sueldo in mayor_2000.items():
        print("Nombre del trabajador",trabajador,"Sueldo", sueldo)
 


def ver_estadisticas(sueldos):

    sueldo_bajo,sueldo_alto,promedio_sueldos = sueldos

    sueldo_bajo = min(sueldos)
    sueldo_alto = max(sueldos)
    promedio_sueldos = sum(sueldos) /len(sueldos)

    return sueldo_bajo,sueldo_alto,promedio_sueldos

 
def generar_reporte(sueldos):
    with open("archivo_registro.csv","w",newline='') as archivo:

        escritor = csv.writer(archivo,delimeter=",")
        escritor.writerow([])


        