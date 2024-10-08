from models.livre import Livre
from models.utilisateur import User

class Bibliotheque:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Bibliotheque, cls).__new__(cls)
            cls._instance.livres = []
            cls._instance.utilisateurs = []
            cls._instance.emprunts = {}
        return cls._instance
    

    def ajouterLivre(self, livre:Livre):
        """Fonction Pour Ajouter un Livre dans la Bibliotheque

        Args:
            livre (Livre): Un livre numerique ou papier 
        returns:
        Affiche un message si le livre est ajouté ou non
        """
        #check if the book is already in the library
        for l in self.livres:
            if l.isbn == livre.isbn:
                print(f"Livre '{livre.titre}' existe déjà.")
        self.livres.append(livre)
        print(f"Livre '{livre.titre}' ajouté.")

    def suppLivre(self, livre:Livre):
        """Fonction pour supprimer un livre de la bibliotheque

        Args:
            livre (Livre): Un livre numerique ou papier
        returns:
        Affiche un message si le livre est supprimé ou non
        """
        if livre in self.livres:
            self.livres.remove(livre)
            print(f"Livre '{livre.titre}' supprimé.")
        else:
            print(f"Livre '{livre}' non trouvé.")
    def MiseajourLivre(self, livre:Livre, stock:int):
        """Fonction pour mettre à jour le stock d'un livre

        Args:
            livre (Livre): Un livre numerique ou papier
            stock (int): Nouveau stock du livre
        returns:
        Affiche un message si le stock du livre est mis à jour ou non
        """
        if livre in self.livres:
            livre.stock = stock
            print(f"Stock du livre '{livre.titre}' mis à jour.")
        else:
            print(f"Livre '{livre}' non trouvé.")
    def __str__(self) -> str:
        return self._instance.livres
    def afficherLivre(self):
        #print all the books with headings
        #print("Titre Auteur ISBN Stock")
        for index, livre in enumerate(self.livres, start=1):
            print(f"{index}. {livre}")
                
    def EmprunterLivre(self, livre:Livre, user:User):
        """Fonction pour emprunter un livre

        Args:
            livre (Livre): un livre numerique ou papier
            user (User): un utilisateur
        returns:
        Affiche un message si le livre est emprunté ou non par l'utilisateur
        """
        if livre is not None and user is not None:
            if (livre in self.livres) and (int(livre.stock) > 0):
                if user.username not in self.emprunts:
                    self.emprunts[user.username] = []
                    self.emprunts[user.username].append(livre)
                    livre_stock_int = int(livre.stock)
                    livre_stock_int-= 1
                    livre.stock = str(livre_stock_int)
                    print(f"Utilisateur {user.username} a emprunte le Livre '{livre.titre}'.")
                elif user.username in self.emprunts:
                    if livre not in self.emprunts[user.username]:
                        self.emprunts[user.username].append(livre)
                        livre_stock_int = int(livre.stock)
                        livre_stock_int-= 1
                        livre.stock = str(livre_stock_int)
                        print(f"Utilisateur {user.username} a emprunte le Livre '{livre.titre}' emprunté.")
                    else:
                        print(f"Utilisateur {user.username} a deja emprunter ce livre.")
                else:
                    print(f"Stock du livre '{livre.titre}' épuisé.")
            else:
                print(f"Livre '{livre}' non trouvé.")
        else:
         print("Veuillez Creer un Utilisateur ou Ajouter un Livre")
    def RetournerLiver(self, livre:Livre, user:User):
        """ Fonction pour retourner un livre emprunté

        Args:
            livre (Livre): Un livre numerique ou papier
            user (User): Un utilisateur
        returns:
        Affiche un message si le livre est retourné ou non par l'utilisateur
        """
        if user.username in self.emprunts:
            if livre in self.emprunts[user.username]:
                self.emprunts[user.username].remove(livre)
                livre_stock_int = int(livre.stock)
                livre_stock_int+= 1
                livre.stock = str(livre_stock_int)
                print(f"Utilisateur {user.username} a retourné le Livre '{livre.titre}'")
            else:
                print(f"Utilisateur {user.username} n'a pas emprunté ce livre.")
        else:
            print(f"Utilisateur {user.username} n'a pas emprunté de livre.")
    def RechercherLiverParAuteur(self, auteur:str)->Livre:
        """Fonction pour rechercher un livre par auteur

        Args:
            auteur (str): Nom de l'auteur

        Returns:
            Livre: Livre trouvé
        """
        for livre in self.livres:
            if livre.auteur == auteur:
                return livre
    def RechercherLiverParTitre(self, titre:str)->Livre:
        """Fonction pour rechercher un livre par titre

        Args:
            titre (str): Titre du livre

        Returns:
            Livre: Livre trouvé
        """
        for livre in self.livres:
            if livre.titre == titre:
                return livre
    def RechercherLiverParISBN(self, isbn:str)->Livre:
        """Fonction pour rechercher un livre par ISBN

        Args:
            isbn (str): ISBN du livre

        Returns:
            Livre: Livre trouvé
        """
        for livre in self.livres:
            if livre.isbn == isbn:
                return livre
    #Nombre Total de livres disponible dans la bibliotheque
    def NombreTotalLivre(self)->int:
        total = 0
        for livre in self.livres:
            total += int(livre.stock)
        return total
    #Nombre Total de livres empruntés
    def NombreTotalLivreEmpruntes(self)->int:
        total = 0   
        for username in self.emprunts:
            total += len(self.emprunts[username])
        return total
    #Nombre Total d'Utilisateurs
    def NombreTotalUtilisateurs(self)->int:
        return len(self.utilisateurs)
#partie Getion des utilisateurs
    def AjouterUtilisateur(self, user:User):
        self.utilisateurs.append(user)
        print(f"Utilisateur '{user.username}' ajouté.")
    def SupprimerUtilisateur(self, user:User):
        if user in self.utilisateurs:
            self.utilisateurs.remove(user)
            print(f"Utilisateur '{user.username}' supprimé.")
        else:
            print(f"Utilisateur '{user.username}' non trouvé.")
    def RechercherUtilisateurParUsername(self,username:str)->User:
        for user in self.utilisateurs:
            if user.username == username:
                return user
    def ListeUtilisateurs(self):
        for user in self.utilisateurs:
            print(user)
