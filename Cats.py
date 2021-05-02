# file 1: CatsFile.py

class Cats:
    def __init__(self, name, gender, age, home):
        self.name = name
        self.gender = gender
        self.age = age
        self.home = home
        
    
 # file 2: CatsFile_2.py


from CatsFile import Cats

A = Cats("Барон", "Мальчик", 2, False)
B = Cats("Сэм", "Мальчик", 1, False)


print("Мохнатый ублюдок 1: ",(A.name),",",(A.gender), ", Возраст:",(A.age), "лет,",  "Имеет дом = ", (A.home) )
print("Мохнатый ублюдок 2: ",(B.name),",",(B.gender), ", Возраст:",(B.age), "лет,",  "Имеет дом = ", (B.home) )
