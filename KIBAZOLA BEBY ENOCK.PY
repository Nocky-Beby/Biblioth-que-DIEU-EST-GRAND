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


def modifier_utilisateur(self):
        email = input("Entrez l'email de l'utilisateur à modifier : ")
        for utilisateur in self.utilisateurs:
            if utilisateur.email == email:
                nouveau_nom = input("Entrez le nouveau nom (laissez vide pour ne pas changer) : ")
                nouveau_email = input("Entrez le nouvel email (laissez vide pour ne pas changer) : ")
                if nouveau_nom:
                    utilisateur.nom = nouveau_nom
                if nouveau_email:
                    utilisateur.email = nouveau_email
                self.sauvegarder_utilisateurs()
                print(f"Informations de l'utilisateur {email} modifiées avec succès.")
                return
        print(f"Utilisateur avec l'email {email} non trouvé.")
 # Affichage des livres empruntés par un utilisateur
    def afficher_livres_empruntes(self):
        email = input("Entrez l'email de l'utilisateur : ")
        for utilisateur in self.utilisateurs:
            if utilisateur.email == email:
                print(f"Livres empruntés par {utilisateur.nom}: {utilisateur.livres_empruntes}")
                return
        print(f"Utilisateur avec l'email {email} non trouvé.")

    # Affichage de l'historique des emprunts d'un utilisateur
    def afficher_historique(self):
        email = input("Entrez l'email de l'utilisateur : ")
        for utilisateur in self.utilisateurs:
            if utilisateur.email == email:
                print(f"Historique des emprunts de {utilisateur.nom}: {utilisateur.historique_emprunts}")
                return
        print(f"Utilisateur avec l'email {email} non trouvé.")

# Classe de gestion des utilisateurs
class GestionUtilisateurs:
    def __init__(self, fichier_json):
        self.fichier_json = fichier_json
        self.utilisateurs = self.charger_utilisateurs()
# Gestion des administrateurs
    def gestion_administrateurs(self):
        # Gestion des administrateurs
        print("Fonctionnalité de gestion des administrateurs en cours de développement.")

    # Affichage de l'audit des actions
    def afficher_audit_actions(self):
        # Afficher l'audit des actions
        print("Fonctionnalité d'audit des actions en cours de développement.")

    # Sauvegarde automatique des données
    def sauvegarde_automatique(self):
        # Sauvegarde automatique des données
        self.sauvegarder_utilisateurs()
        print("Sauvegarde automatique effectuée.")

    # Sauvegarde des utilisateurs dans le fichier JSON
    def sauvegarder_utilisateurs(self):
        with open(self.fichier_json, 'w', encoding='utf-8') as file:
            json.dump([u.to_dict() for u in self.utilisateurs], file, ensure_ascii=False, indent=4)

    # Chargement des utilisateurs à partir du fichier JSON
    def charger_utilisateurs(self):
        try:
            with open(self.fichier_json, 'r', encoding='utf-8') as file:
                utilisateurs_dict = json.load(file)
                return [Utilisateur.from_dict(u) for u in utilisateurs_dict]
        except FileNotFoundError:
            return []

# Classe de gestion des livres
class GestionLivres:
    def __init__(self, fichier_json):
        self.fichier_json = fichier_json
        self.livres = self.charger_livres()

    # Ajouter un livre
    def ajouter_livre(self):
        id = input("Entrez l'ID du livre : ")
        titre = input("Entrez le titre du livre : ")
        auteur = input("Entrez l'auteur du livre : ")
        genre = input("Entrez le genre du livre : ")
        self.livres.append(Livre(id, titre, auteur, genre))
        self.sauvegarder_livres()
        print(f"Livre {titre} ajouté avec succès.")

    # Supprimer un livre
    def supprimer_livre(self):
        id = input("Entrez l'ID du livre à supprimer : ")
        self.livres = [l for l in self.livres if l.id != id]
        self.sauvegarder_livres()
        print(f"Livre avec l'ID {id} supprimé avec succès.")

    # Lister les livres
    def lister_livres(self):
        for livre in self.livres:
            print(livre)
