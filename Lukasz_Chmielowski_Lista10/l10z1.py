#£ukasz Chmielowski gr 1 zad 1 lista 10
class Kolo:

    def __init__(self, promien):
        self.r = promien

    def obwod(self):
        return self.r * 2 * 3.14

    def pole(self):
        return 3.14 * self.r * self.r


a = Kolo(10)
print(a.obwod())
print(a.pole())

