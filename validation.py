import re
from datetime import datetime

# Fonction de validation du numéro
def validate_numero(numero):
    return (
        len(numero) == 7 and
        re.match(r'^(?=.*[A-Z])(?=.*[0-9])[A-Z0-9]{7}$', numero) is not None
    )

# Fonction de validation du prénom
def validate_prenom(prenom):
    return bool(prenom) and prenom[0].isupper() and prenom.isalpha() and len(prenom) >= 3

# Fonction de validation du nom
def validate_nom(nom):
    return bool(nom) and nom[0].isupper() and nom.isalpha() and len(nom) >= 2

# Fonction de validation de la date de naissance
def validate_date(date):
    try:
        datetime_obj = datetime.strptime(date, '%d/%m/%y')
        return datetime_obj.strftime('%d/%m/%Y')  # Retourne la date au format jj/mm/aaaa
    except ValueError:
        return None

# Fonction de validation de la classe
def validate_classe(classe):
    classe = classe.lower().replace(' ', '')  # Enlever les espaces et normaliser la casse
    match = re.match(r'^(\d{1,2})em(a|b)$', classe)
    if match:
        return f"{match.group(1)}em{match.group(2).upper()}"
    return None
