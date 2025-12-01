class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, sóc {self.name} i tinc {self.age} anys.")

    def is_adult(self):
        return self.age >= 18

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


if __name__ == "__main__":
    person = Person("Pep", 30)
    person.greet()
    print("És major d'edat?", person.is_adult())
    print(person)