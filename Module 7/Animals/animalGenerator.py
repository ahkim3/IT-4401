import Animal


def main():
    print("Welcome to the animal generator!")
    print("This program creates Animal objects.")
    print()

    # Loop until all desired Animal objects are instantiated
    animals = []
    repeat = 'y'
    while repeat == 'y':
        type = input("What type of animal would you like to create? ")
        name = input("What is the animal’s name? ")
        print()

        animals.append(Animal.Animal(type, name))

        repeat = input("Would you like to add more animals (y/n)? ")
        print()

    # Display the Animal objects
    print("Animal List:")
    for animal in animals:
        print(animal.get_name(), "the", animal.get_animal_type(),
              "is", animal.check_mood())


main()
