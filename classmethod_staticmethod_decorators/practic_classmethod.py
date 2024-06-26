from datetime import datetime as dt

""" 
Классметод:
"""
"1-дополнение атрибута"
class Cat:
    "Класс Кошка"
    sey: str = ""

    @classmethod
    def appoints_sey(cls):
        cls.sey = "Мяу"

cat = Cat()
print(f"без назначения классметодом: {cat.sey}")
cat.appoints_sey()
print(f"после назначения классметодом: {cat.sey}")

"2-отдача атрибутов"
class Dog:
    "Класс Собака"
    __sey: str = "Гав"

    @classmethod
    def get_sey(cls):
        return cls.__sey

print(f"отдача атрибута с помощью классметода: {Dog.get_sey()}")

"3-переназначение атрибутов"
class Person:
    def __init__(self, name, age):
        self.name: str = name
        self.age: int = age

    @classmethod
    def calculate_age(cls, name, birth):
        curent_year = dt.now().year
        return cls(name, int(curent_year) - birth)

person = Person.calculate_age("Максим", 1988)
print(f"Имя: {person.name}, Возраст: {person.age}")

"4-наследственность"
class Family:
    family_skills = ["Рисование",]

    @classmethod
    def add_skill(cls, skil):
        cls.family_skills.append(skil)

class Masha(Family):
    gender = "Female"
    name = "Маша"

masha = Masha()
masha.add_skill("Танцы")
print(f"{masha.name}{masha.family_skills}")

