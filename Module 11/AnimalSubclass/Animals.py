import random


class Animal:
    def __init__(self, type, name):
        self.__animal_type = type
        self.__name = name

        # Pick a random mood
        num = random.randint(1, 3)
        match num:
            case 1:
                self.__mood = "happy"
            case 2:
                self.__mood = "hungry"
            case 3:
                self.__mood = "sleepy"

    def get_animal_type(self):
        return self.__animal_type

    def get_name(self):
        return self.__name

    def check_mood(self):
        return self.__mood


class Mammal(Animal):
    def __init__(self, type, name, hair_color):
        super().__init__(type, name)
        self.__hair_color = hair_color

    def get_hair_color(self):
        return self.__hair_color


class Bird(Animal):
    def __init__(self, type, name, can_fly):
        super().__init__(type, name)
        self.__can_fly = can_fly

    def get_can_fly(self):
        return self.__can_fly
