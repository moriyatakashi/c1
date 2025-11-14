import tkinter as tk
root = tk.Tk()
root.geometry("640x480")
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="quit", command=root.quit)
menubar.add_cascade(label="file", menu=file_menu)
root.config(menu=menubar)
root.mainloop()