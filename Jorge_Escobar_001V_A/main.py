import funciones as fn

trabajadores = [
    "Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"
    ]

sueldos = {}

while True:
    print("    -----   Menu    -----      ")
    print("0. Inicializar sueldos.")
    print("1. Asignar sueldos aleatorios.")
    print("2. Clasificar sueldos. ")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir. ")

    opcion = int(input("Ingrese opcion que desea: "))


    if opcion == 0:
        sueldos = {trabajador : 0 for trabajador in sueldos} #aca inicializamos los valores de los sueldos en cero
        print("Sueldos inicializados...")

    elif opcion == 1:
            fn.asignar_sueldos(trabajadores)
            print(sueldos)

    elif opcion == 2:
        if sueldos:
            fn.clasificar_sueldos(sueldos)
        else:
            print("Debe inicializar sueldos primero...")


    elif opcion == 3:
        sueldo_bajo,sueldo_alto,Promedio_sueldos = sueldos

        print("")




    elif opcion == 4:
        if sueldos:
            fn.generar_reporte
        else:
            print("Debe inicilizar primero")
    
    

    elif opcion == 5:
        print("Finalizando programa...")
        print("Desarrollado por Jorge EScobar")
        print("Rut: 16754362-6")
        break
    else:
        print("Ingrese una opcion valida, de 0 a 5")