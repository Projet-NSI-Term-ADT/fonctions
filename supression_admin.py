import sqlite3

bdd = sqlite3.connect("BASE_DONNEES_SITE.db")    
curseur = bdd.cursor()

def supression_admin(identifiant):

    curseur.execute(f"SELECT * FROM ADMIN")
    recup_admin = curseur.fetchall()

    curseur.execute(f"SELECT (ID_Utilisateur) FROM UTILISATEURS WHERE Identifiant = '{identifiant}'")
    recup_id = curseur.fetchall()

    id_utilisateur = recup_id[0][0]
    
    requete = f"DELETE FROM ADMIN WHERE (ID_Utilisateur) = '{id_utilisateur}'"
    curseur.execute(requete)
    bdd.commit()
    return identifiant, "supprimé avec succès !"
    
