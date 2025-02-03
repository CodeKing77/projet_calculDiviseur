from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from PIL import Image, ImageTk  # Importation de la Bibliothèque pillow pour insérer les images dans la fenêtre
import threading  # Importation du package thread pour calculer les diviseurs dans un thread séparé
import time  # Importation de la bibliothèque de temps pour marquer la pause

def afficherNombre(event):
    recupereNombre = zoneDeSaisieNombre.get()
    labelDuNombre["text"] = f"{recupereNombre} :"

def calculerDiviseurs(nombre, listbox, event, update_interval=0.1):
    listeDesDiviseurs = []
    if nombre.isnumeric():
        nombre = int(nombre)
        for i in range(1, nombre + 1):
            if nombre % i == 0:
                listeDesDiviseurs.append(i)
                if len(listeDesDiviseurs) >= 1000:  # Limiter le nombre de diviseurs affichés
                    listeDesDiviseurs.append("...")
                    break

                # Mettre à jour l'interface utilisateur à intervalles réguliers
                if i % 1000 == 0:  # Mettre à jour tous les 1000 diviseurs
                    fenetre.after(0, afficherDiviseurs, listbox, listeDesDiviseurs)
                    time.sleep(update_interval)  # Pause pour permettre la mise à jour de l'interface utilisateur

        # Mettre à jour l'interface utilisateur une dernière fois après le calcul
        fenetre.after(0, afficherDiviseurs, listbox, listeDesDiviseurs)
    else:
        fenetre.after(0, showerror, "Erreur", "Veuillez Saisir un nombre entier Positif")

    # Signaler la fin du calcul
    event.set()

def afficherDiviseurs(listbox, listeDesDiviseurs):
    listbox.delete(0, END)
    for diviseur in listeDesDiviseurs:
        listbox.insert(END, diviseur)

def calculDiviseur():
    nombre = zoneDeSaisieNombre.get()
    if not nombre.isnumeric():
        showerror("Erreur", "Veuillez Saisir un nombre entier Positif")
        return

    # Désactiver les boutons pendant le calcul
    boutonCalculer.config(state=DISABLED)
    boutonAnnuler.config(state=DISABLED)

    # Créer un objet Event pour signaler la fin du calcul
    event = threading.Event()

    # Lancer le calcul dans un thread séparé
    thread = threading.Thread(target=calculerDiviseurs, args=(nombre, listbox, event))
    thread.start()

    # Réactiver les boutons après le calcul
    fenetre.after(100, lambda: fenetre.after(100, check_thread, event))

def check_thread(event):
    if event.is_set():
        boutonCalculer.config(state=NORMAL)
        boutonAnnuler.config(state=NORMAL)
    else:
        fenetre.after(100, check_thread, event)

def calcul(event):
    calculDiviseur()

def annulation():
    zoneDeSaisieNombre.delete(0, END)
    labelDuNombre["text"] = ""
    listbox.delete(0, END)

# Création et Configuration de la fenêtre principale
fenetre = Tk()
fenetre.title("Diviseur de Nombres Entiers")
fenetre.geometry("650x400")
fenetre.resizable(width=False, height=False)
fenetre.eval('tk::PlaceWindow . ')
fenetre.config(background="deepskyblue")

# Charger l'image pour l'icône de la fenêtre
icon_path = "C:/Users/lenovo/Desktop/MyApps/projet_calculDiviseur/divide_png.png"  # Remplacez par le chemin de votre image
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
fenetre.iconphoto(False, icon_photo)

# Définir les styles pour les boutons Calculer et Annuler
style = Style()
style.configure("TButton", padding=6, relief="flat", background="#ccc", foreground="#000")
style.map("TButton", background=[("active", "#aaa")])

style.configure("Green.TButton", background="green", foreground="black")
style.configure("Red.TButton", background="red", foreground="black")

# Ajout des Widgets
labelDeSaisie = Label(fenetre, text="Entrer un nombre : ", font="Arial")
labelDeSaisie.place_configure(x=50, y=50)

zoneDeSaisieNombre = Entry(fenetre, font="Arial")
zoneDeSaisieNombre.place_configure(x=280, y=42, width=150, height=30)
zoneDeSaisieNombre.bind("<KeyRelease>", afficherNombre)
zoneDeSaisieNombre.bind("<Return>", calcul)

labelDesDiviseurs = Label(fenetre, text="Les diviseurs de ", font="Arial")
labelDesDiviseurs.place_configure(x=50, y=150)

labelDuNombre = Label(fenetre, text="", font="Arial")
labelDuNombre.place(x=172, y=150)

# Ajout de la Listbox avec une barre de défilement
monFrame = Frame(fenetre)
monFrame.place(x=280, y=140, width=250, height=120)

barreDefilement = Scrollbar(monFrame, orient=VERTICAL)
listbox = Listbox(monFrame, yscrollcommand=barreDefilement.set, font="Arial")
barreDefilement.config(command=listbox.yview)
barreDefilement.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=True)

# Ajout des boutons avec les styles personnalisés
boutonCalculer = Button(fenetre, text="Calculer Diviseur", command=calculDiviseur, style="Green.TButton")
boutonCalculer.place_configure(x=280, y=320)

boutonAnnuler = Button(fenetre, text="Annuler", command=annulation, style="Red.TButton")
boutonAnnuler.place_configure(x=450, y=320)

# Affichage de la fenêtre principale
fenetre.mainloop()
