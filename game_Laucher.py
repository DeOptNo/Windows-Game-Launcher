import os
import subprocess
import webbrowser
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import win32com.client
import winsound  # Built-in sound module for Windows
import threading

# === CONFIG ===   # All of theses should be something like C:Users\user\Launcher\games ETC. Check example image for more details
GAMES_FOLDER = r""
ICONS_FOLDER = r""
FALLBACK_ICON_PATH = r"" # Fallback image
HOVER_SOUND_PATH = r""
LAUNCH_SOUND_PATH = r""

# === UI SETUP ===
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class GameLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🎮 windows Game Launcher")
        self.geometry("900x750")
        self.resizable(False, False)

        os.makedirs(GAMES_FOLDER, exist_ok=True)
        os.makedirs(ICONS_FOLDER, exist_ok=True)

        self.games = self.load_games()
        self.build_ui()

    def load_games(self):
        valid_exts = (".exe", ".lnk", ".url")
        return [f for f in os.listdir(GAMES_FOLDER) if f.endswith(valid_exts)]

    def build_ui(self):
        ctk.CTkLabel(self, text="🕹️ Windows Game Launcher", font=ctk.CTkFont(size=26, weight="bold")).pack(pady=20)

        self.scroll_frame = ctk.CTkScrollableFrame(self, width=860, height=660)
        self.scroll_frame.pack(padx=20, pady=10)

        self.create_game_grid()

    def create_game_grid(self):
        max_columns = 3
        icon_size = (96, 96)

        for index, game_file in enumerate(self.games):
            row = index // max_columns
            col = index % max_columns
            game_name = os.path.splitext(game_file)[0]
            icon_path = os.path.join(ICONS_FOLDER, f"{game_name}.png")
            icon = self.load_icon(icon_path, icon_size)

            card = ctk.CTkFrame(self.scroll_frame, corner_radius=10, fg_color="#1f1f24", width=250)
            card.grid(row=row, column=col, padx=10, pady=20, sticky="nsew")
            card = ctk.CTkFrame(self.scroll_frame, corner_radius=10, fg_color="#1f1f24", width=250)
            card.grid(row=row, column=col, padx=10, pady=20, sticky="nsew")

# Bind hover animation (highlight on hover)
            def on_hover_enter(event, widget=card):
                widget.configure(fg_color="#333344")  # Dark highlight color

            def on_hover_leave(event, widget=card):
                widget.configure(fg_color="#1f1f24")  # Back to default

            card.bind("<Enter>", on_hover_enter)
            card.bind("<Leave>", on_hover_leave)
            
            image_label = ctk.CTkLabel(card, image=icon, text="")
            image_label.pack(pady=(10, 5))

            name_label = ctk.CTkLabel(card, text=game_name, font=ctk.CTkFont(size=14))
            name_label.pack(pady=(0, 10))

            for widget in [card, image_label, name_label]:
                widget.bind("<Enter>", lambda e: self.play_hover_sound())
                widget.bind("<Button-1>", lambda e, f=game_file: self.launch_game(f))

        for col in range(max_columns):
            self.scroll_frame.grid_columnconfigure(col, weight=1)

    def load_icon(self, icon_path, size):
        try:
            if os.path.exists(icon_path):
                img = Image.open(icon_path).resize(size, Image.LANCZOS)
            else:
                img = Image.open(FALLBACK_ICON_PATH).resize(size, Image.LANCZOS)
            return ctk.CTkImage(light_image=img, size=size)
        except Exception as e:
            print(f"Error loading icon: {e}")
            return None

    def play_hover_sound(self):
        threading.Thread(target=self._play_sound, args=(HOVER_SOUND_PATH,)).start()

    def play_launch_sound(self):
        threading.Thread(target=self._play_sound, args=(LAUNCH_SOUND_PATH,)).start()

    def _play_sound(self, sound_path):
        try:
            winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
        except Exception as e:
            print(f"Sound error: {e}")

    def launch_game(self, game_file):
        path = os.path.join(GAMES_FOLDER, game_file)
        ext = os.path.splitext(game_file)[1].lower()

        try:
            self.play_launch_sound()

            if ext == ".lnk":
                shell = win32com.client.Dispatch("WScript.Shell")
                shortcut = shell.CreateShortcut(path)
                target = shortcut.TargetPath
                if os.path.exists(target):
                    subprocess.Popen([target], shell=True)
                else:
                    raise FileNotFoundError("Shortcut target not found.")

            elif ext == ".exe":
                subprocess.Popen([path], shell=True)

            elif ext == ".url":
                with open(path, "r") as file:
                    for line in file:
                        if line.startswith("URL="):
                            url = line.strip().split("=", 1)[-1]
                            webbrowser.open(url)
                            break
                    else:
                        raise ValueError("No URL found in shortcut.")

            else:
                messagebox.showwarning("Unsupported", f"Cannot open file type: {game_file}")

            self.after(300, self.destroy)  # Close launcher after delay

        except Exception as e:
            messagebox.showerror("Error", f"Could not launch {game_file}\n\n{e}")


if __name__ == "__main__":
    app = GameLauncher()
    app.mainloop()
