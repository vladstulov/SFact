class Cat:
    def _init_(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    from cat import Cats

    cats = [
        {
            "name": "Барон",
            "gender": "Мальчик",
            "age": "2 года",
        }
        ,
        {
            "name": "Сэм",
            "gender": "Мальчик",
            "age": "2 года",

        },
    ]
    for cat in cats
        cat_obj = Cat(name = cat.get("name"),
                      gender = cat.get("gender"),
                      age = cat.get("age"))

    print(cat_obj.name, cat_obj.gender, cat_obJ.age)