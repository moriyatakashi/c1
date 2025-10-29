def aa(pa,pb,pc):
    import tkinter as a
    b=a.Tk()
    b.geometry(str(pa)+"x"+str(pb))
    a.Label(b,text=pc).place(x=0,y=0)
    b.mainloop()
aa(99,99,"OK")