
class Animal:
    
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        
    def feed(self, kgs):
        self.health = self.health + 10 * kgs
        self.happiness =self.happiness + 10* kgs
    
    def display_info(self):
        print(f'{self.name} tiene {self.age} de edad, tiene {self.health} de salud y {self.happiness} de felicidad ')
    

class Lion(Animal):
    def __init__(self, name, age, health, happiness):

        super().__init__(name, age, health, happiness)



class Tiger(Animal):
    def __init__(self, name, age, health, happiness):

        super().__init__(name, age, health, happiness)
    

class Bear(Animal):
    def __init__(self, name, age, health, happiness,hibernating):
        super().__init__(name, age, health, happiness)
        
    

lion= Animal("King",3,0,0)
lion.feed(6)

tiger =Animal("Sher kang",4,5,5)
tiger.feed(6)

bear = Animal("Grizzly",2,1,1)
bear.feed(2)


class Zoo:

    def __init__(self, zoo_name):
        self.animals=[]
        self.zoo_name=zoo_name

    def add_animal(self, animal):
        self.animals.append(animal)
        return self

    def display_zoo_animals(self):      
        print(f"\n*** En el {self.zoo_name} puedes visitar a los siguientes animales: ***\n")
        for animal in self.animals:
            print(f"* Nombre: {Animal.__name__}, es un {Animal.__class__.__name__} y tiene {Animal.age} años,\n   tiene una salud de: {Animal.health} y es {Animal.happyness} de felicidad")
        return self

# Agrego 2 zoologicos y agrego animales 
zoo1=Zoo("Nogales")
zoo1.add_animal(tiger).add_animal(lion)

zoo2=Zoo("San Frey zoo")
zoo2.add_animal(lion).add_animal(bear).add_animal(tiger)
