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


def trier_utilisateurs(self):
        critere = input("Entrez le critère de tri (nom ou email) : ")
        self.utilisateurs.sort(key=lambda u: getattr(u, critere))
        self.sauvegarder_utilisateurs()
        print(f"Utilisateurs triés par {critere}.")

    # Recherche d'utilisateurs par un critère donné (nom ou email)
    def recherche_utilisateurs(self):
        critere = input("Entrez le critère de recherche (nom ou email) : ")
        valeur = input(f"Entrez la valeur pour {critere} : ")
        resultats = [u for u in self.utilisateurs if getattr(u, critere) == valeur]
        for utilisateur in resultats:
            print(utilisateur)

    # Importation de données à partir d'un fichier CSV
    def importer_donnees(self):
        fichier_csv = input("Entrez le nom du fichier CSV à importer : ")
        with open(fichier_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.ajouter_utilisateur(row['nom'], row['email'])
        self.sauvegarder_utilisateurs()
        print("Données importées avec succès.")

# Classe de gestion des utilisateurs
class GestionUtilisateurs:
    def __init__(self, fichier_json):
        self.fichier_json = fichier_json
        self.utilisateurs = self.charger_utilisateurs()
    # Emprunter un livre
    def emprunter_livre(self, utilisateur):
        id = input("Entrez l'ID du livre à emprunter : ")
        for livre in self.livres:
            if livre.id == id and livre.disponible:
                livre.disponible = False
                utilisateur.livres_empruntes.append({"id": id, "titre": livre.titre, "date_retour": datetime.now().date() + timedelta(days=14)})
                utilisateur.historique_emprunts.append({"id": id, "titre": livre.titre, "date_emprunt": datetime.now().date()})
                self.sauvegarder_livres()
                print(f"Livre {livre.titre} emprunté avec succès par {utilisateur.nom}.")
                return
        print(f"Livre avec l'ID {id} non disponible ou introuvable.")

    # Retourner un livre
    def retourner_livre(self, utilisateur):
        id = input("Entrez l'ID du livre à retourner : ")
        for livre in self.livres:
            if livre.id == id and not livre.disponible:
                livre.disponible = True
                utilisateur.livres_empruntes = [l for l in utilisateur.livres_empruntes if l["id"] != id]
                self.sauvegarder_livres()
                print(f"Livre {livre.titre} retourné avec succès par {utilisateur.nom}.")
                return
        print(f"Livre avec l'ID {id} non trouvé ou déjà retourné.")

    # Sauvegarde des livres dans le fichier JSON
    def sauvegarder_livres(self):
        with open(self.fichier_json, 'w', encoding='utf-8') as file:
            json.dump([l.to_dict() for l in self.livres], file, ensure_ascii=False, indent=4)

    # Chargement des livres à partir du fichier JSON
    def charger_livres(self):
        try:
            with open(self.fichier_json, 'r', encoding='utf-8') as file:
                livres_dict = json.load(file)
                return [Livre.from_dict(l) for l in livres_dict]
        except FileNotFoundError:
            return []
class GestionLivres:
    def __init__(self, fichier_json):
        self.fichier_json = fichier_json
        self.livres = self.charger_livres()