from operator import xor


    
def generer_cle(mot, n):
    cle = ""
    x = n//len(mot)
    for i in range(x+1):
        cle = cle + mot
    return cle

def xor_crypt(message, cle):
    
    if len(cle) < len(message):
        cle = generer_cle(cle, len(message))
    lst = []
    for char in range(len(message)):
        lst.append(xor(ord(message[char]), ord(cle[char])))
    return lst

def xor_decrypt(lst, cle):
    if len(cle) < len(lst):
        cle = generer_cle(cle, len(lst))
    message = ""
    for nbr in range(len(lst)):
        message += chr(xor(lst[nbr], ord(cle[nbr])))
    return message
        

        
