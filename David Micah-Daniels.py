class Animal:
    def __init__(self, name, behaviour, diet, habitat, lifespan, speed, sound, can_reproduce, number_of_legs, is_mammal):
        self.name = name
        self.behaviour = behaviour
        self.diet = diet
        self.habitat = habitat
        self.lifespan = lifespan
        self.speed = speed
        self.sound = sound
        self.can_reproduce = can_reproduce
        self.number_of_legs = number_of_legs
        self.is_mammal = is_mammal
    
    def info(self):
        print(f"The {self.name} is a {self.habitat} animal. It is {self.behaviour}, a {self.diet}, and can live up to {self.lifespan} years.")
        print(f"It moves at a speed of {self.speed} km/h and makes a sound like '{self.sound}'.")
        print(f"Can it reproduce? {'Yes' if self.can_reproduce else 'No'}. It has {self.number_of_legs} legs and it is {'a mammal' if self.is_mammal else 'not a mammal'}.")
        print("-" * 60)
    
    def make_sound(self):
        print(f"The {self.name} makes a sound like '{self.sound}'.")
    
    def move(self):
        print(f"The {self.name} moves at a speed of {self.speed} km/h.")
    
    def reproduction_status(self):
        print(f"The {self.name} {'can' if self.can_reproduce else 'cannot'} reproduce.")

# Creating unique instances of different animals
lion = Animal("Lion", "Social", "Carnivore", "Savanna", 14, 80, "Roar", True, 4, True)
eagle = Animal("Eagle", "Solitary", "Carnivore", "Mountains", 25, 160, "Screech", True, 2, False)
elephant = Animal("Elephant", "Social", "Herbivore", "Grasslands", 70, 40, "Trumpet", True, 4, True)
dolphin = Animal("Dolphin", "Social", "Carnivore", "Ocean", 50, 60, "Click", True, 0, True)
frog = Animal("Frog", "Solitary", "Omnivore", "Freshwater", 12, 5, "Ribbit", True, 4, False)
cobra = Animal("Cobra", "Solitary", "Carnivore", "Rainforest", 20, 12, "Hiss", True, 0, False)
kangaroo = Animal("Kangaroo", "Social", "Herbivore", "Australian Outback", 23, 70, "Chatter", True, 2, True)
wolf = Animal("Wolf", "Social", "Carnivore", "Forests & Tundra", 16, 60, "Howl", True, 4, True)
butterfly = Animal("Butterfly", "Solitary", "Herbivore", "Gardens & Forests", 1, 10, "Silent", True, 6, False)
penguin = Animal("Penguin", "Social", "Carnivore", "Antarctic Waters", 20, 10, "Honk", True, 2, False)

animals = [lion, eagle, elephant, dolphin, frog, cobra, kangaroo, wolf, butterfly, penguin]

# Displaying information and behaviors for each animal
for animal in animals:
    animal.info()
    animal.make_sound()
    animal.move()
    animal.reproduction_status()
    print()
