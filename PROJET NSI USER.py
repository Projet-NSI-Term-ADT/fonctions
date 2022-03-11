import sqlite3
bdd = sqlite3.connect("BASE_DONNEES_SITE.db")
curseur = bdd.cursor()



def sign_in(identifiant, mdp , ad_mail , date_naissance):
    requete = "INSERT INTO UTILISATEURS (Identifiant, Mdp, Adresse_mail, Date_de_naissance) VALUES (?, ?, ?, ?);"
    curseur.execute(requete, (identifiant, mdp , ad_mail , date_naissance))

def sign_in_unique(identifiant, mdp , ad_mail , date_naissance):
    requete = f"SELECT Identifiant FROM UTILISATEURS WHERE Identifiant = '{identifiant}'"
    curseur.execute(requete)
    test = curseur.fetchall()
    if test == [] :
        sign_in(identifiant, mdp , ad_mail , date_naissance)
        return True
    return False

    
'''      
def sign_in(c,identifiant, mdp , ad_mail , date_naissance):
    requete = (f"INSERT INTO UTILISATEURS (Identifiant, Mdp, Adresse_mail,Date_de_naissance) VALUES ('{identifiant}', '{mdp}', '{ad_mail}', '{date_naissance}')")
    c.execute (requete)
    return True  
'''    
'''    
res=sign_in_unique('Rudolphe', 'Vespa412' , 'rudolphe789@turkey.qc' , '27/05/1984')
print(res)
'''


def demande_dev(identifiant,fiche_profil):
    requete = f"INSERT INTO DEV (Nom, Profil) VALUES (?, ?);"
    curseur.execute(requete,(identifiant,fiche_profil))


def valider_dev(identifiant):
    requete = f"UPDATE UTILISATEURS SET Validation_dev = 1 WHERE Identifiant = '{identifiant}'"
    curseur.execute(requete)

def retirer_dev(identifiant):
    requete = f"UPDATE UTILISATEURS SET Validation_dev = 0 WHERE Identifiant = '{identifiant}'"
    curseur.execute(requete)
    

valider_dev('Rudolphe')

retirer_dev('Rudolphe')


demande_dev('Rudolphe','Je suis un jeune developpeur qui cherche à partager ses jeux ')

bdd.commit ()

