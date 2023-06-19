dogs = []
menu_option = ""
while menu_option != "3":
    print("1.Agregar cachorros")
    print("2.Ver cachorritos")
    print("3.Salir")
    menu_option = input()

    if menu_option == "1":
        dog = []
        name = input("Ingrese el nombre de su cachorrito")
        age = int(input("ingrese la edad de su cachorro"))
        breed = input("Ingrese la raza de su cachorro")

        dog.append(name)
        dog.append(age)
        dog.append(breed)
        dogs.append(dog)

        print("Cachorrito agregado con éxito")

    elif menu_option == "2":  
        number = 0  
        while number < len(dogs):
            print(f"el nombre: { dogs[number][0]}\n"
                  f"la edad: {dogs[number][1]}\n"
                  f"la raza: {dogs[number][2]}\n")
            number += 1 

    elif menu_option == "3":
        print("Gracias, hasta la próxima")