class Livre:
    def __init__(self, titre, auteur,isbn, stock:int):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.stock = stock
        self.stock_init = stock

    def __str__(self):
        return self.titre + " " + self.auteur + " " + self.isbn + " " + str(self.stock)
    
    def nombre_total_livre(self):
        return self.stock
    

