from bibliotheque import *
import os
from colorama import Fore, Style, init
init(autoreset=True)

# Fonction pour effacer l'écran (fonctionne sur Windows et Unix)
def effacer_ecran():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fonction pour afficher un titre avec des bordures
def afficher_titre(titre):
    print(f"\n{'=' * 40}")
    print(f"{titre.center(40)}")
    print(f"{'=' * 40}\n")

def afficher_titre(titre):
    print(f"\n{Fore.CYAN}{'=' * 40}")
    print(f"{Fore.CYAN}{titre.center(40)}")
    print(f"{Fore.CYAN}{'=' * 40}\n")

# Fonction principale du menu
def menu_principal():
    gestion_utilisateurs = GestionUtilisateurs('Utilisateurs.json')
    gestion_livres = GestionLivres('Livres.json')
    options = {
        "1": gestion_utilisateurs.ajouter_utilisateur,
        "2": gestion_utilisateurs.supprimer_utilisateur,
        "3": gestion_utilisateurs.lister_utilisateurs,
        "4": gestion_utilisateurs.modifier_utilisateur,
        "5": gestion_utilisateurs.afficher_livres_empruntes,
        "6": gestion_utilisateurs.afficher_historique,
        "7": gestion_utilisateurs.trier_utilisateurs,
        "8": gestion_utilisateurs.recherche_utilisateurs,
        "9": gestion_utilisateurs.importer_donnees,
        "10": gestion_utilisateurs.afficher_utilisateurs_en_retard,
        "11": gestion_utilisateurs.envoyer_notifications_rappel,
        "12": gestion_utilisateurs.afficher_historique_livre,
        "13": gestion_utilisateurs.generer_statistiques,
        "14": gestion_utilisateurs.afficher_livres_populaires,
        "15": gestion_utilisateurs.gestion_administrateurs,
        "16": gestion_utilisateurs.afficher_audit_actions,
        "17": gestion_utilisateurs.sauvegarde_automatique,
        "18": gestion_livres.ajouter_livre,
        "19": gestion_livres.supprimer_livre,
        "20": gestion_livres.lister_livres,
        "21": lambda : gestion_livres.emprunter_livre(Utilisateur),
        "22": lambda : gestion_livres.retourner_livre(Utilisateur),
        "23": gestion_livres.sauvegarder_livres,
        "24": gestion_livres.charger_livres,
        "0": exit
    }

    while True:
        effacer_ecran()
        afficher_titre("Menu Principal")

        print("1. Ajouter un utilisateur")
        print("2. Supprimer un utilisateur")
        print("3. Lister les utilisateurs")
        print("4. Modifier un utilisateur")
        print("5. Afficher les livres empruntés par un utilisateur")
        print("6. Afficher l'historique d'un utilisateur")
        print("7. Trier les utilisateurs")
        print("8. Recherche avancée d’utilisateurs")
        print("9. Importer les données à partir d'un fichier CSV")
        print("10. Afficher les utilisateurs ayant des retards")
        print("11. Envoyer des notifications de rappel")
        print("12. Afficher l'historique d'un livre")
        print("13. Générer des statistiques détaillées")
        print("14. Afficher les livres les plus empruntés")
        print("15. Gestion des administrateurs")
        print("16. Afficher l'audit des actions")
        print("17. Sauvegarde automatique")
        print("18. Ajouter un livre")
        print("19. Supprimer un livre")
        print("20. Lister les livres")
        print("21. Emprunter les livres")
        print("22. Retourner les livres")
        print("23. Sauvegarder les livres")
        print("24. Charger les livres")
        print("0. Quitter")

        choix = input("\nEntrez votre choix : ").strip()

        if choix in options:
            effacer_ecran()
            afficher_titre(f"Option {choix}")
            options[choix]()
            input("\nAppuyez sur Entrée pour continuer...")  # Pause avant de revenir au menu principal
        else:
            print("Choix invalide, veuillez réessayer.")
            input("Appuyez sur Entrée pour continuer...")  # Pause avant de réafficher le menu

if __name__ == "__main__":
    menu_principal()