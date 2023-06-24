#
grades = []
menu_option = ""
while menu_option != "3":
    print("Calculadora de promedios")
    print("1. Agregar nota")
    print("2. Calcular promedio")
    print("3. Salir")    
    menu_option = input()    
    if menu_option == "1":
     notas = float(input("Inserte sus notas"))
     grades.append(notas)
     print("Nota agregada con éxito")

    elif menu_option == "2":
        # Sumar todas las notas y dividir por la cantidad
        # Acumulador
        sum = 0 
        for grade in grades:
           sum += grade 
        print(f"El promedio de notas es {sum/len(grades)}")   
        pass
    elif menu_option == "3":
        print("Chaucito")
    else:
        print("Ingrese algo válido")
