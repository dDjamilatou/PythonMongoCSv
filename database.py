from pymongo import MongoClient

class Database:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="gestion_etudiants"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.valides = self.db["etudiants_valides"]
        self.invalides = self.db["etudiants_invalides"]

    def ajouter_etudiant(self, etudiant, valide=True):
        """Ajoute un étudiant dans la bonne collection"""
        collection = self.valides if valide else self.invalides
        collection.insert_one(etudiant)
    
    def vider_collections(self):
        """Vide les collections pour éviter les doublons"""
        self.valides.delete_many({})
        self.invalides.delete_many({})

    def recuperer_etudiants(self, valide=True):
        """Récupère tous les étudiants d'une collection"""
        collection = self.valides if valide else self.invalides
        return list(collection.find({}, {"_id": 0}))  # Ne pas afficher l'ID MongoDB

    def rechercher_etudiant(self, numero):
        """Recherche un étudiant par son numéro"""
        etudiant = self.valides.find_one({"Numéro": numero}, {"_id": 0})
        return etudiant if etudiant else self.invalides.find_one({"Numéro": numero}, {"_id": 0})

