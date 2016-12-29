import re
choice=4
mot="beweb"
deb_mot=0           #commencer 1ere lettre
fin_mot=len(mot)-1   #commencer pa la derniere lettre en avancant vers le debut

if choice==1:

        while mot[deb_mot]<mot [fin_mot]: #Tant que le debut du mot < fin du mot
            verif=True
            print "Ceci n'est pas un palindrome"
            if mot(deb_mot)!= mot(fin_mot):#si le debut du mot est different de la fin du mot
                verif=False
            deb_mot=deb_mot+1 #avancer dans le mot
            fin_mot=fin_mot-1 #avancer
        print"Ceci est un palindrome"


if choice==2:
        i=0 #commencer du debut du mot
        nb_lettre=0
        while i<len(mot): #Tant que i<longueur du mot
            expression=r"[a-z]" #trouve les caracteres alpha
            if(re.search(expression, mot[i])):#cherche alpha dans mot
                nb_lettre=nb_lettre+1 #avancer
            i=i+1
        print (nb_lettre)


if choice==3:
        mot = "beweb"
        val = "z" #valeur actuelle
        remp = "w" #valeur remplacement
        mot = mot.replace(remp,val) #remplacer val par remp
        print(mot)


if choice==4:
        mot = 'beweb'
        t= len(mot)/2 #decouper le mot apres les 2 premieres lettres
        mot2 = mot[t:]
        mot1 = mot[:t]
        print(mot1)
        print("/")
        print(mot2)
