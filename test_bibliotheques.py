import unittest
from unittest import TestCase
from models.bibliotheque import Bibliotheque
from models.livrenumerique import LivreNumerique
from models.livrepapier import LivrePapier
from models.utilisateur import User

class BibliothequesTest(TestCase):
    
    def setUp(self):
        self.bibliotheque = Bibliotheque()
        self.livrepapier_1 = LivrePapier(titre="Confiance Illimite", auteur="Franck Nicolas", isbn="1236-652-636", stock=20, nb_pages=20)
        self.livrepapier_2 = LivreNumerique(titre="Le pouvoir de la confiance en soi", auteur="Brian Tracy", isbn="1236-652-637", stock=20, taille_fichier=20)
        self.user1 = User(username="sylla", password="1234",type_utilisateur=1)
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
        self.bibliotheque.suppLivre(self.livrepapier_1)
        self.assertNotIn(self.livrepapier_1, self.bibliotheque.livres)
        self.assertEqual(0, len(self.bibliotheque.livres))
    # Test de la methode pour emprunter un livre pour un utilisateur
    def test_emprunterLivre(self):
        self.bibliotheque.ajouterLivre(self.livrepapier_1)
        self.bibliotheque.EmprunterLivre(self.livrepapier_1, self.user1)
        self.assertIn(self.user1.username, self.bibliotheque.emprunts)
        self.assertEqual(1, len(self.bibliotheque.emprunts[self.user1.username]))
    # Test de la methode pour retourner un livre pour un utilisateur
    def test_retournerLivre(self):
        self.bibliotheque.ajouterLivre(self.livrepapier_1)
        self.bibliotheque.EmprunterLivre(self.livrepapier_1, self.user1)
        self.bibliotheque.RetournerLiver(self.livrepapier_1, self.user1)
        self.assertNotIn(self.livrepapier_1, self.bibliotheque.emprunts[self.user1.username])
    # Test de la methode pour Ajouter un Utilisateur dans la bibliotheque
    def test_ajouterUtilisateur(self):
        self.bibliotheque.AjouterUtilisateur(self.user1)
        self.assertIn(self.user1, self.bibliotheque.utilisateurs)
    # Test de la methode pour supprimer un utilisateur
    def test_supprimerUtilisateur(self):
        self.bibliotheque.AjouterUtilisateur(self.user1)
        self.bibliotheque.SupprimerUtilisateur(self.user1)
        self.assertNotIn(self.user1, self.bibliotheque.utilisateurs)
        


if __name__ == '__main__':
    unittest.main()
    





