from tkinter import *
def aa(w, h, t):
    b = Tk()
    b.geometry(f"{w}x{h}")
    Label(b, text=t).place(x=0, y=0)
    c = Canvas(b, width=w, height=h)
    c.place(x=0, y=20)
    c.create_polygon(w//2, 20, w//2-30, 80, w//2+30, 80, fill="blue")
    b.mainloop()
aa(200, 180, "OK")
