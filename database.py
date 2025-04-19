from pymongo import MongoClient

class Database:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="gestion_etudiants"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.valides = self.db["etudiants_valides"]
        self.invalides = self.db["etudiants_invalides"]

    def ajouter_etudiant(self, etudiant, valide=True):
        collection = self.valides if valide else self.invalides
        collection.insert_one(etudiant)

    def modifier_etudiant(self, numero, nouvelles_donnees, valide=True):
        collection = self.valides if valide else self.invalides
        collection.update_one({"Numéro": numero}, {"$set": nouvelles_donnees})

    def supprimer_etudiant(self, numero):
        result = self.valides.delete_one({"Numéro": numero})
        if result.deleted_count == 0:
            self.invalides.delete_one({"Numéro": numero})

    def rechercher_etudiant(self, numero):
        etudiant = self.valides.find_one({"Numéro": numero}, {"_id": 0})
        return etudiant if etudiant else self.invalides.find_one({"Numéro": numero}, {"_id": 0})

    def recuperer_etudiants(self, valide=True):
        collection = self.valides if valide else self.invalides
        return list(collection.find({}, {"_id": 0}))
