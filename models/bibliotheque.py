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
        #check if the book is already in the library
        for l in self.livres:
            if l.isbn == livre.isbn:
                print(f"Livre '{livre.titre}' existe déjà.")
        self.livres.append(livre)
        print(f"Livre '{livre.titre}' ajouté.")

    def suppLivre(self, livre:Livre):
        if livre in self.livres:
            self.livres.remove(livre)
            print(f"Livre '{livre.titre}' supprimé.")
        else:
            print(f"Livre '{livre}' non trouvé.")
    def MiseajourLivre(self, livre:Livre, stock:int):
        if livre in self.livres:
            livre.stock = stock
            print(f"Stock du livre '{livre.titre}' mis à jour.")
        else:
            print(f"Livre '{livre}' non trouvé.")
    def __str__(self) -> str:
        return self._instance.livres
    def afficherLivre(self):
        #print all the books with headings
        print("Titre Auteur ISBN Stock")
        for livre in self.livres:
            print(livre)
    def EmprunterLivre(self, livre:Livre, user:User):
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
        for livre in self.livres:
            if livre.auteur == auteur:
                return livre
    def RechercherLiverParTitre(self, titre:str)->Livre:
        for livre in self.livres:
            if livre.titre == titre:
                return livre
    def RechercherLiverParISBN(self, isbn:str)->Livre:
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
