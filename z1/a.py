import tkinter as tk
import platform
import b  # b.py をインポート

# OSに応じたフォント設定
if platform.system() == "Windows":
    default_font = ("Meiryo", 12)  # Windowsでは読みやすいメイリオ
elif platform.system() == "Linux":
    default_font = ("Noto Sans", 12)  # UbuntuではNoto系が安定
else:
    default_font = ("Helvetica", 12)  # その他の環境用

# ウィンドウの作成
root = tk.Tk()
root.title("Tkinterサンプル")
root.geometry("300x200")

# ラベルの作成
label = tk.Label(root, text="こんにちは！", font=default_font)
label.pack(pady=10)

# ボタンの作成（3つ）
button1 = tk.Button(root, text="ボタン1", command=lambda: b.on_button1_click(label), font=default_font)
button1.pack(pady=5)

button2 = tk.Button(root, text="ボタン2", command=lambda: b.on_button2_click(label), font=default_font)
button2.pack(pady=5)

button3 = tk.Button(root, text="ボタン3", command=lambda: b.on_button3_click(label), font=default_font)
button3.pack(pady=5)

# メインループの開始
root.mainloop()
