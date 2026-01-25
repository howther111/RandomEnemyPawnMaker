import os
import tkinter as tk
from tkinter import messagebox

def replace_enemy_name():
    old = old_entry.get()
    new = new_entry.get()

    if not old or not new:
        messagebox.showwarning("警告", "両方の文字列を入力してください。")
        return

    base_dir = os.path.dirname(os.path.abspath(__file__))
    replaced_files = 0

    for filename in os.listdir(base_dir):
        if not filename.endswith(".txt"):
            continue

        old_path = os.path.join(base_dir, filename)

        # --- ファイル内容の置換 ---
        try:
            with open(old_path, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = content.replace(old, new)

            if content != new_content:
                with open(old_path, "w", encoding="utf-8") as f:
                    f.write(new_content)

        except Exception as e:
            messagebox.showerror("エラー", f"{filename} の処理中にエラーが発生しました。\n{e}")
            return

        # --- ファイル名の置換 ---
        if old in filename:
            new_filename = filename.replace(old, new)
            new_path = os.path.join(base_dir, new_filename)
            os.rename(old_path, new_path)

        replaced_files += 1

    messagebox.showinfo("完了", f"{replaced_files} 個のファイルを処理しました。")

# --- GUI構築 ---
root = tk.Tk()
root.title("エネミー名一括変更ツール")
root.geometry("400x200")

tk.Label(root, text="変更する対象の文字列を入力してください：").pack(pady=5)
old_entry = tk.Entry(root, width=40)
old_entry.pack()

tk.Label(root, text="変更後の文字列を入力してください：").pack(pady=5)
new_entry = tk.Entry(root, width=40)
new_entry.pack()

tk.Button(root, text="置換実行", command=replace_enemy_name).pack(pady=15)

root.mainloop()
