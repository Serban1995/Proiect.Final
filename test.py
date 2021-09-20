from tkinter import *

import sqlite3

root = Tk()
root.title("test baza de date")
root.geometry("800x500")


conn = sqlite3.connect("test_baza_de_date.db")
c = conn.cursor()
# funtia submit
def submit():
    conn = sqlite3.connect("test_baza_de_date.db")
    c = conn.cursor()
    # c.execute("CREATE TABLE users(user)")
    c.execute("INSERT INTO users VALUES (:user)",
              {
                "user": user.get()})





    conn.commit()
    conn.close()
    user.delete(0, END)
def query():
    conn = sqlite3.connect("test_baza_de_date.db")
    c = conn.cursor()
    c.execute("SELECT *, oid FROM users")
    records = c.fetchall()
    print(records)
    print_records = ""
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=9, column=0, columnspan=2)



    conn.commit()
    conn.close()

user = Entry(root, width=30)
user.grid(row=0, column=1, padx=20)
user_label = Label(root, text="User Name")
user_label.grid(row=0, column=0)
# se face un buton in prima faza pentru submit
submit_btn = Button(root, text= "adauga in baza de date", command= submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
# buton care afiseaza intrarile
query_btn = Button(root, text= "Afiseaza intrarile", command= query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


conn.commit()


conn.close()




root.mainloop()