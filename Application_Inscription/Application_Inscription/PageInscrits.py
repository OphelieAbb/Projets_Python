from tkinter import *
from PIL import Image, ImageTk

def listeInscrit(fenetre,liste):
	newFen = Toplevel(fenetre)
	newFen.geometry("350x400+350+150")
	newFen.title("Liste des inscrits")

	listeCan = Canvas(newFen, bg="#FF7800")
	fontLabel = "arial 11 bold"

	resultat = Label (contenu, text = "Liste des inscrits", font = fontLabel,fg="#FF7800",bg="white")
	prenom = Label (contenu, text = "prénoms", font = fontLabel,fg="#FF7800",bg="white")
	nom = Label (contenu, text = "noms", font = fontLabel,fg="#FF7800",bg="white")
	status = Label (contenu, text = "Aucun inscrit pour le moment", font = "arial 9 bold",fg="#FF7800",bg="white")

	listeCan.grid(row=0,column=0)
	resultat.grid(row=0,column=0, columnspan=3)
	photo.grid(row=1,column=0,padx=5,pady=5)
	prenom.grid(row=1,column=1,padx=5,pady=5)
	nom.grid(row=1,column=2,padx=5,pady=5)
	status.grid(row=2,column=0,columnspan=3)

	if liste :
		r=2
		for p in liste:
			photoLab = Label(listeCan, height=50)
			img = Image.open(p.photo)
			img = img.resize((80,80),Image.ANTIALIAS)
			photoLab.img = ImageTk.PhotoImage(img)
			photoLab.configure(image=photoLab.img)

			pre=Label(listenCan, text=p.prenom, font = fontLabel, fg="white", bg="#FF7800")
			no=Label(listenCan, text=p.nom, font = fontLabel, fg="white", bg="#FF7800")

			photoLab.grid(row = r,column = 1)
			pre.grid(row = r,column = 2)
			no.grid(row = r,column = 3)

			listeCan.create_line(9,55,355,55,width = 1,fill="white")
			r+=1

			stuatus.configure(text="{} inscris pour le moment".format(len(liste)))
			status.grid(row=r, column=0, columnspan = 3,pady=2)

	newFen.mainloop()

