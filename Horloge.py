from tkinter import*
from math import*
from time import*
fenetre= Tk()
fenetre.config(width=700 ,height=700)
fenetre.title("Makhloufi Jessy")
Canevas=Canvas(fenetre, width=700, height=700, background='White')
Canevas.place(x=0,y=0)
fenetre.config(background='Black')
Canevas.create_oval(95,100,600,600,fill='White',outline='WHite')
Horlogenormal = PhotoImage(file="Horloge 1.gif")
Horloge1 = Canevas.create_image(345, 350, image=Horlogenormal)

def _1():
    global angle_heure
    angle_heure=angle_heure+30
    x_heure, y_heure = Heure(345, 350, 100, angle_heure)
    Canevas.coords(Aiguille_heure, 345,350,x_heure, y_heure)
def __1():
    global angle_heure
    angle_heure = angle_heure - 30
    x_heure, y_heure = Heure(345, 350, 100, angle_heure)
    Canevas.coords(Aiguille_heure, 345, 350, x_heure, y_heure)

def _1m():
    global angle_Minute
    angle_Minute= angle_Minute + 6
    x_minute, y_minute = Minute(345, 350, 250, angle_Minute)
    Canevas.coords(Aiguille_minute, 345, 350, x_minute, y_minute)

def __1m():
    global angle_Minute
    angle_Minute = angle_Minute - 6
    x_minute, y_minute = Minute(345, 350, 250, angle_Minute)
    Canevas.coords(Aiguille_minute, 345, 350, x_minute, y_minute)

def nuit():
        Canevas.config(background='Black')
        Hologe1 = Canevas.create_image(345, 350, image=Horlogenormal)

def jour():
    Canevas.config(background='White')
    Hologe1 = Canevas.create_image(345, 350, image=Horlogenormal)

def syncro():
    global angle_heure,angle_Minute,angle_seconde
    heure=strftime("%H")
    angle_heure = (int(heure)/12*360)
    x_heure, y_heure = Heure(345, 350, 100, angle_heure)
    Canevas.coords(Aiguille_heure, 345, 350, x_heure, y_heure)
    minute=strftime("%M")
    angle_Minute = (int(minute)/60*360)
    x_minute, y_minute = Minute(345, 350, 250, angle_Minute)
    Canevas.coords(Aiguille_minute, 345, 350, x_minute, y_minute)
    Seconde=strftime("%S")
    angle_seconde = (int(Seconde)/60*360)
    x_seconde, y_seconde = seconde(345, 350, 220, angle_seconde)
    Canevas.coords(Aiguille_seconde,345, 350, x_seconde, y_seconde)

Bouton1h=Button(fenetre,text="+ 1h",font=('Time',20,'bold'),command=_1)
Bouton1h.place(x=50,y=0)
Bouton1H=Button(fenetre,text="- 1h",font=('Time',20,'bold'),command=__1)
Bouton1H.place(x=575,y=0)
Bouton1m=Button(fenetre,text="+ 1min", font=('Time',20,'bold'),command=_1m)
Bouton1m.place(x=40,y=645)
Bouton1M=Button(fenetre,text="- 1min", font =('Time',20,'bold'),command=__1m)
Bouton1M.place(x=565,y=645)
Boutonnuit=Button(fenetre,text='nuit', font=('Time',20,'bold'),command=nuit)
Boutonnuit.place(x=0,y=315)
Boutonjour=Button(fenetre,text='Jour', font=('Time',20,'bold'),command=jour)
Boutonjour.place(x=615,y=315)
Boutonsyncro=Button(fenetre, text='Syncronisation', font = ('Time',20,'bold'),command=syncro)
Boutonsyncro.place(x=250, y=0)

def Heure(x_centre, y_centre, longueur_aiguille, angle_en_degre):
    angle_radian = angle_en_degre / 360 * 2 * pi
    x_extrem = x_centre + longueur_aiguille * sin(angle_radian)
    y_extrem = y_centre - longueur_aiguille * cos(angle_radian)
    return x_extrem, y_extrem
angle_heure = (12 / 12 * 360)
x_heure,y_heure = Heure(345,350,100,angle_heure)
Aiguille_heure = Canevas.create_line(345,350,x_heure,y_heure,width=4)
def Minute(x_centre, y_centre, longueur_aiguille, angle_en_degre):
    angle_radian = angle_en_degre / 360 * 2 * pi
    x_extrem = x_centre + longueur_aiguille * sin(angle_radian)
    y_extrem = y_centre - longueur_aiguille * cos(angle_radian)
    return x_extrem, y_extrem
angle_Minute = (15/ 60 * 360)
x_minute,y_minute = Minute(345,350,200,angle_Minute)
Aiguille_minute = Canevas.create_line(345,350,x_minute,y_minute,width=4)
def seconde(x_centre, y_centre, longueur_aiguille, angle_en_degre):
    angle_radian = angle_en_degre / 360 * 2 * pi
    x_extrem = x_centre + longueur_aiguille * sin(angle_radian)
    y_extrem = y_centre - longueur_aiguille * cos(angle_radian)
    return x_extrem, y_extrem
angle_seconde = (1800 / 60 * 360)
x_seconde,y_seconde = seconde(345,350,220,angle_seconde)
Aiguille_seconde = Canevas.create_line(345,350,x_seconde,y_seconde,width=2)

fenetre.mainloop()