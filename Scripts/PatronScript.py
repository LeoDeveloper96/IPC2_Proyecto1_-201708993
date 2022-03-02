class Patron:
    def __init__(self, cod, patron):
        self.cod = cod
        self.patron = patron

    def setCod(self, cod):
        self.cod = cod

    def getCod(self):
        return self.cod

    def setPatron(self, patron):
        self.patron = patron

    def getPatron(self):
        return self.patron
