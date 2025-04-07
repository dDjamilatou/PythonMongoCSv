import csv
from database import Database
from validation import (
    validate_numero,
    validate_prenom,
    validate_nom,
    validate_date,
    validate_classe
)

# Initialisation de la base de données
db = Database()

# Nettoyer les collections avant d'insérer les nouvelles données
db.vider_collections()

# Lecture du fichier CSV
file_path = "data.csv"

with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    headers = next(reader)  # Lire les en-têtes
    for row in reader:
        if all(not cell.strip() for cell in row):  # Vérifie si toutes les colonnes sont vides
            continue  # Ignore cette ligne

        if len(row) != 7:
            db.ajouter_etudiant({"Données": row, "Erreur": "Structure invalide"}, valide=False)
            continue

        code, numero, nom, prenom, date_naissance, classe, notes = row

        errors = []
        if not validate_numero(numero):
            errors.append(f"Numéro invalide: {numero}")
        if not validate_prenom(prenom):
            errors.append(f"Prénom invalide: {prenom}")
        if not validate_nom(nom):
            errors.append(f"Nom invalide: {nom}")
        date_naissance = validate_date(date_naissance)
        if not date_naissance:
            errors.append(f"Date de naissance invalide")
        if not validate_classe(classe):
            errors.append(f"Classe invalide: {classe}")

        etudiant = {
            "CODE": code,
            "Numéro": numero,
            "Nom": nom,
            "Prénom": prenom,
            "Date de naissance": date_naissance,
            "Classe": classe,
            "Notes": notes
        }

        if errors:
            etudiant["Erreurs"] = errors
            db.ajouter_etudiant(etudiant, valide=False)
        else:
            db.ajouter_etudiant(etudiant, valide=True)

# Affichage des étudiants valides
# print("Étudiants valides :")
# for etudiant in db.recuperer_etudiants(valide=True):
#     print(etudiant)


# Affichage des étudiants invalides
# print("\nÉtudiants invalides :")
# for etudiant in db.recuperer_etudiants(valide=False):
#     print(etudiant)

print("Données insérées avec succès dans MongoDB !")

