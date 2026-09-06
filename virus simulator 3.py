import tkinter as tk
import subprocess
import tempfile
import os

def open_troll():
    window.destroy()

    # Create a temporary text file
    file = tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".txt",
        delete=False,
        encoding="utf-8"
    )

    file.write("you just got trolled!")
    file.close()

    # Open it in Notepad
    subprocess.Popen(["notepad.exe", file.name])


window = tk.Tk()
window.title("Virus Simulator 2!")
window.geometry("500x300")

warning = tk.Label(
    window,
    text="⚠️ WARNING!\n\n"
         "Are you sure you want to open this virus?\n\n"
         "This is a harmless virus simulator.\n"
         "It cannot cause data loss or install programs.",
    font=("Arial", 12)
)
warning.pack(pady=35)

button_frame = tk.Frame(window)
button_frame.pack()

yes_button = tk.Button(
    button_frame,
    text="YES",
    width=10,
    command=open_troll
)
yes_button.pack(side="left", padx=10)

cancel_button = tk.Button(
    button_frame,
    text="CANCEL",
    width=10,
    command=window.destroy
)
cancel_button.pack(side="left", padx=10)

window.mainloop()