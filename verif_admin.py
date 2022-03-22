import sqlite3

bdd = sqlite3.connect("BASE_DONNEES_SITE.db")    
curseur = bdd.cursor()

def verif_admin(identifiant):
    curseur.execute(f"SELECT * FROM ADMIN")
    recup_admin = curseur.fetchall()

    curseur.execute(f"SELECT (ID_Utilisateur) FROM UTILISATEURS WHERE Identifiant = '{identifiant}'")
    recup_id = curseur.fetchall()

    id_utilisateur = recup_id[0][0]

    for i in recup_admin:
        if i[1] == id_utilisateur:
        
            return identifiant, "est admin."
    
    return identifiant, "n'est pas admin."
