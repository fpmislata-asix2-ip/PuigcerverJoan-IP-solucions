class Plant:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    def __str__(self):
        return f"Plant(health={self.health}, attack={self.attack})"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.health < other.health

    def __eq__(self, other):
        return self.health == other.health \
            and self.attack == other.attack

    def __add__(self, other):
        health = self.health + other.health
        attack = self.attack + other.attack
        return Plant(health, attack)

    def __and__(self, other):
        health = min(self.health, other.health)
        attack = min(self.attack,  other.attack)
        return Plant(health, attack)


if __name__ == '__main__':
    p1 = Plant(100, 20)
    p2 = Plant(300, 15)
    p3 = Plant(150, 10)
    l = [p1, p2, p3]

    print(p1)
    print(p2)
    print("p1 < p2?", p1 < p2) # p1.__lt__(p2)
    print("p1 == p2?", p1 == p2) # p1.__eq__(p2)
    print(sorted(l, reverse=True)) # Utilitzen l'operador '<' per ordenar

    print("p1 & p2 ->", p1 & p2)
    print("p1 + p2 ->", p1 + p2)