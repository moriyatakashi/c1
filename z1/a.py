import tkinter as tk

def on_button_click():
    label.config(text="ボタンがクリックされました！")

# ウィンドウの作成
root = tk.Tk()
root.title("Tkinterサンプル")
root.geometry("300x150")

# ラベルの作成
label = tk.Label(root, text="こんにちは！", font=("Arial", 14))
label.pack(pady=10)

# ボタンの作成
button = tk.Button(root, text="クリックしてね", command=on_button_click)
button.pack(pady=10)

# メインループの開始
root.mainloop()