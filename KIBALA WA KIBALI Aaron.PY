import json
import csv
import smtplib
from datetime import datetime, timedelta

# Classe représentant un utilisateur
class Utilisateur:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.livres_empruntes = []
        self.historique_emprunts = []

    def __str__(self):
        return f"{self.nom} ({self.email})"

    def to_dict(self):
        return {
            "nom": self.nom,
            "email": self.email,
            "livres_empruntes": self.livres_empruntes,
            "historique_emprunts": self.historique_emprunts
        }

    @classmethod
    def from_dict(cls, data):
        utilisateur = cls(data["nom"], data["email"])
        utilisateur.livres_empruntes = data["livres_empruntes"]
        utilisateur.historique_emprunts = data["historique_emprunts"]
        return utilisateur

# Classe représentant un livre
class Livre:
    def __init__(self, id, titre, auteur, genre, disponible=True):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.disponible = disponible

    def __str__(self):
        return f"{self.titre} par {self.auteur} ({'Disponible' if self.disponible else 'Indisponible'})"

    def to_dict(self):
        return {
            "id": self.id,
            "titre": self.titre,
            "auteur": self.auteur,
            "genre": self.genre,
            "disponible": self.disponible
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["titre"], data["auteur"], data["genre"], data["disponible"])

 # Ajout d'un utilisateur
    def ajouter_utilisateur(self):
        nom = input("Entrez le nom de l'utilisateur : ")
        email = input("Entrez l'email de l'utilisateur : ")
        self.utilisateurs.append(Utilisateur(nom, email))
        self.sauvegarder_utilisateurs()
        print(f"Utilisateur {nom} ajouté avec succès.")

    # Suppression d'un utilisateur
    def supprimer_utilisateur(self):
        email = input("Entrez l'email de l'utilisateur à supprimer : ")
        self.utilisateurs = [u for u in self.utilisateurs if u.email != email]
        self.sauvegarder_utilisateurs()
        print(f"Utilisateur avec l'email {email} supprimé avec succès.")

    # Liste des utilisateurs
    def lister_utilisateurs(self):
        for utilisateur in self.utilisateurs:
            print(utilisateur)

# Classe de gestion des utilisateurs
class GestionUtilisateurs:
    def __init__(self, fichier_json):
        self.fichier_json = fichier_json
        self.utilisateurs = self.charger_utilisateurs()

# Affichage des utilisateurs ayant des retards dans le retour des livres
    def afficher_utilisateurs_en_retard(self):
        date_actuelle = datetime.now().date()
        for utilisateur in self.utilisateurs:
            retards = [livre for livre in utilisateur.livres_empruntes if livre['date_retour'] < date_actuelle]
            if retards:
                print(f"Utilisateur {utilisateur.nom} a des retards: {retards}")

    # Envoi de notifications de rappel aux utilisateurs ayant des retards
    def envoyer_notifications_rappel(self):
        # Implémenter l'envoi d'emails ou SMS
        for utilisateur in self.utilisateurs:
            date_actuelle = datetime.now().date()
            retards = [livre for livre in utilisateur.livres_empruntes if livre['date_retour'] < date_actuelle]
            if retards:
                self.envoyer_email(utilisateur.email, "Rappel de retour de livre", f"Vous avez des livres en retard : {retards}")

    # Envoi d'un email
    def envoyer_email(self, to_email, subject, message):
        # Configurer le serveur SMTP et envoyer l'email
        print(f"Envoi d'un email à {to_email} avec le sujet '{subject}' et le message '{message}'")

    # Affichage de l'historique d'un livre
    def afficher_historique_livre(self):
        # Implémenter l'affichage de l'historique d'un livre
        titre = input("Entrez le titre du livre : ")
        historique = []
        for utilisateur in self.utilisateurs:
            for emprunt in utilisateur.historique_emprunts:
                if emprunt['titre'] == titre:
                    historique.append((utilisateur.nom, emprunt))
        print(f"Historique pour le livre '{titre}': {historique}")

    # Génération des statistiques détaillées
    def generer_statistiques(self):
        # Générer des statistiques détaillées
        stats = {
            "total_utilisateurs": len(self.utilisateurs),
            "total_livres_empruntes": sum(len(u.livres_empruntes) for u in self.utilisateurs),
            "total_emprunts": sum(len(u.historique_emprunts) for u in self.utilisateurs)
        }
        print(f"Statistiques détaillées : {stats}")

    # Affichage des livres les plus empruntés
    def afficher_livres_populaires(self):
        # Afficher les livres les plus empruntés
        popularite = {}
        for utilisateur in self.utilisateurs:
            for emprunt in utilisateur.historique_emprunts:
                titre = emprunt['titre']
                if titre not in popularite:
                    popularite[titre] = 0
                popularite[titre] += 1
        livres_populaires = sorted(popularite.items(), key=lambda x: x[1], reverse=True)
        print(f"Livres les plus populaires : {livres_populaires}")