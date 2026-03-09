
class Maillon:

    def __init__(self, v):
        self.val = v
        self.suiv = None


class ListeC:

    # liste 
    def __init__(self):
        self.tete = None
    
    # nombre d'élement
    def longueur(self):
        mcour = self.tete
        compteur = 0
        while mcour != None:
            compteur += 1
            mcour = mcour.suiv
        return compteur

    # position
    def ieme(self, i):
        if 1 <= i and i <= self.longueur():
            mcour = self.tete
            j = 1
            while j < i:
                j += 1
                mcour = mcour.suiv
            return mcour.val
        else:
            return None
    
    # supprimer un element à une position 
    def supprimer(self, i):
        if 1 <= i and i <= self.longueur():
            if i == 1:
                self.tete = self.tete.suiv
            else:
                mcour = self.tete
                pred = mcour
                compteur = 1
                while compteur < i:
                    pred = mcour
                    mcour = mcour.suiv
                    compteur += 1
                pred.suiv = mcour.suiv
    
    # inseret un element à une position 
    def inserer(self, i, val):
        mn = Maillon(val)
        if i == 1 and self.longueur() == 0:
            self.tete = mn
        elif i == 1:
            mn.suiv = self.tete
            self.tete = mn
        elif 1 <= i and i <= self.longueur() + 1:
            mcour = self.tete
            pred = mcour
            compteur = 1
            while compteur < i:
                pred = mcour
                mcour = mcour.suiv
                compteur += 1
            pred.suiv = mn
            mn.suiv = mcour
    
    # afficher les elements de la liste
    def affiche(self):
        mcour = self.tete
        while mcour != None:
            print("[", mcour.val, "]-->", end='')
            mcour = mcour.suiv
        print("None")

# class film pour ajouter les films 
class Film:
    def __init__(self,titre,duree,genre,annee):
        self.titre=titre
        self.duree=duree
        self.genre=genre
        self.annee=annee

        
# fonction des genrs
def creer_liste_genres():
    """Crée et retourne une liste contenant tous les genres possibles"""
    genres = ListeC()
    genres.inserer(1, "Comédie")
    genres.inserer(2, "Drame")
    genres.inserer(3, "Comédie dramatique")
    genres.inserer(4, "Thriller")
    genres.inserer(5, "Action")
    genres.inserer(6, "Aventure")
    genres.inserer(7, "Horreur")
    genres.inserer(8, "Science-fiction")
    genres.inserer(9, "Fantastique")
    return genres

# choisire le genre 
def choisir_genre(liste_genres):
    """Affiche les genres, demande à l'utilisateur de choisir et retourne le nom du genre"""
    # Afficher tous les genres
    for i in range(1, liste_genres.longueur() + 1):
        genre = liste_genres.ieme(i)
        print(f"{i}) {genre}")
    
    # Demander le choix à l'utilisateur
    while True:
        try:
            choix = int(input("Entrez le numéro du genre : "))
            if 1 <= choix <= liste_genres.longueur():
                return liste_genres.ieme(choix)
            else:
                print("Numéro invalide. Réessayez.")
        except:
            print("Veuillez entrer un nombre valide.")

# enregistrer un film
def saisir_film(stock_films, liste_genres):
    print("\n--- Saisie d'un nouveau film ---")
    
    titre = input("Entrez le titre du film : ")
    
    while True:
        try:
            duree = int(input("Entrez la durée du film (en minutes) : "))
            if duree > 0:
                break
            else:
                print("La durée doit être positive.")
        except:
            print("Veuillez entrer un nombre valide.")
    
    genre = choisir_genre(liste_genres)
    
    while True:
        try:
            annee = int(input("Entrez l'année de parution du film : "))
            if 1800 <= annee <= 2030: 
                break
            else:
                print("Année invalide.")
        except:
            print("Veuillez entrer une année valide.")
    
    nouveau_film = Film(titre, duree, genre, annee)
    stock_films.inserer(stock_films.longueur() + 1, nouveau_film)
    print("\nFilm ajouté avec succès !")

# Afficher la liste des films, titre uniquement 
def afficher_titres(stock_films):
    if stock_films.longueur() == 0:
        print("\nAucun film dans le stock.")
    else:
        print("\n--- Liste des films (titres uniquement) ---")
        for i in range(1, stock_films.longueur() + 1):
            film = stock_films.ieme(i)
            print(f"{i}. {film.titre}")

# suprimer un titre à partire de son titre 
def supprimer_film_par_titre(stock_films):
    if stock_films.longueur() == 0:
        print("\nAucun film à supprimer.")
        return
    
    titre_recherche = input("\nEntrez le titre du film à supprimer : ")
    
    trouve = False
    for i in range(1, stock_films.longueur() + 1):
        film = stock_films.ieme(i)
        if film.titre.lower() == titre_recherche.lower():
            stock_films.supprimer(i)
            print(f"Le film '{titre_recherche}' a été supprimé.")
            trouve = True
            break
    
    if not trouve:
        print(f"Aucun film trouvé avec le titre '{titre_recherche}'.")

# vide du stock de filme
def vider_stock(stock_films):
    if stock_films.longueur() == 0:
        print("\nLe stock est déjà vide.")
        return
    
    confirmation = input("\nÊtes-vous sûr de vouloir supprimer TOUS les films ? (oui/non) : ")
    if confirmation.lower() == "oui":
        # Supprimer tous les films un par un
        while stock_films.longueur() > 0:
            stock_films.supprimer(1)
        print("Tous les films ont été supprimés.")
    else:
        print("Opération annulée.")

# Modifier les informations relatives à un film dont le titre a été renseigné
def modifier_film(stock_films, liste_genres):
    """Modifie les informations d'un film"""
    if stock_films.longueur() == 0:
        print("\nAucun film à modifier.")
        return
    
    titre_recherche = input("\nEntrez le titre du film à modifier : ")
    

    trouve = False
    for i in range(1, stock_films.longueur() + 1):
        film = stock_films.ieme(i)
        if film.titre.lower() == titre_recherche.lower():
            trouve = True
            print(f"\nFilm trouvé : {film}")
            print("\n--- Saisie des nouvelles informations ---")
      
            nouveau_titre = input("Nouveau titre (laisser vide pour conserver) : ")
            if nouveau_titre != "":
                film.titre = nouveau_titre
            
            duree_str = input("Nouvelle durée en minutes (laisser vide pour conserver) : ")
            if duree_str != "":
                try:
                    film.duree = int(duree_str)
                except:
                    print("Durée invalide, conservation de l'ancienne valeur.")
            
            changer_genre = input("Changer le genre ? (oui/non) : ")
            if changer_genre.lower() == "oui":
                film.genre = choisir_genre(liste_genres)
            
            annee_str = input("Nouvelle année (laisser vide pour conserver) : ")
            if annee_str != "":
                try:
                    film.annee = int(annee_str)
                except:
                    print("Année invalide, conservation de l'ancienne valeur.")
            
            print("\nFilm modifié avec succès !")
            break
    
    if not trouve:
        print(f"Aucun film trouvé avec le titre '{titre_recherche}'.")

# Rechercher et afficher les caractéristiques de tous les films d’une durée supérieure à 60 minutes
def rechercher_par_duree(stock_films):
    print("\n--- Films de plus de 60 minutes ---")
    
    trouve = False
    for i in range(1, stock_films.longueur() + 1):
        film = stock_films.ieme(i)
        if film.duree > 60:
            print(film)
            trouve = True
    
    if not trouve:
        print("Aucun film de plus de 60 minutes.")

# Rechercher et afficher les caractéristiques de tous les films appartenant à un genre spécifique
def rechercher_par_genre(stock_films, liste_genres):
    print("\n--- Recherche par genre ---")
    genre_recherche = choisir_genre(liste_genres)
    
    print(f"\n--- Films du genre '{genre_recherche}' ---")
    trouve = False
    for i in range(1, stock_films.longueur() + 1):
        film = stock_films.ieme(i)
        if film.genre == genre_recherche:
            print(film)
            trouve = True
    
    if not trouve:
        print(f"Aucun film du genre '{genre_recherche}'.")

#  Rechercher et afficher les caractéristiques de tous les films produits lors d’une année donnée
def rechercher_par_annee(stock_films):
    try:
        annee_recherche = int(input("\nEntrez l'année de production : "))
        
        print(f"\n--- Films produits en {annee_recherche} ---")
        trouve = False
        for i in range(1, stock_films.longueur() + 1):
            film = stock_films.ieme(i)
            if film.annee == annee_recherche:
                print(film)
                trouve = True
        
        if not trouve:
            print(f"Aucun film produit en {annee_recherche}.")
    except:
        print("Année invalide.")


# menu
def afficher_menu():
    print("\n-------- MENU --------")
    print("1) Saisir un film")
    print("2) Afficher la liste des films (uniquement les titres)")
    print("3) Supprimer un film")
    print("4) Supprimer tous les films")
    print("5) Modifier un film")
    print("6) Rechercher les films de plus de 60 minutes")
    print("7) Rechercher par genre")
    print("8) Rechercher par année")
    print("9) Quitter")


#  Quitter l'application

def main():
    stock_films = ListeC() 
    liste_genres = creer_liste_genres() 
    
    print("===========================================")
    print("  Bienvenue dans le gestionnaire de cinéma")
    print("===========================================")
    
    # Boucle principale
    continuer = True
    while continuer:
        afficher_menu()
        
        try:
            choix = int(input("\nEntrez votre choix : "))
            
            if choix == 1:
                saisir_film(stock_films, liste_genres)
            elif choix == 2:
                afficher_titres_films(stock_films)
            elif choix == 3:
                supprimer_film_par_titre(stock_films)
            elif choix == 4:
                vider_stock(stock_films)
            elif choix == 5:
                modifier_film(stock_films, liste_genres)
            elif choix == 6:
                rechercher_par_duree(stock_films)
            elif choix == 7:
                rechercher_par_genre(stock_films, liste_genres)
            elif choix == 8:
                rechercher_par_annee(stock_films)
            elif choix == 9:
                print("\nMerci d'avoir utilisé le gestionnaire de cinéma. Au revoir !")
                continuer = False
            else:
                print("\nChoix invalide. Veuillez choisir un numéro entre 1 et 9.")
        
        except ValueError:
            print("\nErreur : veuillez entrer un nombre valide.")
        except Exception as e:
            print(f"\nErreur inattendue : {e}")


# ===== LANCEMENT DU PROGRAMME =====

if __name__ == "__main__":
    main()
