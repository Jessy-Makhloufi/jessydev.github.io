#Programme réaliser par Makhloufi Jessy
from tkinter import*
#from tkinter import* pour créer une interface graphique
fenetre=Tk()
fenetre.config(width=1000,height=800, bg='#F0FFF0') #fentre=Tk() pour créer une fenetre et lui donné des configuration comme ça taille
fenetre.title("Convertisseur")#pour donner un titre à la fenetre
Text=Label(text="Convertisseur Binaire, Hexadécimale, Décimale", bg='#F0FFF0', font=('times',30,'bold','underline'))
#Label pour créer du texte sur la fenetre
Texte=Label(text="Binaire : 00000000", fg='#FF7F50', font=('times',20,'bold'))
Texte1=Label(text="Décimale : 000", fg='#FF7F50', font=('times',20,'bold'))
Texte2=Label(text="Héxadécimale : 00", fg='#FF7F50', font=('times',20,'bold'))
Texte3=Label(text="Décimale : 000", fg='#1E90FF', font=('times',20,'bold'))
Texte4=Label(text="Binaire : 00000000", fg='#1E90FF', font=('times',20,'bold'))
Texte5=Label(text="Héxadécimale : 00", fg='#1E90FF', font=('times',20,'bold'))
#.place pour les placer dans la fenetre
Text.place(x=100, y=75)
Texte.place(x=100, y=300)
Texte1.place(x=100, y=330)
Texte2.place(x=100, y=360)
Texte3.place(x=100, y=500)
Texte4.place(x=100, y=530)
Texte5.place(x=100, y=560)
#def pour créer des définition qui changerons le nombre sur le bouton
def action():
    etat=Bouton.cget('text')
    #.cget('text') pour récupéere le chiffre du bouton
    if etat=='0':
        Bouton.config(text='1',fg='red')
    else:
        Bouton.config(text='0',fg='black')
def action1():
    etat1=Bouton1.cget('text')
    if etat1=='0':
        Bouton1.config(text='1',fg='red')
    else:
        Bouton1.config(text='0',fg='black')
def action2():
    etat2=Bouton2.cget('text')
    if etat2=='0':
        Bouton2.config(text='1',fg='red')
    else:
        Bouton2.config(text='0',fg='black')
def action3():
    etat3=Bouton3.cget('text')
    if etat3=='0':
        Bouton3.config(text='1',fg='red')
    else:
        Bouton3.config(text='0',fg='black')
def action4():
    etat4=Bouton4.cget('text')
    if etat4=='0':
        Bouton4.config(text='1',fg='red')
    else:
        Bouton4.config(text='0',fg='black')
def action5():
    etat5=Bouton5.cget('text')
    if etat5=='0':
        Bouton5.config(text='1',fg='red')
    else:
        Bouton5.config(text='0',fg='black')
def action6():
    etat6=Bouton6.cget('text')
    if etat6=='0':
        Bouton6.config(text='1',fg='red')
    else:
        Bouton6.config(text='0',fg='black')
def action7():
    etat7=Bouton7.cget('text')
    if etat7=='0':
        Bouton7.config(text='1',fg='red')
    else:
        Bouton7.config(text='0',fg='black')
def actionall():
    action()
    action1()
    action2()
    action3()
    action4()
    action5()
    action6()
    action7()
def action8():
    etat8=Bouton8.cget('text')
    if etat8 == '0':
         Bouton8.config(text='1', fg='red')
    elif etat8 == '1':
           Bouton8.config(text='2', fg='red')
    elif etat8 == '2':
          Bouton8.config(text='3', fg='red')
    elif etat8 == '3':
          Bouton8.config(text='4', fg='red')
    elif etat8 == '4':
          Bouton8.config(text='5', fg='red')
    elif etat8 == '5':
          Bouton8.config(text='6', fg='red')
    elif etat8 == '6':
         Bouton8.config(text='7', fg='red')
    elif etat8 == '7':
          Bouton8.config(text='8', fg='red')
    elif etat8 == '8':
         Bouton8.config(text='9', fg='red')
    elif etat8 == '9':
         Bouton8.config(text='0', fg='black')
def action9():
    etat9=Bouton9.cget('text')
    if etat9 == '0':
          Bouton9.config(text='1', fg='red')
    elif etat9 == '1':
         Bouton9.config(text='2', fg='red')
    elif etat9 == '2':
         Bouton9.config(text='3', fg='red')
    elif etat9 == '3':
         Bouton9.config(text='4', fg='red')
    elif etat9 == '4':
         Bouton9.config(text='5', fg='red')
    elif etat9 == '5':
        Bouton9.config(text='6', fg='red')
    elif etat9 == '6':
            Bouton9.config(text='7', fg='red')
    elif etat9 == '7':
         Bouton9.config(text='8', fg='red')
    elif etat9 == '8':
        Bouton9.config(text='9', fg='red')
    elif etat9 == '9':
            Bouton9.config(text='0', fg='black')
def action10():
    etat10=Bouton10.cget('text')
    if etat10 == '0':
        Bouton10.config(text='1', fg='red')
    elif etat10 == '1':
        Bouton10.config(text='2', fg='red')
    elif etat10 == '2':
        Bouton10.config(text='3', fg='red')
    elif etat10 == '3':
        Bouton10.config(text='4', fg='red')
    elif etat10 == '4':
        Bouton10.config(text='5', fg='red')
    elif etat10 == '5':
        Bouton10.config(text='6', fg='red')
    elif etat10 == '6':
        Bouton10.config(text='7', fg='red')
    elif etat10 == '7':
        Bouton10.config(text='8', fg='red')
    elif etat10 == '8':
        Bouton10.config(text='9', fg='red')
    elif etat10 == '9':
        Bouton10.config(text='0', fg='black')
def actionall2():
    action8()
    action9()
    action10()
#Bouton=Button pour créer des bouton sur l'interface graphique
Bouton=Button(fenetre, text='0',font=('times',25,'bold'), command=action)
#et Bouton.place pour placer les bouton
Bouton.place(x=50, y=200)
Bouton1=Button(fenetre, text='0', font=('times',25,'bold'), command=action1)
Bouton1.place(x=100, y=200)
Bouton2=Button(fenetre, text='0', font=('times',25,'bold'), command=action2)
Bouton2.place(x=150, y=200)
Bouton3=Button(fenetre, text='0', font=('times',25,'bold'), command=action3)
Bouton3.place(x=200, y=200)
Bouton4=Button(fenetre, text='0', font=('times',25,'bold'), command=action4)
Bouton4.place(x=250, y=200)
Bouton5=Button(fenetre, text='0', font=('times',25,'bold'), command=action5)
Bouton5.place(x=300, y=200)
Bouton6=Button(fenetre, text='0', font=('times',25,'bold'), command=action6)
Bouton6.place(x=350, y=200)
Bouton7=Button(fenetre, text='0', font=('times',25,'bold'), command=action7)
Bouton7.place(x=400, y=200)
Boutonall1=Button(fenetre, text='Change tout les boutons',font=('times',20,'bold'), command=actionall)
Boutonall1.place(x=460, y=200)
Bouton8=Button(fenetre, text='0', font=('times',25,'bold'), command=action8)
Bouton8.place(x=50,y=400)
Bouton9=Button(fenetre, text='0', font=('times',25,'bold'), command=action9)
Bouton9.place(x=100,y=400)
Bouton10=Button(fenetre, text='0', font=('times',25,'bold'), command=action10)
Bouton10.place(x=150,y=400)
Boutonall2=Button(fenetre, text='Change tout les boutons', font=('times',20,'bold'), command=actionall2)
Boutonall2.place(x=350, y=500)
#definition pour convertir du binaire en décimale
def BinVersDec(nb):
    nd = 0
    for bit in nb:
        nd = nd * 2 + int(bit)
    return nd
#definition pour convertir du décimale en hexadécimale
def DecVersHex(nd): # Pour nd < 4095
    nh=(nd//16**2,nd//16,nd%16)
    return hex(nd)[2:].upper()
#pour récuperer les nombre des bouton et les transmettre au definition qui les convertira
def modification1():
    etat = Bouton.cget('text')
    etat1 = Bouton1.cget('text')
    etat2 = Bouton2.cget('text')
    etat3 = Bouton3.cget('text')
    etat4 = Bouton4.cget('text')
    etat5 = Bouton5.cget('text')
    etat6 = Bouton6.cget('text')
    etat7 = Bouton7.cget('text')
    base2=etat+etat1+etat2+etat3+etat4+etat5+etat6+etat7
    bin=BinVersDec(nb=base2)
    hexa=DecVersHex(nd=bin)
    #.config pour modifer le texte de la fenetre et afficher les résultat des convertion
    Texte.config(text='Binaire : '+str(base2))
    Texte1.config(text='Décimale : '+str(bin))
    Texte2.config(text='Héxadécimale : '+str(hexa))
Boutonm=Button(fenetre,text='Bin > Déc et Hex', font=('times',20,'bold'), command=modification1)
Boutonm.place(x=777, y=200)
def DecVersBin(nd):
    nb = ''
    while nd != 0 :
        nb = str(nd % 2) + nb
        nd = nd // 2
    return nb
def DecVersHex1(nd):
    nh=(nd//16**2,nd//16,nd%16)
    return hex(nd)[2:].upper()
def modification2():
    etat8 = Bouton8.cget('text')
    etat9 = Bouton9.cget('text')
    etat10 = Bouton10.cget('text')
    base_10=int(etat8+etat9+etat10)
    dec=DecVersBin(nd=base_10)
    dec1=DecVersHex1(nd=base_10)
    Texte3.config(text="Decimale : "+str(base_10))
    Texte4.config(text="Binaire : "+str(dec))
    Texte5.config(text="Héxadécimale : "+str(dec1))
Boutonn=Button(fenetre,text="Déc > Bin et Hex", font=('times',20,'bold'), command=modification2)
Boutonn.place(x=700, y=500)
#fenetre.mainloop() pour afficher la fenetre
fenetre.mainloop()