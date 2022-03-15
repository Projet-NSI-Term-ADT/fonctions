from PIL import Image
import os

def resizeimg(x,y,nom_fichier):
    if os.path.exists(f"images\jeux\{nom_fichier}"):
        imageLue = Image.open(f"images\jeux\{nom_fichier}")
    else:
        print("Impossible d'ouvrir le fichier car il n'existe pas")
    if x < 500 and y < 755:
        print("Les dimensions sont invalides.\nDimensions minimales requises : 500 x 755")
    else:
        dim=imageLue.size
        imageComp=imageLue.resize((500,755))
        imageComp.save(f"images\jeux\jeux_comp\{nom_fichier}")
        os.remove(f"images\jeux\{nom_fichier}")
        dimComp=imageComp.size
        print("Dimension d'origine: ",dim,"\nDimension compressée:",dimComp)