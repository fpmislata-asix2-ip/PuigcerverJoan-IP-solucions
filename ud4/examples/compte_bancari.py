class CompteBancari:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo
        self.locked = False

    def ingresar(self, quantitat):
        if quantitat > 0:
            self.__saldo += quantitat

    def retirar(self, quantitat):
        if quantitat > 0 and quantitat <= self.__saldo:
            self.__saldo -= quantitat
            return True
        return False

    def __str__(self):
        return f"CompteBancari(titular={self.titular}, saldo={self.__saldo})"



if __name__ == "__main__":
    compte = CompteBancari('Anna', 100)
    print(compte)
    compte.ingresar(50)
    print(compte)
    retirat = compte.retirar(100)
    print(f"s'ha retirat 100 euros? {retirat}")
    print(compte)
    retirat = compte.retirar(100)
    print(f"s'ha retirat 100 euros? {retirat}")
    print(compte)