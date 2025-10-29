def aa(pa, pb, pc):
    import tkinter as a
    b = a.Tk()
    b.geometry(str(pa) + "x" + str(pb))
    a.Label(b, text=pc).place(x=0, y=0)
    c = a.Canvas(b, width=pa, height=pb)
    c.place(x=0, y=20)
    x1, y1 = pa // 2, 20
    x2, y2 = x1 - 30, y1 + 60
    x3, y3 = x1 + 30, y1 + 60
    c.create_polygon(x1, y1, x2, y2, x3, y3, fill="blue")
    b.mainloop()
aa(200, 200, "OK")