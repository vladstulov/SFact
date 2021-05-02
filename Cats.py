# file 1: CatsFile.py

class Cats:
    def __init__(self, name, gender, age, home):
        self.name = name
        self.gender = gender
        self.age = age
        self.home = home
    
    def get_param(self):
        print('Мохнатый ублюдок : ', (self.name), ',', (self.gender),', ' 'Возраст:',(self.age), 'лет',', '  "Имеет дом = ", (self.home) )

    
 # file 2: CatsFile_2.py


from CatsFile import Cats

A = Cats("Барон", "Мальчик", 2, False)
B = Cats("Сэм", "Мальчик", 1, False)

A.get_param()
B.get_param()
