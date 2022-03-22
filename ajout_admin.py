import sqlite3
bdd = sqlite3.connect("BASE_DONNEES_SITE.db")    
curseur = bdd.cursor()
def ajout_admin(identifiant):
    

    curseur.execute(f"SELECT * FROM ADMIN")
    recup_admin = curseur.fetchall()

    curseur.execute(f"SELECT (Identifiant) FROM UTILISATEURS")
    recherche_personne = curseur.fetchall()
    
    curseur.execute(f"SELECT (ID_Utilisateur) FROM UTILISATEURS WHERE Identifiant = '{identifiant}'")
    recup_id = curseur.fetchall()

    id_utilisateur = recup_id[0][0]


    for i in recup_admin:

        if i[1] == id_utilisateur:
            return "Cet utilisateur est déja Admin"
    
    curseur.execute(f"INSERT INTO ADMIN (ID_Utilisateur) VALUES ({id_utilisateur})")
    
    
    bdd.commit()
    return identifiant, "a été ajouté en tant que nouvel admin avec succès !"
    

 