from tkinter import *
from tkinter.filedialog import askopenfilename
#nous permet de parccourir notre ordinateur pour choisir une image
from tkinter.messagebox import showerror, showinfo
#Pour créer la fenêtre d'erreur/infos
from PageInscrits import listeInscrit


class Personnage():
	def __init__(self, prenom, nom, photo):
		self.prenom = prenom
		self.nom = nom
		self.photo = photo
	
	def __eq__(self, other):
		return(self.prenom == other.prenom and self.nom == other.nom)

def parcourir():
	global imageName
	#pouvoir rentrer dans le dossier de l'utilisateur pour ajouter une image
	imn = askopenfilename(initialdir="/", title = "selectionner une image",filetypes = (("png file","*.png"),("jpg file","*.jpg")))

	if imn :
		imageName=imn
	if imageName:
		texte = imageName.split("/")#prends les elements de chaque / pour les mettre dans un tableau
		photoEntree.configure(text=".../"+texte[-1])#pour ne pas afficher toute l'adressse de l'image juste le dernier mot de la liste avec -1

#Est ce que la personne a déjà été ajouté ou pas	
def appartient(liste,val):
	for i in range (len(liste)):
		if liste[i].__eq__(val):#other=val liste i = self
			return 1 #faux
	return 0 #vrai

def valider():
	global listePersonne, imageName
	photo = imageName
	if prenomEntree.get() and nomEntree.get() and photo :
		pn = Personnage(prenomEntree.get(),nomEntree.get(),photo)
		if appartient(listePersonne, pn):
			showerror(title = "Formulaire invalide", message = "Cet utilisateur existe déjà")
		else:
			listePersonne.append(pn)
			showinfo(title = "Validation reussie", message = "{} a bien été ajouté".format(prenomEntree.get()))
	else:
		showerror(title="Formulaire invalide", message = "Tous les chants doivent être renseignés")

def reinitialiser():
	global imageName
	prenomEntree.delete(0,END)
	nomEntree.delete(0,END)
	imageName=""
	photoEntree.configure(test="aucune image selectionnée")


imageName, listePersonne = "",[]

fen = Tk()
fen.geometry("300x320+300+150")
fen.title("Page d'inscriptions")

contenu = Canvas(fen, bg="#FF7800")

fontLabel = "arial 13 bold"
fontEntree = "arial 11 bold"

prenom = Label(contenu, text="votre prénom :", font = fontLabel, fg="white",bg="#FF7800")
nom = Label(contenu, text="votre nom :", font = fontLabel, fg="white",bg="#FF7800")
photo = Label(contenu, text="votre photo :", font = fontLabel, fg="white",bg="#FF7800")
validation = Label(contenu, text="Entrez vos informations ici:", font = fontLabel, fg="white",bg="#FF7800")

prenomEntree = Entry(contenu,font=fontEntree)
nomEntree = Entry(contenu,font=fontEntree)
photoEntree = Label(contenu, text="Aucune image n'est selectionnée", font = "arial 8 bold", fg="white",bg="#FF7800")
buttonParcourir = Button(contenu,text="Pr", command=parcourir, fg="#FF7800",bg="white")

validation.grid(row=0,column=0,columnspan=2)
prenom.grid(row=1,column=0,sticky=E,padx=5,pady=5)
nom.grid(row=2,column=0,sticky=E,padx=5,pady=5)
photo.grid(row=3,column=0,sticky=E,padx=5,pady=5)

prenomEntree.grid(row=1,column=1,padx=5, pady=5)
nomEntree.grid(row=2,column=1,padx=5, pady=5)
photoEntree.grid(row=3,column=1,padx=5, pady=5, sticky = W)
buttonParcourir.grid(row=3,column=1,padx=5, pady=5, sticky = E)

b1 = Button(fen,text="Valider", command=valider, width=10, fg="#FF7800",bg="white")
b2 = Button(fen,text="Reinitialiser", command=reinitialiser, width=10, fg="#FF7800",bg="white")
b3 = Button(fen,text="Voir la liste", command=lambda : listeInscrit(fen,listePersonne), width=10, fg="#FF7800",bg="white")

b1.grid(row=4, column=0, pady=5)
b2.grid(row=5, column=0, pady=5)
b3.grid(row=6, column=0, pady=5)

contenu.grid(row=0, column=0, padx=5,pady=5)

#Affiche la fenêtre
fen.mainloop()


