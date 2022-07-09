
from app import *

from db_manager import mysql_conn

def nextPage():
    login1.destroy()
    mainsoft()
def loginform():
    global login1
    login1 = Tk()
    login1.title("MySQL bejelentkezés")
    login1.geometry("300x400")
    login1.configure(background="#d3d5d2", height=300, width=400)
    login1.resizable(False, False)

    Label(login1, text="Bejelentkezés az adatbázisba", font="{Arial} 15 {bold}", foreground="#000000", background="#d3d5d2").place(anchor="nw", rely=0.05, relx=0.03, x=0, y=0)
    Label(login1, background="#d3d5d2", font="{arial} 12 {}", text="Kiszolgáló:").place(anchor="nw", relx=0.05, rely=0.25, x=0, y=0)
    server = Entry (login1)
    server.place(anchor="nw", relx=0.50, rely=0.259, x=0, y=0)

    Label(login1, background="#d3d5d2", font="{arial} 12 {}", text="Adatbázis:").place(anchor="nw", relx=0.05, rely=0.40, x=0, y=0)
    databasename = Entry (login1)
    databasename.place(anchor="nw", relx=0.50, rely=0.409, x=0, y=0)

    Label(login1, background="#d3d5d2", font="{arial} 12 {}", text="Felhasználónév:").place(anchor="nw", relx=0.05, rely=0.55, x=0, y=0)
    username = Entry (login1)
    username.place(anchor="nw", relx=0.50, rely=0.559, x=0, y=0)

    Label(login1, background="#d3d5d2", font="{arial} 12 {}", text="Jelszó:").place(anchor="nw", relx=0.05, rely=0.70, x=0, y=0)
    password = Entry (login1)
    password.place(anchor="nw", relx=0.50, rely=0.709, x=0, y=0)

    Button(login1, background="#c6e1e1", font="{arial} 10 {}", text="Bejelentkezés", command=lambda:mysql_conn(server, databasename, username, password) & nextPage()).place(anchor="nw", relwidth=0.31, relx=0.50, rely=0.85, x=0, y=0)

    login1.mainloop()

loginform()