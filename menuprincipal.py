from database import Database

def parser_notes(notes_str):
    notes = []
    matieres = notes_str.split("#")
    for matiere in matieres:
        try:
            nom, reste = matiere.strip().split("[")
            note, horaire = reste.strip("]").split("|")
            notes.append({
                "matiere": nom.strip(),
                "note": float(note),
                "horaire": horaire.strip()
            })
        except ValueError:
            print(f"Erreur de format pour : {matiere}")
    return notes


def afficher_etudiants(etudiants):
    if not etudiants:
        print("Aucun étudiant trouvé.")
    else:
        for e in etudiants:
            print(e)


def main():
    db = Database()

    while True:
        print("\n=== MENU ===")
        print("1. Ajouter étudiant")
        print("2. Modifier étudiant")
        print("3. Supprimer étudiant")
        print("4. Rechercher étudiant")
        print("5. Afficher tous les étudiants valides")
        print("6. Afficher tous les étudiants invalides")
        print("7. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            code = input("CODE : ")
            numero = input("Numéro : ")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            date_naissance = input("Date de naissance (JJ/MM/AA) : ")
            classe = input("Classe : ")
            notes_brutes = input("Notes (ex: Math[11|13:06] #Francais[08|17:12] ...) : ")
            notes = parser_notes(notes_brutes)
            valide = input("Valide ? (oui/non) : ").lower() == "oui"

            etudiant = {
                "CODE": code,
                "Numéro": numero,
                "Nom": nom,
                "Prénom": prenom,
                "Date de naissance": date_naissance,
                "Classe": classe,
                "Notes": notes
            }

            db.ajouter_etudiant(etudiant, valide)
            print("Étudiant ajouté avec succès.")

        elif choix == "2":
            numero = input("Numéro de l'étudiant à modifier : ")
            etudiant = db.rechercher_etudiant(numero)
            if etudiant:
                nom = input(f"Nouveau nom ({etudiant['Nom']}) : ") or etudiant["Nom"]
                prenom = input(f"Nouveau prénom ({etudiant['Prénom']}) : ") or etudiant["Prénom"]
                classe = input(f"Nouvelle classe ({etudiant['Classe']}) : ") or etudiant["Classe"]
                date_naissance = input(f"Nouvelle date de naissance ({etudiant['Date de naissance']}) : ") or etudiant["Date de naissance"]
                notes_brutes = input("Nouvelles notes (laisser vide pour garder les anciennes) : ")
                notes = parser_notes(notes_brutes) if notes_brutes else etudiant["Notes"]
                valide = input("Est-il valide ? (oui/non) : ").lower() == "oui"

                nouvelles_donnees = {
                    "Nom": nom,
                    "Prénom": prenom,
                    "Classe": classe,
                    "Date de naissance": date_naissance,
                    "Notes": notes
                }

                db.modifier_etudiant(numero, nouvelles_donnees, valide)
                print("Étudiant modifié avec succès.")
            else:
                print("Étudiant introuvable.")

        elif choix == "3":
            numero = input("Numéro de l'étudiant à supprimer : ")
            db.supprimer_etudiant(numero)
            print("Étudiant supprimé (si existant).")

        elif choix == "4":
            numero = input("Numéro de l'étudiant à rechercher : ")
            etudiant = db.rechercher_etudiant(numero)
            if etudiant:
                afficher_etudiants([etudiant])
            else:
                print("Étudiant introuvable.")

        elif choix == "5":
            print("\nÉtudiants valides :")
            afficher_etudiants(db.recuperer_etudiants(valide=True))

        elif choix == "6":
            print("\nÉtudiants invalides :")
            afficher_etudiants(db.recuperer_etudiants(valide=False))

        elif choix == "7":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()