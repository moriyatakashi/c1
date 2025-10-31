from tkinter import *
b = Tk()
b.geometry("200x180")
Label(b, text="OK").place(x=0, y=0)
c = Canvas(b, width=200, height=180)
c.place(x=0, y=20)
c.create_polygon(100, 20, 70, 80, 130, 80, fill="blue")
b.mainloop()
