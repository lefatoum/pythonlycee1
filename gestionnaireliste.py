from tkinter import *
import random

F = Tk()

Choix1 = Variable(F, ('AAAAA', 'BBBBB', 'CCCCC'))
L1 = Listbox(F, listvariable=Choix1, selectmode="multiple")
L1.grid(column=2, row=0, rowspan=4)

Choix2 = Variable(F, ('DDDDD', 'EEEEE', 'FFFFF'))
L2 = Listbox(F, listvariable=Choix2, selectmode="multiple")
L2.grid(column=2, row=0, rowspan=4)


def GetreverseSelection(ListBox):
    Lindex = []
    for index in ListBox.curselection():
        Lindex.append(index)
    Lindex.reverse()
    return Lindex


def AGauche():
    for i in GetreverseSelection(L2):
        data = L2.get(i)
        L1.insert('end', data)
        L2.delete(i)


def ADroite():
    for i in GetreverseSelection(L1):
        data = L1.get(i)
        L2.insert('end', data)
        L1.delete(i)


BL = Button(F, text="<<<", command=AGauche)
BL.grid(column=1, row=1, sticky="ewns")

BR = Button(F, text=">>>", command=ADroite)
BR.grid(column=1, row=2, sticky="ewns")


def RAZ():
    L2.delete(0, 'end')


def DELSEL():
    for i in GetreverseSelection(L2):
        L2.delete(i)


def ADD():
    data = text.get()
    if len(data) == 0: data = "???"
    L2.insert('end', data)


BRAZ = Button(F, text="Efface tout", command=RAZ)
BRAZ.grid(column=3, row=0, sticky="ewns")

BSUP = Button(F, text="Supprime selection", command=DELSEL)
BSUP.grid(column=3, row=2, sticky="ewns")

BAJ = Button(F, text="Ajoute 1 élément", command=ADD)
BAJ.grid(column=3, row=3, sticky="ewns")


text = StringVar(F)
TE = Entry(F, textvariable=text)
TE.grid(column=3, row=3, sticky="ewns")


F.title("Gestionnaire de listes")
F.mainloop()
