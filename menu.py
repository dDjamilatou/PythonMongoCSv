from database import Database

class Menu:
    def __init__(self):
        self.db = Database()

    def afficher_menu(self):
        while True:
            print("\n1. Afficher les étudiants valides")
            print("2. Afficher les étudiants invalides")
            print("3. Rechercher un étudiant par numéro")
            print("4. Quitter")
            choix = input("Choisissez une option : ")

            if choix == "1":
                for etudiant in self.db.recuperer_etudiants(valide=True):
                    print(etudiant)
            elif choix == "2":
                for etudiant in self.db.recuperer_etudiants(valide=False):
                    print(etudiant)
            elif choix == "3":
                numero = input("Entrez le numéro de l'étudiant : ")
                etudiant = self.db.rechercher_etudiant(numero)
                print(etudiant if etudiant else "Aucun étudiant trouvé.")
            elif choix == "4":
                break
            else:
                print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu = Menu()
    menu.afficher_menu()
