from tkinter import *
from tkinter import ttk #Ezekkel beimportáltuk a szükséges dolgokat a Tkinterből. Ez kell a GUI megvalsításához
import mysql.connector
from mysql.connector import Error

curs = None
conn = None
def nextPage():

    from app import mainsoft
    mainsoft()

#
def mysql_conn(server, databasename, username, password):
    global conn, curs
    try:
        conn = mysql.connector.connect(host=server.get(),
                                             database=databasename.get(),
                                             user=username.get(),
                                             password=password.get())

        # conn = mysql.connector.connect(host='sql11.freemysqlhosting.net',
        #                                      database='sql11504863',
        #                                      user='sql11504863',
        #                                      password='aYmX6DHsyX')
        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("A csatlakozott MySQL verziója:", db_Info)
            curs = conn.cursor()
            curs.execute("select database();")
            record = curs.fetchone()

            print("Csatlakoztál az adatbázishoz: ", record)
            curs.execute(
                "CREATE TABLE IF NOT EXISTS users (vnev TEXT, knev TEXT, szulhely TEXT, szulido TEXT, nem TEXT, lakcim TEXT)")

    except Error as e:
        print("Hiba a MySQL kapcsolodása közben:", e)
        hibasql = Tk()
        hibasql.title("Hiba")
        hibasql.resizable(False, False)
        hibasql.geometry('200x50')
        hibasql.configure(background="#d3d5d2", height=200, width=50)
        Label(hibasql, background="#d3d5d2",
              text="Sikertelen bejelentkezés.").pack()
        return
    # finally:
    #     if conn.is_connected():
    #         curs.close()
    #         conn.close()
    #         print("MySQL connection is closed")




def db_create():
    global conn, curs
    conn = sqlite3.connect("data/data.db")
    curs = conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS users (vnev TEXT, knev TEXT, szulhely TEXT, szulido TEXT, nem TEXT, lakcim TEXT)")


def db_insert(vnev, knev, szulhely, szulido, nem, lakcim):
    if not vnev.get() or not knev.get() or not szulhely.get() or not szulido.get() or nem.get() =="Válaszd ki a nemet." or not lakcim.get():
        hiba=Tk()
        hiba.title("hiba")
        hiba.resizable(False, False)
        hiba.geometry('200x50')
        hiba.configure(background="#d3d5d2", height=200, width=50)
        Label(hiba, background="#d3d5d2",
              text="Összes mezőt ki kell tölteni!").pack()

        return

    curs.execute("INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)", (vnev.get(), knev.get(),
                                szulhely.get(), szulido.get(), nem.get(), lakcim.get()))
    conn.commit()
    vnev.delete(0, 'end')
    knev.delete(0, 'end')
    szulhely.delete(0, 'end')
    szulido.delete(0, 'end')
    lakcim.delete(0, 'end')

def db_query(table):
    curs.execute("SELECT * FROM users")
    datas = curs.fetchall()
    table.delete(*table.get_children())
    rowid = 1
    for data in datas:
        table.insert("", "end", values=(rowid, data[0],data[1],data[2],data[3],data[4],data[5]))
        rowid += 1
def db_close():
    if conn and curs:
        curs.close()
        conn.close()
        print("MySQL kapcsolat bezárva")

