from models.livre import Livre


class LivrePapier(Livre):
    def __init__(self, titre, auteur, isbn, stock, nb_pages:int):
        super().__init__(titre, auteur, isbn, stock)
        self.nb_pages = nb_pages

    def __str__(self):
        return super().__str__() + " " + str(self.nb_pages) + " pages"