import sqlite3

bdd = sqlite3.connect("BASE_DONNEES_SITE.db")
curseur = bdd.cursor()
#curseur.execute('PRAGMA foreign_keys = OFF'
"""
def login(Mdp, identifiant):
    requete = "SELECT Identifiant, Adresse_mail, Mdp FROM UTILISATEURS WHERE Mdp = ? AND identifiant = ?;" # si marche pas faire avec dico : https://python.doctor/page-database-data-base-donnees-query-sql-mysql-postgre-sqlite
    curseur.execute(requete, (Mdp, identifiant))
    user = curseur.fetchone()
    print(user)
    #if curseur.fetchone()[1] != None: #est-ce que je dois re-vérifier que ce qu'il y a dans le curseur est bien le bon identifiant ou je laisse qu'une vérification
    #    return True
    #else :
    #    return False
    #bdd.commit()
 """   

def login(identifiant, Mdp): #peut-être un soucis de guilemets
    requete = "SELECT Identifiant, Adresse_mail, Mdp FROM UTILISATEURS WHERE Identifiant = ? AND Mdp = ?;" # https://python.doctor/page-database-data-base-donnees-query-sql-mysql-postgre-sqlite
    curseur.execute(requete, (identifiant, Mdp))
    user = curseur.fetchone()
    if user != None:
        return True
    else:
        return False
    bdd.commit() #pas obligé
    
    
    

    #if curseur.fetchone()[1] != None: #est-ce que je dois re-vérifier que ce qu'il y a dans le curseur est bien le bon identifiant ou je laisse qu'une vérification
    #    return True
    #else :
    #    return False
    #bdd.commit()
    