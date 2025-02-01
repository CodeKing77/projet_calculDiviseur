from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *


def afficherNombre(event): 
    recupereNombre = zoneDeSaisieNombre.get()
    labelDuNombre["text"] = f"{recupereNombre} :"

def calculDiviseur():  #Fonction de Calcul des diviseurs de nombre entiers positifs
    listeDesDiviseurs =[]
    nombre = zoneDeSaisieNombre.get()
    if nombre.isnumeric():
        nombre = int(nombre)
        for i in range(1,nombre+1):
            if nombre % i == 0 :
                listeDesDiviseurs.append(i)
                #listeDesDiviseurs = listeDesDiviseurs + [i]  Cette méthode marche aussi
            else :
                pass
        resultat = str(listeDesDiviseurs)    #Conversion de la liste en  string
        print(resultat.strip("[]"), type(resultat))       #La fonction strip("[]")  permet d'enlever les parenthèses du  string
        resultatDiviseur.set(f'{resultat.strip("[]")}')   #La fonction strip("[]")  permet d'enlever les parenthèses du  string
    else :
        while True :
            showerror("Erreur", "Veuillez Saisir un nombre entier Positif")
            return

def calcul(event):  #Fonction de Calcul des diviseurs de nombre entiers positifs 
    listeDesDiviseurs =[]
    nombre = zoneDeSaisieNombre.get()
    if nombre.isnumeric():
        nombre = int(nombre)
        for i in range(1,nombre+1):
            if nombre % i == 0 :
                listeDesDiviseurs.append(i)
                #listeDesDiviseurs = listeDesDiviseurs + [i]  Cette méthode marche aussi
            else :
                pass
        resultat = str(listeDesDiviseurs)    #Conversion de la liste en  string
        print(resultat.strip("[]"), type(resultat))       #La fonction strip("[]")  permet d'enlever les parenthèses du  string
        resultatDiviseur.set(f'{resultat.strip("[]")}')   #La fonction strip("[]")  permet d'enlever les parenthèses du  string
    else :
        while True :
            showerror("Erreur", "Veuillez Saisir un nombre entier Positif")
            return
        
def  annulation():
    zoneDeSaisieNombre.delete(0, END)
    labelDuNombre["text"]= ""
    resultatDiviseur.set("")  


#Création  et Configuration de la fenêtre principale
fenetre = Tk()
fenetre.title("Calcul de Diviseurs")
fenetre.geometry("680x300")
fenetre.resizable(width=True , height=False)
fenetre.eval('tk::PlaceWindow . ')
fenetre.config(background="navyblue")


#Ajout des Widgets
labelDeSaisie =Label(fenetre, text="Entrer un nombre : ")
labelDeSaisie.place_configure(x=50 , y=50)

zoneDeSaisieNombre = Entry(fenetre)
zoneDeSaisieNombre.place_configure(x=250 , y=42 , width=350 , height=30)
zoneDeSaisieNombre.bind("<KeyRelease>", afficherNombre)
zoneDeSaisieNombre.bind("<Return>", calcul)

labelDesDiviseurs = Label(fenetre, text="Les diviseurs de ")
labelDesDiviseurs.place_configure(x= 50, y=150)

labelDuNombre = Label(fenetre, text="")
labelDuNombre.place(x=140 , y=150)

resultatDiviseur =StringVar()
labelAffichageResultat = Label(fenetre, textvariable=resultatDiviseur)
labelAffichageResultat.place(x=250 , y=140, width=500 , height=30)


#Ajout des boutons 
boutonCalculer = Button(fenetre, text="Calculer", command=calculDiviseur)
boutonCalculer.place_configure(x=250 , y=240)

boutonAnnuler = Button(fenetre, text="Annuler", command=annulation)
boutonAnnuler.place_configure(x= 400, y=240)


#Affichage de la fenêtre principale
fenetre.mainloop()