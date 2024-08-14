from models.livre import Livre

class LivreNumerique(Livre):
    def __init__(self, titre, auteur, isbn, stock, taille_fichier:int):
        super().__init__(titre, auteur, isbn, stock)
        self.taille_fichier = taille_fichier


    def __str__(self):
        return super().__str__() + " " + str(self.taille_fichier) + " Mo"