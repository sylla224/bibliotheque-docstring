class Livre:
    """Classe Principale Livre
    Args:
        titre (str): Titre du livre
        auteur (str): Auteur du livre
        isbn (str): ISBN du livre
        stock (int): Stock du livre
    return:
        str: titre auteur isbn stock

    """
    def __init__(self, titre, auteur,isbn, stock:int):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.stock = stock
        self.stock_init = stock

    def __str__(self):
        return self.titre + ", " + self.auteur + ", " + self.isbn + ", " + str(self.stock)
    
    def nombre_total_livre(self):
        return self.stock
    

