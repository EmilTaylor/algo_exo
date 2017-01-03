
#on initialise les variables et le tableau
tab = [4,80,15,26,9,13,7]
switch = ""
sorted = False
print("base : " + str(tab))
while sorted == False :
	moved = False
	i = 0

	while i < len(tab) -1:
#tant que l'index courant est inferieur a la longueur du tableau
# si la valeur suivant est plus grande, on switch
		if tab[i+1] > tab[i]:
			switch = tab[i] 
			tab[i] = tab[i + 1] 
			tab[i + 1] = switch
			moved = True
			print(tab)
		i += 1
	print("boucle : " + str(tab))
	if moved == False:
		sorted = True
print(tab)
