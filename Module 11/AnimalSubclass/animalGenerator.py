import Animals


def main():
    print("Welcome to the animal generator!")
    print("This program creates Animal objects")
    print()

    # Loop until all desired Animal objects are instantiated
    animals = []
    repeat = 'y'
    while repeat == 'y':
        print("Would you like to create a mammal or bird?")
        print("1. Mammal")
        print("2. Bird")
        animal_choice = input("Which would you like to create? ")
        print()

        match animal_choice:
            case "1":  # Mammal
                type = input("What type of mammal would you like to create? ")
                name = input("What is the mammal’s name? ")
                hair_color = input("What is the mammal’s hair color? ")

                animals.append(Animals.Mammal(type, name, hair_color))
            case "2":  # Bird
                type = input("What type of bird would you like to create? ")
                name = input("What is the bird’s name? ")
                can_fly = input("Can the bird fly? ")

                animals.append(Animals.Bird(type, name, can_fly))
            case _:
                print("Invalid choice (must choose 1 or 2).")

        print()
        repeat = input("Would you like to add more animals (y/n)? ")
        print()

    # Display the Animal objects
    print("Animal List:")
    for animal in animals:
        print(animal.get_name(), "the", animal.get_animal_type(),
              "is", animal.check_mood())


main()
