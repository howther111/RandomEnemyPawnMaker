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

    total_txt_files = 0
    replaced_files = 0

    for filename in os.listdir(base_dir):
        if not filename.lower().endswith(".txt"):
            continue

        total_txt_files += 1
        old_path = os.path.join(base_dir, filename)

        try:
            # --- ファイル内容読み込み ---
            with open(old_path, "r", encoding="utf-8") as f:
                content = f.read()

            content_replaced = False

            # --- ファイル内容の置換 ---
            if old in content:
                content = content.replace(old, new)
                content_replaced = True

                with open(old_path, "w", encoding="utf-8") as f:
                    f.write(content)

            # --- ファイル名の置換 ---
            if old in filename:
                new_filename = filename.replace(old, new)
                new_path = os.path.join(base_dir, new_filename)
                os.rename(old_path, new_path)
                content_replaced = True

            if content_replaced:
                replaced_files += 1

        except Exception as e:
            messagebox.showerror(
                "エラー",
                f"{filename} の処理中にエラーが発生しました。\n{e}"
            )
            return

    messagebox.showinfo(
        "完了",
        f"検出した .txt ファイル数：{total_txt_files}\n"
        f"置換が行われたファイル数：{replaced_files}"
    )

# --- GUI構築 ---
root = tk.Tk()
root.title("エネミー名一括変更ツール")
root.geometry("420x220")

tk.Label(root, text="変更する対象の文字列を入力してください：").pack(pady=5)
old_entry = tk.Entry(root, width=45)
old_entry.pack()

tk.Label(root, text="変更後の文字列を入力してください：").pack(pady=5)
new_entry = tk.Entry(root, width=45)
new_entry.pack()

tk.Button(root, text="置換実行", command=replace_enemy_name).pack(pady=15)

root.mainloop()
