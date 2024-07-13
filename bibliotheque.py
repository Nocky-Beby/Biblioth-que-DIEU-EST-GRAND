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

# Classe de gestion des utilisateurs
class GestionUtilisateurs:
    def __init__(self, fichier_json):
        self.fichier_json = fichier_json
        self.utilisateurs = self.charger_utilisateurs()

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

    # Modification des informations d'un utilisateur
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

    # Tri des utilisateurs par un critère donné (nom ou email)
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