
quitter = False
oui = "o"
non = "n"
reponse = ""
verif = False

while quitter == False:
	print("Hello Guy!")
	perroquet = raw_input("entre une phrase ou un mot: ")
	print(str(perroquet))
	verif = True

	while verif == True:
		reponse = raw_input("Veux-tu quitter o/n ?")

		if oui == reponse:
			quitter = True
			verif = False
		elif non == reponse:
			print("non")
			verif = False
		else: ("non")
print("Oh no no no... ")
