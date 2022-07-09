import webbrowser
import requests
import win32api
import threading
from tkinter import *
from tkinter import ttk #Ezekkel beimportáltuk a szükséges dolgokat a Tkinterből. Ez kell a GUI megvalsításához
from db_manager import db_close, db_query, db_insert
from tkinter import ttk, messagebox
import login
__version__ = '1.2'
_AppName_ = 'Adatbázis'
__Owner__ = "Szép Szilveszter"
#db_create()

def check_updates():
    try:
        response = requests.get(
            'https://raw.githubusercontent.com/szepszilo/database/main/version.txt')
        data = response.text

        if float(data) > float(__version__):
            messagebox.showinfo('Szoftver frissítés', 'Frissítés elérhető!')
            mb1 = messagebox.askyesno('Frissítés!', f'{_AppName_} {__version__} szoftverhez elérhető frissítés: {data}')
            if mb1 is True:
                # -- Replace the url for your file online with the one below.
                webbrowser.open_new_tab('https://raw.githubusercontent.com/szepszilo/database/main/'
                                        'update.msi?raw=true')
                #parent.destroy()
            else:
                pass
        else:
            messagebox.showinfo('Szoftver frissítés', 'Nincs elérhető frissítés.')
    except Exception as e:
        messagebox.showinfo('Szoftver frissítés', 'Frissítés ellenőrzés sikertelen, hiba:' + str(e))

def nevjegy():
    nevjegy = Toplevel(win)
    nevjegy.geometry('200x100')
    nevjegy.resizable(False, False)
    nevjegy.configure(background="#d3d5d2", height=200, width=200)
    Label(nevjegy,background="#d3d5d2", text="Készítette: Szép Szilveszter\nAdatbázis beta v1.2\n email: szep.code@gmail.com").pack()
    Button(nevjegy, background="#c6e1e1", font="{arial} 10 {}", text="Frissítés keresése", command=check_updates).place(anchor="nw", relwidth=0.60, relx=0.20, rely=0.60, x=0, y=0)

def adatbazis():
    adatbazis = Toplevel(win)
    adatbazis.geometry('800x270')
    adatbazis.configure(background="#d3d5d2", height=800, width=270)
    Button(adatbazis, background="#c6e1e1", font="{arial} 10 {}", text="Lekérdez", command=lambda:db_query(table)).place(anchor="nw",relwidth=0.20,relx=0.20, rely=0.86,x=0, y=0)
    Button(adatbazis, background="#c6e1e1", font="{arial} 10 {}", text="exportálás CSV-be").place(anchor="nw", relwidth=0.20,
                                                                                         relx=0.60, rely=0.86, x=0, y=0)
    cols = ("Id", "Vezetéknév", "Keresztnév", "Születési hely", "Születési idő", "Nem", "Lakcím")
    table = ttk.Treeview(adatbazis, columns=cols, show="headings")
    for col in cols:
        table.heading(col, text=col)
    table.place(anchor="nw",relwidth=1,relx=0.0, rely=0.0,x=0, y=0)
    adatbazis.resizable(False, False)

def mainsoft():
    global win
    win= Tk() # Ezzel megadtuk hogy a win változó a Tk azaz ő lesz maga a GUI
    win.title("Adatbazis v1.2") #Ablak neve
    win.geometry("400x500")    #Ablak mérete
    win.configure(background="#d3d5d2", height=200, width=200)
    win.resizable(False, False) #Ablak méretének modositása horizontálisan és vertikálisan



    ####################
    Button(win, background="#c6e1e1", font="{arial} 10 {}", text="Névjegy", command=nevjegy).place(anchor="nw", relwidth=0.31, relx=0.60, rely=0.03, x=0, y=0)
    Button(win, background="#c6e1e1", font="{arial} 10 {}", text="Adatbázis", command=adatbazis).place(anchor="nw", relwidth=0.31, relx=0.05, rely=0.90, x=0, y=0)
    Button(win, background="#c6e1e1", font="{arial} 10 {}", text="Alkalmazás", command=lambda:db_insert(vnev, knev, szulhely, szulido, nem, lakcim)).place(anchor="nw", relwidth=0.31, relx=0.50, rely=0.90, x=0, y=0)

    ####################

    Label(win, text="Adatbázis beta v1.2", font="{Arial} 16 {bold}", foreground="#a2cece", background="#d3d5d2").place(anchor="nw", rely=0.03, x=0, y=0)

    Label(win, background="#d3d5d2", font="{arial} 12 {}", text="Vezetéknév:").place(anchor="nw", relx=0.05, rely=0.10, x=0, y=0)
    vnev = Entry (win)
    vnev.place(anchor="nw", relx=0.33, rely=0.109, x=0, y=0)

    Label(win, background="#d3d5d2", font="{arial} 12 {}", text="Keresztnév:").place(anchor="nw", relx=0.05, rely=0.20, x=0, y=0)
    knev = Entry (win)
    knev.place(anchor="nw", relx=0.33, rely=0.209, x=0, y=0)

    Label(win, background="#d3d5d2", font="{arial} 12 {}", text="Születés helye:").place(anchor="nw", relx=0.05, rely=0.30, x=0, y=0)
    szulhely = Entry (win)
    szulhely.place(anchor="nw", relx=0.33, rely=0.309, x=0, y=0)

    Label(win, background="#d3d5d2", font="{arial} 12 {}", text="Születés ideje:").place(anchor="nw", relx=0.05, rely=0.40, x=0, y=0)
    szulido = Entry (win)
    szulido.place(anchor="nw", relx=0.33, rely=0.409, x=0, y=0)

    Label(win, background="#d3d5d2", font="{arial} 12 {}", text="Nem:").place(anchor="nw", relx=0.05, rely=0.50, x=0, y=0)
    nem = StringVar(win)
    nem.set("Válaszd ki a nemet.")
    nemek = OptionMenu(win, nem, "férfi", "nő", "egyéb")
    nemek.place(anchor="nw", relx=0.33, rely=0.490, x=0, y=0)

    Label(win, background="#d3d5d2", font="{arial} 12 {}", text="Lakcím:").place(anchor="nw", relx=0.05, rely=0.60, x=0, y=0)
    lakcim = Entry (win)
    lakcim.place(anchor="nw", relx=0.33, rely=0.609, x=0, y=0)

    win.mainloop()

db_close()