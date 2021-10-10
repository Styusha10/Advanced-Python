class Mother():
    def __str__(self): return 'This is Mother'

class Daughter(Mother): def __str__(self): return 'This is Daughter'

if __name == "__main__":
    print(Mother())
    print(Daughter())
