#Projet réalisé par Jessy Makhloufi
from tkinter import*
from random import*
fenetre = Tk()
fenetre.config(width=1000, height=800, bg='white')
fenetre.title("Choix du Pixel Art")
texte1=Label(text="Choisissez votre Pixel Art", font=("time",30,"underline"),bg="white")
texte1.place(x=275, y=100)
def Totoro(): # pour créer les pixel Art Totoro avec les bouton
    fenetre = Tk()
    fenetre.config(height=1000, width=1000)
    fenetre.title("Totoro (Pixel Art)")
    Canevas = Canvas(fenetre, bg='white', height=1000, width=1000)
    Canevas.place(x=0, y=0)
    NB_LIGNES = 20
    NB_COLONNES = 20
    TAILLE_PIXEL = 29
    Grille_pixel = []
    Table_Totoro = [
        [0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 1, 3, 4, 3, 4, 4, 1, 2, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 2, 2, 1, 3, 4, 3, 4, 1, 2, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 2, 2, 2, 1, 3, 3, 1, 2, 2, 2, 1, 0, 0, 0],
        [0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 0, 0],
        [0, 1, 1, 1, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 1, 1, 1],
        [0, 0, 1, 1, 2, 0, 1, 0, 2, 2, 2, 2, 2, 0, 1, 0, 2, 1, 1, 0],
        [1, 1, 1, 2, 2, 2, 0, 2, 2, 1, 1, 1, 2, 2, 0, 2, 2, 2, 1, 1],
        [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
        [1, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2],
        [1, 2, 2, 1, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 1, 2, 2],
        [1, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2],
        [1, 1, 2, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 2, 1],
        [0, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1],
        [0, 0, 1, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 1, 0],
        [0, 0, 0, 1, 2, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 2, 1, 0, 0],
        [0, 0, 0, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 0, 0]
    ]

    for ligne in range(NB_LIGNES):
        Grille_pixel.append([])

        for colonne in range(NB_COLONNES):
            x0, x1 = colonne * TAILLE_PIXEL, (colonne + 1) * TAILLE_PIXEL
            y0, y1 = ligne * TAILLE_PIXEL, (ligne + 1) * TAILLE_PIXEL
            if Table_Totoro[ligne][colonne] == 0:
                Grille_pixel[ligne].append(Canevas.create_rectangle(x0, y0, x1, y1, fill="white"))
            elif Table_Totoro[ligne][colonne] == 1:
                Grille_pixel[ligne].append(Canevas.create_rectangle(x0, y0, x1, y1, fill="black"))
            elif Table_Totoro[ligne][colonne] == 2:
                Grille_pixel[ligne].append(Canevas.create_rectangle(x0, y0, x1, y1, fill="lightgray"))
            elif Table_Totoro[ligne][colonne] == 3:
                Grille_pixel[ligne].append(Canevas.create_rectangle(x0, y0, x1, y1, fill="darkgreen"))
            elif Table_Totoro[ligne][colonne] == 4:
                Grille_pixel[ligne].append(Canevas.create_rectangle(x0, y0, x1, y1, fill="lightgreen"))

    def couleur00():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="black")

    def couleur01():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="lightgray")

    def couleur02():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="darkgreen")

    def couleur03():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="lightgreen")

    def couleur04():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="white")

    def couleur10():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="lightgray")

    def couleur11():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="darkgreen")

    def couleur12():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="lightgreen")

    def couleur13():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="white")

    def couleur14():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="black")

    def couleur20():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="darkgreen")

    def couleur21():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="lightgreen")

    def couleur22():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="white")

    def couleur23():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="black")

    def couleur24():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="lightgray")

    def couleur30():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 3:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="lightgreen")

    def couleur31():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 3:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="white")

    def couleur32():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 3:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="black")

    def couleur33():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 3:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="lightgray")

    def couleur34():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 3:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="darkgreen")

    def couleur40():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 4:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="white")

    def couleur41():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 4:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="black")

    def couleur42():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 4:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="lightgray")

    def couleur43():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 4:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="darkgreen")

    def couleur44():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 4:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="lightgreen")

    def DecVersHex1(nd1):
        nh1 = (nd1 // 16, nd1 % 16)
        ListeHex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        nh_str1 = ListeHex[nh1[0]] + ListeHex[nh1[1]]
        return nh_str1

    def DecVersHex2(nd2):
        nh2 = (nd2 // 16, nd2 % 16)
        ListeHex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        nh_str2 = ListeHex[nh2[0]] + ListeHex[nh2[1]]
        return nh_str2

    def DecVersHex3(nd3):
        nh3 = (nd3 // 16, nd3 % 16)
        ListeHex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        nh_str3 = ListeHex[nh3[0]] + ListeHex[nh3[1]]
        return nh_str3

    def aleatoiree1():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoiree2():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoiree3():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoiree4():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoiree5():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoire():
        couleur = aleatoiree1()
        couleur2 = aleatoiree2()
        couleur3 = aleatoiree3()
        couleur4 = aleatoiree4()
        couleur5 = aleatoiree5()
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur)
                elif Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur2)
                elif Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur3)
                elif Table_Totoro[ligne][colonne] == 3:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur4)
                elif Table_Totoro[ligne][colonne] == 4:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur5)

    Bouton0 = Button(fenetre, text="noire       " ,bg="white",command=couleur00)
    Bouton0.place(x=500, y=600)
    Bouton1 = Button(fenetre, text="gris         ",bg="white", command=couleur01)
    Bouton1.place(x=600, y=600)
    Bouton2 = Button(fenetre, text="vert foncé   ",bg="white", command=couleur02)
    Bouton2.place(x=700, y=600)
    Bouton3 = Button(fenetre, text="vert claire  ",bg="white", command=couleur03)
    Bouton3.place(x=800, y=600)
    Bouton4 = Button(fenetre, text="blanc        ",bg="white", command=couleur04)
    Bouton4.place(x=900, y=600)

    Bouton5 = Button(fenetre, text="gris         ",bg="black", fg="white",command=couleur10)
    Bouton5.place(x=500, y=650)
    Bouton6 = Button(fenetre, text="vert foncé   ",bg="black", fg="white", command=couleur11)
    Bouton6.place(x=600, y=650)
    Bouton7 = Button(fenetre, text="vert clair   ",bg="black", fg="white", command=couleur12)
    Bouton7.place(x=700, y=650)
    Bouton8 = Button(fenetre, text="blanc        ",bg="black", fg="white", command=couleur13)
    Bouton8.place(x=800, y=650)
    Bouton9 = Button(fenetre, text="noire        ",bg="black", fg="white", command=couleur14)
    Bouton9.place(x=900, y=650)

    Bouton10 = Button(fenetre, text="vert foncé   ",bg="lightgrey",command=couleur20)
    Bouton10.place(x=500, y=700)
    Bouton11 = Button(fenetre, text="vert claire  ",bg="lightgrey", command=couleur21)
    Bouton11.place(x=600, y=700)
    Bouton12 = Button(fenetre, text="blanc        ",bg="lightgrey", command=couleur22)
    Bouton12.place(x=700, y=700)
    Bouton13 = Button(fenetre, text="noire        ",bg="lightgrey", command=couleur23)
    Bouton13.place(x=800, y=700)
    Bouton14 = Button(fenetre, text="gris         ",bg="lightgrey", command=couleur24)
    Bouton14.place(x=900, y=700)

    Bouton15 = Button(fenetre, text="vert claire  ",bg="darkgreen", command=couleur30)
    Bouton15.place(x=500, y=750)
    Bouton16 = Button(fenetre, text="blanc        ",bg="darkgreen", command=couleur31)
    Bouton16.place(x=600, y=750)
    Bouton17 = Button(fenetre, text="noire        ",bg="darkgreen", command=couleur32)
    Bouton17.place(x=700, y=750)
    Bouton18 = Button(fenetre, text="gris         ",bg="darkgreen", command=couleur33)
    Bouton18.place(x=800, y=750)
    Bouton19 = Button(fenetre, text="vert foncé   ",bg="darkgreen", command=couleur34)
    Bouton19.place(x=900, y=750)

    Bouton20 = Button(fenetre, text="blanc        ",bg="lightgreen", command=couleur40)
    Bouton20.place(x=500, y=800)
    Bouton21 = Button(fenetre, text="noire        ",bg="lightgreen", command=couleur41)
    Bouton21.place(x=600, y=800)
    Bouton22 = Button(fenetre, text="gris         ",bg="lightgreen", command=couleur42)
    Bouton22.place(x=700, y=800)
    Bouton23 = Button(fenetre, text="vert foncé   ",bg="lightgreen", command=couleur43)
    Bouton23.place(x=800, y=800)
    Bouton24 = Button(fenetre, text="vert claire  ",bg="lightgreen", command=couleur44)
    Bouton24.place(x=900, y=800)

    huggy = Button(fenetre, text="Pixel Art Huggy Wuggy", font=("time", 20, "underline"), command=Huggy_Wuggy)
    huggy.place(x=675, y=150)
    poke = Button(fenetre, text="Pixel Art Pokémon", font=("time", 20, "underline"), command=Pokemon)
    poke.place(x=700, y=300)

    BoutonA = Button(fenetre, text="aleatoire", command=aleatoire)
    BoutonA.place(x=100, y=700)
def Huggy_Wuggy(): # pour créer les pixel Art Huggy Wuggy avec les bouton
    fenetre = Tk()
    fenetre.config(width=1000, height=800, bg='white')
    fenetre.title("Huggy_Wuggy (Pixel Art)")
    # bouton=input()
    Canevas = Canvas(fenetre, width=1000, height=1000, bg='white')
    Canevas.place(x=0, y=0)
    NB_LIGNES = 17
    NB_COLONNES = 19
    TAILLE_PIXEL = 35
    Grille_pixel = []
    Table_Totoro = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0],
        [0, 1, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 1, 0],
        [0, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 0],
        [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
        [0, 1, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 1, 0],
        [0, 1, 2, 2, 0, 1, 1, 0, 2, 2, 2, 0, 1, 1, 0, 2, 2, 1, 0],
        [0, 1, 2, 2, 0, 1, 1, 0, 2, 2, 2, 0, 1, 1, 0, 2, 2, 1, 0],
        [0, 1, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 1, 0],
        [0, 1, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 1, 0],
        [0, 0, 1, 2, 2, 3, 1, 3, 3, 3, 3, 3, 1, 3, 2, 2, 1, 0, 0],
        [0, 0, 1, 2, 2, 2, 3, 1, 1, 1, 1, 1, 3, 2, 2, 2, 1, 0, 0],
        [0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 3, 2, 2, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for ligne in range(NB_LIGNES):
        Grille_pixel.append([])

        for colonne in range(NB_COLONNES):
            x0, x1 = colonne * TAILLE_PIXEL, (colonne + 1) * TAILLE_PIXEL
            y0, y1 = ligne * TAILLE_PIXEL, (ligne + 1) * TAILLE_PIXEL
            if Table_Totoro[ligne][colonne] == 0:
                Grille_pixel[ligne].append(Canevas.create_rectangle(x0, y0, x1, y1, fill="white"))
            elif Table_Totoro[ligne][colonne] == 1:
                Grille_pixel[ligne].append(Canevas.create_rectangle(x0, y0, x1, y1, fill="black"))
            elif Table_Totoro[ligne][colonne] == 2:
                Grille_pixel[ligne].append(Canevas.create_rectangle(x0, y0, x1, y1, fill="Blue"))
            elif Table_Totoro[ligne][colonne] == 3:
                Grille_pixel[ligne].append(Canevas.create_rectangle(x0, y0, x1, y1, fill="Red"))

    def couleur00():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="black")

    def couleur01():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="blue")

    def couleur02():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="red")

    def couleur03():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="white")

    def couleur10():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="black")

    def couleur11():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="blue")

    def couleur12():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="red")

    def couleur13():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="white")

    def couleur20():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="black")

    def couleur21():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="blue")

    def couleur22():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="red")

    def couleur23():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="white")

    def couleur30():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 3:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="black")

    def couleur31():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 3:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="blue")

    def couleur32():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 3:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="red")

    def couleur33():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 3:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="white")

    def DecVersHex1(nd1):
        nh1 = (nd1 // 16, nd1 % 16)
        ListeHex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        nh_str1 = ListeHex[nh1[0]] + ListeHex[nh1[1]]
        return nh_str1

    def DecVersHex2(nd2):
        nh2 = (nd2 // 16, nd2 % 16)
        ListeHex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        nh_str2 = ListeHex[nh2[0]] + ListeHex[nh2[1]]
        return nh_str2

    def DecVersHex3(nd3):
        nh3 = (nd3 // 16, nd3 % 16)
        ListeHex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        nh_str3 = ListeHex[nh3[0]] + ListeHex[nh3[1]]
        return nh_str3

    def aleatoiree1():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoiree2():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoiree3():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoiree4():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoiree5():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoire():
        couleur = aleatoiree1()
        couleur2 = aleatoiree2()
        couleur3 = aleatoiree3()
        couleur4 = aleatoiree4()
        couleur5 = aleatoiree5()
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur)
                elif Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur2)
                elif Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur3)
                elif Table_Totoro[ligne][colonne] == 3:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur4)
                elif Table_Totoro[ligne][colonne] == 4:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur5)

    Bouton0 = Button(fenetre, text="noire        ",bg="white", command=couleur00)
    Bouton0.place(x=500, y=600)
    Bouton1 = Button(fenetre, text="bleu        ",bg="white", command=couleur01)
    Bouton1.place(x=600, y=600)
    Bouton2 = Button(fenetre, text="rouge   ",bg="white", command=couleur02)
    Bouton2.place(x=700, y=600)
    Bouton3 = Button(fenetre, text="blanc  ",bg="white", command=couleur03)
    Bouton3.place(x=800, y=600)

    Bouton5 = Button(fenetre, text="noire         ",bg="black", fg="white", command=couleur10)
    Bouton5.place(x=500, y=650)
    Bouton6 = Button(fenetre, text="bleu   ",bg="black", fg="white", command=couleur11)
    Bouton6.place(x=600, y=650)
    Bouton7 = Button(fenetre, text="rouge   ",bg="black", fg="white", command=couleur12)
    Bouton7.place(x=700, y=650)
    Bouton8 = Button(fenetre, text="blanc        ",bg="black", fg="white", command=couleur13)
    Bouton8.place(x=800, y=650)

    Bouton10 = Button(fenetre, text="noire    ",bg="blue",fg="white", command=couleur20)
    Bouton10.place(x=500, y=700)
    Bouton11 = Button(fenetre, text="bleu  ",bg="blue",fg="white", command=couleur21)
    Bouton11.place(x=600, y=700)
    Bouton12 = Button(fenetre, text="rouge        ",bg="blue",fg="white", command=couleur22)
    Bouton12.place(x=700, y=700)
    Bouton13 = Button(fenetre, text="blanc        ",bg="blue",fg="white", command=couleur23)
    Bouton13.place(x=800, y=700)

    Bouton15 = Button(fenetre, text="noire  ",bg="red", command=couleur30)
    Bouton15.place(x=500, y=750)
    Bouton16 = Button(fenetre, text="bleu        ",bg="red", command=couleur31)
    Bouton16.place(x=600, y=750)
    Bouton17 = Button(fenetre, text="rouge        ",bg="red", command=couleur32)
    Bouton17.place(x=700, y=750)
    Bouton18 = Button(fenetre, text="blanc         ",bg="red", command=couleur33)
    Bouton18.place(x=800, y=750)

    poke= Button(fenetre, text="Pixel Art Pokémon",font=("time", 20, "underline"),command=Pokemon)
    poke.place(x=700 ,y=150)
    totoro2 = Button(fenetre, text="Pixel Art Totoro", font=("time", 20, "underline"), command=Totoro)
    totoro2.place(x=700, y=300)

    BoutonA = Button(fenetre, text="aleatoire", command=aleatoire)
    BoutonA.place(x=100, y=700)
def Pokemon(): # pour créer les pixel Art Pokémon avec les bouton
    fenetre = Tk()
    fenetre.config(width=1000, height=800, bg='white')
    fenetre.title("Pokémon (Pixel Art)")
    # bouton=input()
    Canevas = Canvas(fenetre, width=1000, height=1000, bg='white')
    Canevas.place(x=0, y=0)
    NB_LIGNES = 16
    NB_COLONNES = 18
    TAILLE_PIXEL = 35
    Table_Totoro = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0],
        [0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0],
        [0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 0, 0, 0],
        [0, 0, 0, 1, 2, 2, 2, 2, 1, 0, 0, 1, 2, 2, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    Grille_pixel = []
    for ligne in range(NB_LIGNES):
        Grille_pixel.append([])

        for colonne in range(NB_COLONNES):
            x0, x1 = colonne * TAILLE_PIXEL, (colonne + 1) * TAILLE_PIXEL
            y0, y1 = ligne * TAILLE_PIXEL, (ligne + 1) * TAILLE_PIXEL
            if Table_Totoro[ligne][colonne] == 0:
                Grille_pixel[ligne].append(Canevas.create_rectangle(x0, y0, x1, y1, fill="white"))
            elif Table_Totoro[ligne][colonne] == 1:
                Grille_pixel[ligne].append(Canevas.create_rectangle(x0, y0, x1, y1, fill="black"))
            elif Table_Totoro[ligne][colonne] == 2:
                Grille_pixel[ligne].append(Canevas.create_rectangle(x0, y0, x1, y1, fill="red"))

    def couleur00():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="black")

    def couleur01():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="white")

    def couleur02():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="red")

    def couleur10():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="black")

    def couleur11():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="white")

    def couleur12():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="red")

    def couleur20():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="black")

    def couleur21():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="white")

    def couleur22():
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="red")

    def DecVersHex1(nd1):
        nh1 = (nd1 // 16, nd1 % 16)
        ListeHex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        nh_str1 = ListeHex[nh1[0]] + ListeHex[nh1[1]]
        return nh_str1

    def DecVersHex2(nd2):
        nh2 = (nd2 // 16, nd2 % 16)
        ListeHex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        nh_str2 = ListeHex[nh2[0]] + ListeHex[nh2[1]]
        return nh_str2

    def DecVersHex3(nd3):
        nh3 = (nd3 // 16, nd3 % 16)
        ListeHex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        nh_str3 = ListeHex[nh3[0]] + ListeHex[nh3[1]]
        return nh_str3

    def aleatoiree1():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoiree2():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoiree3():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoiree4():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoiree5():
        nd1 = randint(0, 255)
        nd2 = randint(0, 255)
        nd3 = randint(0, 255)
        return DecVersHex1(nd1) + DecVersHex2(nd2) + DecVersHex3(nd3)

    def aleatoire():
        couleur = aleatoiree1()
        couleur2 = aleatoiree2()
        couleur3 = aleatoiree3()
        couleur4 = aleatoiree4()
        couleur5 = aleatoiree5()
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if Table_Totoro[ligne][colonne] == 0:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur)
                elif Table_Totoro[ligne][colonne] == 1:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur2)
                elif Table_Totoro[ligne][colonne] == 2:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur3)
                elif Table_Totoro[ligne][colonne] == 3:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur4)
                elif Table_Totoro[ligne][colonne] == 4:
                    Canevas.itemconfig(Grille_pixel[ligne][colonne], fill="#" + couleur5)

    Bouton0 = Button(fenetre, text="noire        ",bg="white", command=couleur00)
    Bouton0.place(x=500, y=600)
    Bouton1 = Button(fenetre, text="blanc        ",bg="white", command=couleur01)
    Bouton1.place(x=600, y=600)
    Bouton2 = Button(fenetre, text="rouge   ",bg="white", command=couleur02)
    Bouton2.place(x=700, y=600)

    Bouton5 = Button(fenetre, text="noire         ",bg="black", fg="white", command=couleur10)
    Bouton5.place(x=500, y=650)
    Bouton6 = Button(fenetre, text="blanc   ",bg="black", fg="white", command=couleur11)
    Bouton6.place(x=600, y=650)
    Bouton7 = Button(fenetre, text="rouge   ",bg="black", fg="white", command=couleur12)
    Bouton7.place(x=700, y=650)

    Bouton10 = Button(fenetre, text="noire    ",bg="red", command=couleur20)
    Bouton10.place(x=500, y=700)
    Bouton11 = Button(fenetre, text="blanc  ",bg="red", command=couleur21)
    Bouton11.place(x=600, y=700)
    Bouton12 = Button(fenetre, text="rouge        ",bg="red", command=couleur22)
    Bouton12.place(x=700, y=700)

    huggy= Button(fenetre, text="Pixel Art Huggy Wuggy",font=("time",20,"underline"), command=Huggy_Wuggy)
    huggy.place(x=675, y=150)
    totoro2=Button(fenetre, text="Pixel Art Totoro",font=("time",20,"underline"), command=Totoro)
    totoro2.place(x=700, y=300)

    BoutonA = Button(fenetre, text="aleatoire", command=aleatoire)
    BoutonA.place(x=100, y=700)

totoro=Button(fenetre,text="Totoro", font=("times",30,"bold"), command=Totoro)
huggy=Button(fenetre, text="Huggy Wuggy", font=("times",30,"bold"),command=Huggy_Wuggy)
pokemon=Button(fenetre,text="Pokémon", font=("times",30,"bold"),command=Pokemon)
totoro.place(x=100, y=300)
huggy.place(x=340, y=300)
pokemon.place(x=700, y=300)

fenetre.mainloop() # pour afficher les fenetre