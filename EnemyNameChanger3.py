import os
import sys
import tkinter as tk
from tkinter import messagebox


def get_base_dir():
    """
    PyInstaller(onefile/onedir)どちらでも
    “exeが置かれている場所” を基準ディレクトリとして返す。
    """
    if getattr(sys, "frozen", False):
        # exe実行時
        return os.path.dirname(sys.executable)
    # 通常の .py 実行時
    return os.path.dirname(os.path.abspath(__file__))


def replace_enemy_name():
    old = old_entry.get()
    new = new_entry.get()

    if not old or not new:
        messagebox.showwarning("警告", "両方の文字列を入力してください。")
        return

    if old == new:
        messagebox.showinfo("情報", "変更前と変更後が同じです。処理は行いません。")
        return

    base_dir = get_base_dir()

    total_txt_files = 0
    replaced_files = 0
    error_files = []

    for filename in os.listdir(base_dir):
        if not filename.lower().endswith(".txt"):
            continue

        total_txt_files += 1
        old_path = os.path.join(base_dir, filename)

        try:
            content_replaced = False

            # --- まず内容を置換（ファイル名変更があっても安全にするため、パスは変数で追跡） ---
            with open(old_path, "r", encoding="utf-8") as f:
                content = f.read()

            if old in content:
                content = content.replace(old, new)
                with open(old_path, "w", encoding="utf-8") as f:
                    f.write(content)
                content_replaced = True

            # --- 次にファイル名の置換（衝突チェック） ---
            current_path = old_path
            current_filename = filename

            if old in current_filename:
                new_filename = current_filename.replace(old, new)
                new_path = os.path.join(base_dir, new_filename)

                # 同名衝突を避ける（既存ファイルがあるならエラー扱い）
                if os.path.exists(new_path):
                    raise FileExistsError(f"リネーム先が既に存在します: {new_filename}")

                os.rename(current_path, new_path)
                current_path = new_path
                content_replaced = True

            if content_replaced:
                replaced_files += 1

        except Exception as e:
            # 1ファイルで失敗しても全体は続行し、最後にまとめて表示
            error_files.append(f"{filename}: {e}")

    # --- 結果表示 ---
    msg = (
        f"対象フォルダ：{base_dir}\n\n"
        f"検出した .txt ファイル数：{total_txt_files}\n"
        f"置換が行われたファイル数：{replaced_files}\n"
        f"エラー件数：{len(error_files)}"
    )

    if error_files:
        # エラー詳細は長くなるので必要なら分割して表示（簡易）
        detail = "\n".join(error_files[:30])
        if len(error_files) > 30:
            detail += f"\n...（他 {len(error_files) - 30} 件）"
        messagebox.showwarning("完了（エラーあり）", msg + "\n\n--- エラー詳細 ---\n" + detail)
    else:
        messagebox.showinfo("完了", msg)


# --- GUI構築 ---
root = tk.Tk()
root.title("エネミー名一括変更ツール")
root.geometry("460x240")

tk.Label(root, text="変更する対象の文字列を入力してください：").pack(pady=5)
old_entry = tk.Entry(root, width=55)
old_entry.pack()

tk.Label(root, text="変更後の文字列を入力してください：").pack(pady=5)
new_entry = tk.Entry(root, width=55)
new_entry.pack()

tk.Button(root, text="置換実行", command=replace_enemy_name).pack(pady=18)

root.mainloop()
