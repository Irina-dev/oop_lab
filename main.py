from math import gcd
class Rational(object):
    def __init__(self, nom, denom):
        self.nom = nom
        self.denom = denom

    def rational(self):
        nod = gcd(self.nom, self.denom)
        if nod != 0:
            self.nom = self.nom//nod
            self.denom = self.denom // nod
        return str(self.nom) + '/' + str(self.denom)


    def decimal(self):
        return self.nom/self.denom


if __name__ == "__main__":
    frac = Rational(2, 3)
    print(frac.rational())
    print(frac.decimal())

