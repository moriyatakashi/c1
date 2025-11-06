import tkinter as tk
import platform
import b
if platform.system() == "Windows":
    default_font = ("Meiryo", 12)
elif platform.system() == "Linux":
    default_font = ("Noto Sans", 12)
else:
    default_font = ("Helvetica", 12)
root = tk.Tk()
root.title("v0.1")
root.geometry("400x200")
label = tk.Label(root, text="選んでください", font=default_font)
label.pack(pady=10)
button1 = tk.Button(root, text="case1", command=lambda: b.on_button1_click(label), font=default_font)
button1.pack(pady=5)
button2 = tk.Button(root, text="case2", command=lambda: b.on_button2_click(label), font=default_font)
button2.pack(pady=5)
button3 = tk.Button(root, text="case3", command=lambda: b.on_button3_click(label), font=default_font)
button3.pack(pady=5)
root.mainloop()
