import unittest
from unittest import TestCase
from models.bibliotheque import Bibliotheque
from models.livrenumerique import LivreNumerique
from models.livrepapier import LivrePapier

class BibliothequesTest(TestCase):
    
    def setUp(self):
        self.bibliotheque = Bibliotheque()
        self.livrepapier_1 = LivrePapier(titre="Confiance Illimite", auteur="Franck Nicolas", isbn="1236-652-636", stock=20, nb_pages=20)
        self.livrepapier_2 = LivreNumerique(titre="Le pouvoir de la confiance en soi", auteur="Brian Tracy", isbn="1236-652-637", stock=20, taille_fichier=20)
        return super().setUp()
    # Test de la méthode ajouterLivre Numerique
    def test_ajouterLivreNumerique(self):
        self.bibliotheque.ajouterLivre(self.livrepapier_2)
        self.assertIn(self.livrepapier_2, self.bibliotheque.livres)
        self.assertEqual(1, len(self.bibliotheque.livres))
    # Test de la méthode ajouterLivre Papier
    def test_ajouterLivrePapier(self):
        self.bibliotheque.ajouterLivre(self.livrepapier_1)
        self.assertIn(self.livrepapier_1, self.bibliotheque.livres)
        self.assertEqual(1, len(self.bibliotheque.livres))
    # Test de la méthode supprimerLivre
    def test_supprimerLivre(self):
        self.bibliotheque.ajouterLivre(self.livrepapier_1)
        self.bibliotheque.supprimerLivre(self.livrepapier_1)
        self.assertNotIn(self.livrepapier_1, self.bibliotheque.livres)
        self.assertEqual(0, len(self.bibliotheque.livres))
      


if __name__ == '__main__':
    unittest.main()
    





