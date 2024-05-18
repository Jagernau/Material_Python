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
