import re
choice==4
mot="beweb"
deb_mot=0
fin_mot=len(mot)-1

if choice==1:
    while mot[deb_mot]<mot [fin_mot]:
        verif=True
        print "Ceci n'est pas un palindrome"
        if mot(deb_mot)!= mot(fin_mot):
            verif=False
        deb_mot=deb_mot+1
        fin_mot=fin_mot-1
    print"Ceci est un palindrome"

if choice==2:
i=0
nb_lettre=0
    while i<len(mot):
    expression=r"[a-z]"
    if(re.search(expression, mot[i])):
        nb_lettre=nb_lettre+1
    i=i+1
print (nb_lettre)

if choice==3:
    mot = "beweb"
    val = "z"
    remp = "w"
    mot = mot.replace(remp,val)
    print(mot)

if choice==4:
mot = 'beweb'
t= len(mot)/2
# mot = map(''.join, zip(*[iter(mot)]*3))
mot2 = mot[t:]
mot1 = mot[:t]
print(mot1)
print("/")
print(mot2)
