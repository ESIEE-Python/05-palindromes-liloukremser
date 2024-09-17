'oui'
#### Fonction secondaire
import string

def ispalindrome(s):
    """ evalue si la phrase est un palindrome ou non """
    s = s.lower()
    remplacer_accents = s.maketrans('éèêëàâäôç','eeeeaaaoc')
    enlever_ponctuation = s.maketrans('','', string.punctuation + ' ')
    s_traduite = s.translate(remplacer_accents)
    s_finale = s_traduite.translate(enlever_ponctuation)
    if s_finale == s_finale[::-1] :
        return True
    return False

#### Fonction principale

def main():
    """ test de la fonction ispalindrome"""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
