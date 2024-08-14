from models.livrenumerique import LivreNumerique
from models.livrepapier import LivrePapier
from models.bibliotheque import Bibliotheque
from models.utilisateur import User
import typer

app = typer.Typer()

livre1 = LivreNumerique("Les Misérables", "Victor Hugo", "978-2-253-09861-3", 5, 3)
livre2 = LivrePapier("Les Misérables Nouveau", "Victor Hugo", "978-2-253-09861-3", 1488, 3)
biblio = Bibliotheque()

def main():
    while True:
    #Menu de l'application
        typer.echo("-----------------Menu-----------------")
        typer.echo("Bienvenue dans la bibliotheque")
        typer.echo("1. Ajouter un livre")
        typer.echo("2. Supprimer un livre")
        typer.echo("3. Rechercher un livre")
        typer.echo("4. Ajouter un utilisateur")
        typer.echo("5. Emprunter un livre")
        typer.echo("6. Retourner un livre")
        typer.echo("7. Lister les livres")
        typer.echo("8. Statistiques")
        typer.echo("9. Quitter")
        #Creation d'un utilisateur
        #typer.echo("Creation d'un utilisateur")
        #List des menu de la Bibliotheque
        #------------------------Menu Livre------------------------#
        def menu_livre():
                while True:
                    typer.echo("1. Livre Numerique")
                    typer.echo("2. Livre Papier")
                    typer.echo("3. Retour")
                    choix_livre = typer.prompt("Entrez votre choix de livre")
                    if choix_livre == "1":
                        titre = typer.prompt("Entrez le titre")
                        auteur = typer.prompt("Entrez l'auteur")
                        isbn = typer.prompt("Entrez l'isbn")
                        taille_fichier = typer.prompt("Entrez la taille du fichier")
                        stock = typer.prompt("Entrez le stock")
                        livre = LivreNumerique(titre=titre, auteur=auteur, isbn=isbn, taille_fichier=taille_fichier, stock=stock)
                        biblio.ajouterLivre(livre)
                    elif choix_livre == "2":
                        titre = typer.prompt("Entrez le titre")
                        auteur = typer.prompt("Entrez l'auteur")
                        isbn = typer.prompt("Entrez l'isbn")
                        nb_pages = typer.prompt("Entrez le nombre de pages")
                        stock = typer.prompt("Entrez le stock")
                        livre = LivrePapier(titre=titre, auteur=auteur, isbn=isbn, nb_pages=nb_pages, stock=stock)
                        biblio.ajouterLivre(livre)
                    elif choix_livre == "3":
                        break
                    else:
                        typer.echo("Veuillez saisir un nombre du menu")
                """ typer.echo("1. Livre Numerique")
                typer.echo("2. Livre Papier")
                typer.echo("3. Retour") """
                # choix_livre = typer.prompt("Entrez votre choix")
        #------------------------Fin Menu Livre------------------------#
        #----------------------- Menu Supprimer Livre------------------------#
        def menu_supprimer_livre():
                isbn_sup = typer.prompt("Entrez l'ISBN du livre à supprimer")
                for livre in biblio.livres:
                    if livre.isbn == isbn_sup:
                        biblio.suppLivre(livre)
                        break
                else:
                    typer.echo(f"Le Livre avec ISBN '{isbn_sup}' non trouvé.")
        #----------------------- Fin Menu Supprimer Livre------------------------#
        #----------------------- Menu Rechercher Livre------------------------#
        def menu_rechercher_livre():
                while True:
                #menu de recherche
                    typer.echo("1. Rechercher par titre")
                    typer.echo("2. Rechercher par ISBN")
                    typer.echo("3. Retour")
                    choix_recherche = typer.prompt("Entrez votre choix de recherche")
                    if choix_recherche == "1":
                        titre_recherche = typer.prompt("Entrez le titre du livre")
                        for livre in biblio.livres:
                            if livre.titre == titre_recherche:
                                typer.echo(livre)
                                break
                        else:
                            typer.echo(f"Le Livre avec titre '{titre_recherche}' non trouvé.")
                    elif choix_recherche == "2":
                        isbn_recherche = typer.prompt("Entrez l'ISBN du livre")
                        for livre in biblio.livres:
                            if livre.isbn == isbn_recherche:
                                typer.echo(livre)
                                break
                        else:
                            typer.echo(f"Le Livre avec ISBN '{isbn_recherche}' non trouvé.")
                    elif choix_recherche == "3":
                        break
        #----------------------- Fin Menu Rechercher Livre------------------------#
        #----------------------- Menu Ajouter Utilisateur------------------------#
        def menu_ajouter_utilisateur():
                typer.echo("Creation d'un utilisateur")
                username = typer.prompt("Entrez le nom d'utilisateur")
                password_user= typer.prompt("Entrez le mot de passe")
                type_user= typer.prompt("Entrez le type d'utilisateur 0 ou 1")
                type_user= int(type_user)
                if type_user in [0, 1]:
                    biblio.AjouterUtilisateur(User(username=username, password=password_user, type_utilisateur=type_user))
                else:
                    typer.echo("Type d'utilisateur non valide")
        #----------------------- Fin Menu Ajouter Utilisateur------------------------#
        #----------------------- Menu Emprunter Livre------------------------#
        def menu_emprunter_livre():
                typer.echo("Emprunter un livre")
                username = typer.prompt("Entrez le nom d'utilisateur")
                isbn_livre= typer.prompt("Entrez l'ISBN du livre")
                user=biblio.RechercherUtilisateurParUsername(username)
                if user.type_utilisateur==0:
                     biblio.EmprunterLivre(livre=biblio.RechercherLiverParISBN(isbn_livre), user=user)
                else:
                     print(f"{user.username} n'est pas autoriser a faire des emprunts de livre")
                     
                
        #----------------------- Fin Menu Emprunter Livre------------------------#
        #----------------------- Menu Retourner Livre------------------------#
        def menu_retourner_livre():
                typer.echo("Retourner un livre")
                username=typer.prompt("Entrez le nom d'utilisateur")
                isbn_livre=  typer.prompt("Entrez l'ISBN du livre")
                biblio.RetournerLiver(livre=biblio.RechercherLiverParISBN(isbn_livre), user=biblio.RechercherUtilisateurParUsername(username))
        #----------------------- Fin Menu Retourner Livre------------------------#
        #----------------------- Menu Afficher Livres------------------------#
        def menu_afficher_livres():
                typer.echo("Liste des livres disponibles")
                biblio.afficherLivre()
        #----------------------- Fin Menu Afficher Livres------------------------#
        #----------------------- Menu Statistiques------------------------#
        def menu_statistiques():
                while True:
                    typer.echo("Statistiques De la bibliotheque")
                    typer.echo("1. Nombre total de livres disponibles")
                    typer.echo("2. Nombre total de livres empruntés")
                    typer.echo("3. Nombre total d'utilisateurs")
                    typer.echo("4. Les livres les plus empruntés")
                    typer.echo("5. Liste des Utilisateurs")
                    typer.echo("6. Retourner au menu")
                    choix_stat = typer.prompt("Entrez votre choix")
                    if choix_stat == "1":
                        typer.echo(f"Nombre total de livres disponibles: {biblio.NombreTotalLivre()}")
                    elif choix_stat == "2":
                        typer.echo(f"Nombre total de livres empruntés: {biblio.NombreTotalLivreEmpruntes()}")
                    elif choix_stat == "3":
                        typer.echo(f"Nombre total d'utilisateurs: {biblio.NombreTotalUtilisateurs()}")
                    elif choix_stat == "4":
                        typer.echo("Les livres les plus empruntés")
                        for key, value in biblio.emprunts.items():
                            typer.echo(f"{key}: {[livre.titre for livre in value]}")
                    elif choix_stat == "5":
                        typer.echo("Liste des Utilisateurs")
                        biblio.ListeUtilisateurs()
                    elif choix_stat == "6":
                        break
        #----------------------- Fin Menu Statistiques------------------------#
        #------------------------Menu Principal------------------------#
        choix = typer.prompt("Entrez votre choix de menu")
        if choix == "1":
            menu_livre()
        elif choix == "2":
            menu_supprimer_livre()
        elif choix == "3": 
            menu_rechercher_livre()
        elif choix == "4":
            menu_ajouter_utilisateur()
        elif choix=="5":
            #verifier si il exist un utilisateur et un livre
            if len(biblio.utilisateurs) == 0 or len(biblio.livres) == 0:
                typer.echo("Veuillez Creer un Utilisateur ou Ajouter un Livre")
            else:
             menu_emprunter_livre()
        elif choix == "6":
            menu_retourner_livre()
        elif choix == "7": 
            menu_afficher_livres()
        elif choix=="8":  
            menu_statistiques()       
        elif choix == "9":
            break
        
    """ username = input("username")
    password = input("password")
    user_to_create = User(username=username, password=password)
    print(user_to_create)
    #Emprunter un livre
    
    biblio.AjouterUtilisateur(user_to_create)
    biblio.ajouterLivre(livre1)
    biblio.ajouterLivre(livre2)
    biblio.EmprunterLivre(livre=livre1, user=user_to_create)
    biblio.EmprunterLivre(livre=livre2, user=user_to_create)
    print(livre1.stock)
    for livre in biblio.livres:
        print(livre)
    print(biblio.utilisateurs)
    for key, value in biblio.emprunts.items():
        print(key, [livre.titre for livre in value])
    #Retourner un livre
    biblio.RetournerLiver(livre=livre1,user=user_to_create)
    for key, value in biblio.emprunts.items():
        print(key, [livre.titre for livre in value])
    readline_new = input("") """
    
#user1=User("sylla", "password1")
#user2 = User("sylla", "password2")
#creation d'un super utilisateur
super_user = User(username="admin", password="123", type_utilisateur=1)  

if __name__ == "__main__":
    biblio.AjouterUtilisateur(super_user)
    typer.run(main)
   




   # typer.echo("Hello World")
   # print(user1)
   # print(user2)
   # biblio = Bibliotheque()
   # biblio.ajouterLivre(livre1)
   # biblio.ajouterLivre(livre2)
   # biblio.afficherLivre()





