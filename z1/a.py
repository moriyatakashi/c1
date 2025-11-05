import tkinter as tk
import b  # b.py をインポート

# ウィンドウの作成
root = tk.Tk()
root.title("Tkinterサンプル")
root.geometry("300x200")

# ラベルの作成
label = tk.Label(root, text="こんにちは！", font=("Arial", 14))
label.pack(pady=10)

# ボタンの作成（3つ）
button1 = tk.Button(root, text="ボタン1", command=lambda: b.on_button1_click(label))
button1.pack(pady=5)

button2 = tk.Button(root, text="ボタン2", command=lambda: b.on_button2_click(label))
button2.pack(pady=5)

button3 = tk.Button(root, text="ボタン3", command=lambda: b.on_button3_click(label))
button3.pack(pady=5)

# メインループの開始
root.mainloop()