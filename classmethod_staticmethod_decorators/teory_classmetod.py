"""
classmethod и staticmethod - это специальные декораторы, которые позволяют определять методы в классах с особым поведением. Однако они имеют различия в том, как они обрабатывают аргументы и как они взаимодействуют с экземплярами класса.
"""

"""
1️⃣ classmethod:

-  Декоратор преобразует обычный метод класса в тот, который принимает первым аргументом ссылку на класс (обычно называемый cls).
-  Это означает, что метод classmethod может обращаться к атрибутам и вызывать другие методы класса через ссылку на сам класс, а не через экземпляр класса.
-  Может использоваться, например, для создания альтернативных конструкторов класса или для работы с классовыми переменными.
Пример classmethod: https://www.perplexity.ai/search/classmethod-python-b.iPjE87QPCeHWWwt2RMuw
"""
class MyClass1:
    class_attribute = 123
    
    @classmethod
    def class_method(cls):
        return cls.class_attribute

print(MyClass1.class_method())  # Выведет: 123

"""
Создание объектов класса с помощью classmethod
Классметод может использоваться как фабричный метод для создания объектов класса из других данных:
"""
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2023 - birth_year) # переопределил атрибуты класса принятыми аргументами.
        
person = Person1.from_birth_year('John', 1990)
print(person.name, person.age) # Output: John 33

"""
Доступ к атрибутам класса
Классметоды могут использоваться для доступа и модификации атрибутов класса
"""
class MyClass:
    class_attr = 0
    
    @classmethod
    def increment(cls):
        cls.class_attr += 1
        
MyClass.increment()
print(MyClass.class_attr) # Output: 1

"""
Наследование и переопределение classmethod
Классметоды наследуются дочерними классами и могут быть переопределены:
"""
class Person:
    species = 'Human'
    
    @classmethod
    def get_species(cls):
        return cls.species
        
class Male(Person):
    species = 'Male'
    
print(Person.get_species()) # Output: Human 
print(Male.get_species()) # Output: Male
"""
Оптимизация с помощью classmethod
Классметоды могут использоваться для оптимизации, например, для кэширования результатов дорогостоящих вычислений на уровне класса
"""
class ExpensiveObject:
    cache = {}
    
    def __init__(self, arg):
        self.arg = arg
        
    @classmethod
    def get_or_create(cls, arg):
        if arg not in cls.cache:
            cls.cache[arg] = cls(arg)
        return cls.cache[arg]
        
obj1 = ExpensiveObject.get_or_create(123)
obj2 = ExpensiveObject.get_or_create(123)
print(obj1 is obj2) # True
