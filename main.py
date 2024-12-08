import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Formularz rejestracyjny zgłoszenia na festiwal")
# Etykiety i pola tekstowe
label_title = tk.Label(root, text="Imię")
label_title.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_title = tk.Entry(root, width=40)
entry_title.grid(row=0, column=1, padx=10, pady=5)
label_author = tk.Label(root, text="Nazwisko")
label_author.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_author = tk.Entry(root, width=40)
entry_author.grid(row=1, column=1, padx=10, pady=5)
label_genre = tk.Label(root, text="Adres-email")
label_genre.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_genre = tk.Entry(root, width=40)
entry_genre.grid(row=2, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Numer telefonu")
label_year.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=3, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Miasto")
label_year.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=3, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Kraj")
label_year.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=3, column=1, padx=10, pady=5)
label_year = tk.Label(root, text="Data")
label_year.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_year = tk.Entry(root, width=40)
entry_year.grid(row=3, column=1, padx=10, pady=5)
label_ID = tk.Label(root, text="PESEL")
label_ID.grid(row=4, column=0, padx=10, pady=5, sticky="w")
label_ID = tk.Entry(root, width=40)
label_ID.grid(row=4, column=1, padx=10, pady=5)
label_DG = tk.Label(root, text="Wykształcenie")
label_DG.grid(row=5, column=0, padx=10, pady=5, sticky="w")
label_DG = tk.Entry(root, width=40)
label_DG.grid(row=5, column=1, padx=10, pady=5)
label_EX = tk.Label(root, text="Doświadczenie wolontariackie")
label_EX.grid(row=6, column=0, padx=10, pady=5, sticky="w")
label_EX = tk.Entry(root, width=40)
label_EX.grid(row=6, column=1, padx=10, pady=5)
# Przycisk zapisu
button_save = tk.Button(root, text="Zapisz", command=lambda x:x)
button_save.grid(row=4, column=0, columnspan=2, pady=10)
# Uruchomienie pętli głównej
root.mainloop()