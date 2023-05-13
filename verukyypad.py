import tkinter as tk
from tkinter import messagebox, filedialog
import os
import shutil






def toggle_fullscreen(event=None):
    state = not root.attributes('-fullscreen')
    root.attributes('-fullscreen', state)


# Sprawdzenie i utworzenie folderu "verukyypad" na pulpicie, jeśli nie istnieje
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
verukyypad_folder = os.path.join(desktop_path, 'verukyypad')
if not os.path.exists(verukyypad_folder):
    os.mkdir(verukyypad_folder)

current_file = None  # Ścieżka do aktualnie otwartego pliku


def save_file():
    global current_file
    if current_file:
        try:
            with open(current_file, 'w') as file:
                file.write(text_widget.get('1.0', tk.END))
            messagebox.showinfo('Informacja', 'Plik został zapisany.')
        except Exception as e:
            messagebox.showerror('Błąd', f'Wystąpił błąd podczas zapisywania pliku:\n{str(e)}')
    else:
        save_file_as()


def save_file_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension='.verukyypad',
                                             filetypes=[('Pliki Verukyypad', '*.verukyypad')])

    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(text_widget.get('1.0', tk.END))
            current_file = file_path
            messagebox.showinfo('Informacja', 'Plik został zapisany.')
        except Exception as e:
            messagebox.showerror('Błąd', f'Wystąpił błąd podczas zapisywania pliku:\n{str(e)}')


def open_file():
    global current_file
    file_path = filedialog.askopenfilename(filetypes=[('Pliki Verukyypad', '*.verukyypad')])

    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            text_widget.delete('1.0', tk.END)
            text_widget.insert(tk.END, content)
            current_file = file_path
        except FileNotFoundError:
            messagebox.showerror('Błąd', 'Plik nie został znaleziony.')
        except Exception as e:
            messagebox.showerror('Błąd', f'Wystąpił błąd podczas otwierania pliku:\n{str(e)}')


root = tk.Tk()
root.title('Verukyypad -Info = (Aby uruchomić program w pełnym ekranie, kliknij F11)')
root.geometry('700x500')

# Motyw ciemny
root.config(bg='black')

# Pole tekstowe
text_widget = tk.Text(root, wrap=tk.WORD, bg='black', fg='white')
text_widget.pack(fill=tk.BOTH, expand=True)

text_widget.configure(insertbackground='red')

# Menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Nowy', command=lambda: text_widget.delete('1.0', tk.END))
file_menu.add_command(label='Otwórz', command=open_file)
file_menu.add_command(label='Zapisz', command=save_file)
file_menu.add_command(label='Zapisz jako', command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label='Zamknij', command=root.quit)
menu_bar.add_cascade(label='Plik', menu=file_menu)

root.config(menu=menu_bar)

def on_closing():
    if current_file:
        save_file()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.bind('<F11>', toggle_fullscreen)

def on_close():
    if current_file:
        save_file()
    else:
        response = messagebox.askyesno('Zamknąć program?', 'Najpierw zapisz plik przed zamknięciem.\nCzy na pewno chcesz zamknąć program?')
        if response:
            save_file()
            root.destroy()

# ...

root.protocol("WM_DELETE_WINDOW", on_close)


poland_label = tk.Label(root, text="©Pikusw.pl - Programował=Sebastian Wanat", font=("Arial", 10), bg="#006600", fg="red")
poland_label.pack(side=tk.BOTTOM, pady=10)




root.mainloop()