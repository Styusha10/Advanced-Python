class Animal():
    
    def name(self): return self.name

    def age(self): return self.age

    def __initial__(self, name, age):
        self.name = name
        self.age = age

class Zebra(Animal):
    def species(self): return self.species

    def __initial__(self, name, age, species):
        super().__initial__(name, age)
        self.species = species
        
    def __out__(self):
        print(self.name, self.age, self.species, '\n')
        pass

class Dolphin(Animal):
    def species(self): return self.species

    def __initial__(self, name, age, species):
        super().__initial__(name, age)
        self.species = species
        
    def __out__(self):
        print(self.name, self.age, self.species, '\n')
        pass

if __name__ == "__main__":
    a = Animals('Name', 5)
    z = Zebra('Ricky', 10, 'Zebra')
    d = Dolphin('Elly', 4, 'Dolphin')
    print(a.name(), a.age())
    print(z.name(), z.age(), z.species())
    print(d.name(), d.age(), d.species())
