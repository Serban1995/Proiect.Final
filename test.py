from tkinter import *
from tkinter import *
from tkinter import messagebox as mb
import json
import sqlite3

root = Tk()
root.title("test baza de date")
root.geometry("800x500")
with open('quiz.json') as f:  #deschidem fisierul jason dupa care transformam obiectele din el in fisiere la noi in program
    obj = json.load(f)
q = (obj['ques'])
options = (obj['options'])
a = (obj['ans'])


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

# class Quiz:
#     def __init__(self):
#         self.qn = 0
#         self.opt_selected = IntVar()
#         self.opts = self.radiobtns()
#         self.ques = self.question(self.qn)
#         self.display_options(self.qn)
#         self.buttons()
#         self.correct = 0
#
#
#
#
#     # funtie creata pentru a creea doua label-uri pentru titlu si intrebare
#     # funtie v-a returna label-ul  gn, care reprezinta numarul intrebarii mai apoi apelat in constructor
#
#     def question(self, qn):
#         t = Label(root, text="Quiz App", width=50, bg="blue", fg="white", font=("times", 20, "bold"))
#         t.place(x=0, y=2)
#         qn = Label(root, text=" ", width=60, font=("times", 16, "bold"), anchor="w")
#         qn.place(x=70, y=100)
#         # print(t)
#         # print(qn)
#         return qn
#
#     # creearea butoanelor de optiuni incepand cu o lista goala apoi folosind un while adaugand valori listei plus pozitia lor
#     def radiobtns(self):
#         val = 0
#         b = []
#         yp = 150
#         while val < 4:
#             btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
#             b.append(btn)
#             btn.place(x=100, y=yp)
#             val += 1
#             yp += 40
#         return b
#     # afisam variantele de rapuns
#     def display_options(self, qn):
#         val = 0 #creez o variabila initiala cu valoare 0
#         self.opt_selected.set(0) #setam 0 ca sa nu avem nici o varianta selectata by default
#         self.ques["text"] = q[qn]
#         for op in options[qn]: #folosind un loop afisez variantele de rapuns
#             self.opts[val]['text'] = op
#             val += 1
#         # print(op)
#         # print(val)
#         # print(self.ques["text"])
#         # print(q[qn])
#
#     def buttons(self):
#         nbutton = Button(root, text="Next",command=self.nextbtn, width=10, bg="green", fg="white",
#                          font=("times", 16, "bold"))
#         nbutton.place(x=200, y=380)
#         quitbutton = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
#                             font=("times", 16, "bold"))
#         quitbutton.place(x=380, y=380)
#         # verificam raspunsul dat de user iar daca acesta este corect returnam True
#
#     # verificam daca imputul dat de user este corect
#     def checkans(self, qn):
#         if self.opt_selected.get() == a[qn]:
#             return True
#     # oferim funtionalitate butonului de next sa ne afiseze urmatoarea intrebare
#     # adunam raspunsurile corecte ale user-ului
#     def nextbtn(self):
#         if self.checkans(self.qn):
#             self.correct += 1
#         self.qn += 1
#         if self.qn == len(q): #folosim un if ca atunci cand terminam numarul de intrebari sa ne afiseze raspunsulrile
#             self.display_rezult()
#         else:
#             self.display_options(self.qn)
#
#     def display_rezult(self):
#         scor = int(self.correct / len(q) * 100)
#         result = f"Scor: {scor} %"
#         wc = len(q) - self.correct
#         correct = "Raspunsuri corecte: " + str(self.correct)
#         wrong = "Raspunsuri gresite: " + str(wc)
#         mb.showinfo("Rezultat", "\n".join([result, correct, wrong]))
#
#
#
# # print(q)
# # print(options)
# # print(a)
# quiz = Quiz()




root.mainloop()