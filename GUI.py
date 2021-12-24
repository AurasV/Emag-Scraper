import tkinter as tk
from tkinter.constants import SUNKEN
def handle_click(event):
    print("The button has been pressed!")
    search_term = search_text.get()
    print(search_term)
    file_name = file_text.get()
    print(file_name)
    page_number = page_text.get()
    print(page_number)
    items_number = number_of_items_text.get()
    print(items_number)
    window.destroy()


window = tk.Tk()
frame = tk.Frame(
    master = window,
    width = 1250,
    height = 500
)
frame.pack()
frame_sunken = tk.Frame(master = window, relief = SUNKEN, borderwidth=10)
frame_sunken.pack()
search = tk.Label(
    text = "Ce vrei sa cauti?",
    master = frame,
    font = ("Times New Roman", 44)
)
search.place(x = 20, y = 10)
search_text = tk.Entry(
    width = 40,
    master = frame,
    font = ("Times New Roman", 20)
)
search_text.place(x = 20, y = 80)
file = tk.Label(
    text = "Cum vrei sa se numeasca fisierul?",
    master = frame,
    font = ("Times New Roman", 44)
)
file.place(x = 20, y = 120)
file_text = tk.Entry(
    width = 40,
    master = frame,
    font = ("Times New Roman", 20)
)
file_text.place(x = 20, y = 190)
button = tk.Button(
    text = "Gata",
    width = 25,
    height = 5,
    bg = "#1B085F",
    fg = "#03A3FF",
    master = frame_sunken
)
page = tk.Label(
    text = "A cata pagina vrei sa cauti?(Ex 1, 2, 5)",
    master = frame,
    font = ("Times New Roman", 44)
)
page.place(x = 20, y = 230)
page_text = tk.Entry(
    width = 40,
    master = frame,
    font = ("Times New Roman", 20)
)
page_text.place(x = 20, y = 300)
number_of_items = tk.Label(
    text = "Cate produse vrei sa apara in lista?(Ex 20, max 60)",
    master = frame,
    font = ("Times New Roman", 44)
)
number_of_items.place(x = 20, y = 340)
number_of_items_text = tk.Entry(
    width = 40,
    master = frame,
    font = ("Times New Roman", 20)
)
number_of_items_text.place(x = 20, y = 410)
button.bind("<Button-1>", handle_click)
button.pack()
window.mainloop()


