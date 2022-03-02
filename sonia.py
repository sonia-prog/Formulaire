# -*- coding: utf-8 -*-
from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


fenetre = Tk()
fenetre.geometry("600x500")
fenetre.title("Formulaire recrutement Médecins / Agents")

v = IntVar()
w = IntVar()

cadre1 = LabelFrame(fenetre)
cadre1.pack(padx=5, pady=5)

etiquette1 = Label(cadre1, text="* Nom :")
etiquette1.pack(padx=5, pady=5, side=LEFT)
entree1 = Entry(cadre1)
entree1.pack(padx=5, pady=5, side=LEFT)

cadre2 = LabelFrame(fenetre)
cadre2.pack(padx=5, pady=5)

etiquette2 = Label(cadre2, text='* Prénom :')
etiquette2.pack(padx=0, pady=5, side=LEFT)
entree2 = Entry(cadre2)
entree2.pack(padx=5, pady=5, side=LEFT)

cadre3 = LabelFrame(fenetre)
cadre3.pack(padx=5, pady=5)

etiquette3 = Label(cadre3, text=" * Date d'arrivée :")
etiquette3.pack(padx=5, pady=5, side=LEFT)
entree3 = Entry(cadre3)
entree3.pack(padx=5, pady=5, side=LEFT)

cadre4 = LabelFrame(fenetre)
cadre4.pack(padx=5, pady=5)

etiquette4 = Label(cadre4, text=" * Adresse mail :")
etiquette4.pack(padx=5, pady=5, side=LEFT)
Boutonmail1 = Radiobutton(cadre4, text="oui", value=4, variable=w)
Boutonmail2 = Radiobutton(cadre4, text="non", value=5, variable=w)
Boutonmail1.pack(padx=5, pady=5, side=LEFT)
Boutonmail2.pack(padx=5, pady=5, side=LEFT)


cadre5 = LabelFrame(fenetre)
cadre5.pack(padx=5, pady=5)

etiquette5 = Label(cadre5, text=" * Etablissement principal :")
etiquette5.pack(padx=5, pady=5, side=LEFT)
Boutonmail1 = Radiobutton(cadre5, text="Saintes", value=1, variable=v).pack(padx=5, pady=5, side=LEFT)
Boutonmail2 = Radiobutton(cadre5, text="Royan", value=2, variable=v).pack(padx=5, pady=5, side=LEFT)
Boutonmail3 = Radiobutton(cadre5, text="Saint Jean d'Angely", value=3, variable=v).pack(padx=5, pady=5, side=LEFT)


cadre6 = LabelFrame(fenetre)
cadre6.pack(padx=5, pady=5)

etiquette6 = Label(cadre6, text=" * Service :")
etiquette6.pack(padx=5, pady=5, side=LEFT)
choix = ttk.Combobox(cadre6, values=["Admissions", "GRH", "Pédiatrie", "Réanimation-urgence"], state="readonly")
choix.pack(padx=5, pady=5, side=LEFT)

cadre7 = LabelFrame(fenetre)
cadre7.pack(padx=5, pady=5)

etiquette7 = Label(cadre7, text=" * Nom du profil à copier :")
etiquette7.pack(padx=5, pady=5, side=LEFT)
entree7 = Entry(cadre7)
entree7.pack(padx=5, pady=5, side=LEFT)

cadre8 = LabelFrame(fenetre)
cadre8.pack(padx=5, pady=5)

etiquette8 = Label(cadre8, text=" * Commentaire :")
etiquette8.pack(padx=5, pady=5, side=LEFT)
entree8 = Entry(cadre8)
entree8.pack(padx=5, pady=5, side=LEFT)


def formulaireenvoye():
    messagebox.showinfo("Statut de l'inscription", "Formulaire envoyé")
    with open("rapport.txt", "w", encoding='utf-8') as fichier:
        fichier.write(
            'Message envoyé à ' + datetime.now().strftime(('%d-%m-%Y %H-%M-%S'))
            + '\n utilisateur\t'
            + entree1.get()
            + "\n mdp:\t "
            + entree2.get()
            )
    fenetre.quit()


b = Button(fenetre, text="Valider", command=formulaireenvoye)
b.pack(padx=5, pady=5)

etiquette9 = Label(fenetre, text=" * Champs obligatoires")
etiquette9.pack(side=LEFT)

fenetre.mainloop()
