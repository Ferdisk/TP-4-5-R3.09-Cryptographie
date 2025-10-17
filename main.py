import hashlib
class Couleurs:
    BLEU = '\033[94m'       # Bleu
    CYAN = '\033[96m'       # Cyan / Bleu clair
    VERT = '\033[92m'       # Vert
    JAUNE = '\033[93m'      # Jaune
    ROUGE = '\033[91m'      # Rouge         # Réinitialisation (retour normal)
    GRAS = '\033[1m'        # Texte en gras
    SOULIGNE = '\033[4m'    # Texte souligné
    REINITIALISER = '\033[0m'  # Identique à FIN


def verifchaine(chaine: str) -> bool:
    """Renvoie False si la chaîne contient au moins un caractère invisible."""
    CARACTERES_INVISIBLES = (
        ' ',      # espace normal
        '\t',     # tabulation
        '\n',     # saut de ligne
        '\r',     # retour chariot
        '\v',     # tabulation verticale
        '\f',     # saut de page
        '\u00A0', # espace insécable (non-breaking space)
        '\u1680', # espace ogham
        '\u2000', # espace en
        '\u2001', # espace em
        '\u2002', # espace demi-en
        '\u2003', # espace 3/4 em
        '\u2004', # espace fine
        '\u2005', # espace moyenne
        '\u2006', # espace fine 3/4
        '\u2007', # espace numérique
        '\u2008', # espace ponctuation
        '\u2009', # fine espace
        '\u200A', # espace fine très petite
        '\u2028', # saut de ligne Unicode
        '\u2029', # séparateur de paragraphe
        '\u202F', # espace fine insécable (français typographique)
        '\u205F', # espace moyenne mathématique
        '\u3000', # espace idéographique (asiatique)
    )

    for caractere in chaine:
        if caractere in CARACTERES_INVISIBLES:
            return False 
    return True


def concatener_deux_chaines(chaine1:str, chaine2:str)-> str:
    return chaine1 + chaine2


def hachage(chaine1:str, chaine2:str):


    chaine = concatener_deux_chaines(chaine1, chaine2)

    h1 = chaine.encode()

    hash = hashlib.sha1(h1).hexdigest()
    h8 = hash[:8]
    print("SHA1:", h8)


if __name__ == "__main__":
    mdp_maitre: str = input("Veuillez entrer votre mot de passe maître sans caractères invisibles : ")
    print()

    while not verifchaine(mdp_maitre):
        mdp_maitre = input("Erreur : la chaîne contient un caractère invisible.\nVeuillez réessayer : ")
        print()

    tag: str = input("Veuillez entrer un tag sans caractères invisibles : ")
    print()

    while not verifchaine(tag):
        tag = input("Erreur : la chaîne contient un caractère invisible.\nVeuillez réessayer : ")
        print()
    
    hachage(mdp_maitre, tag)

    



    



    
    

    
    