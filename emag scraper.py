import tkinter as tk
from tkinter.constants import SUNKEN
def handle_click(event):
    scrape()
    window.destroy()

def scrape():
    import requests
    import xlsxwriter
    from bs4 import BeautifulSoup
    from xlsxwriter import worksheet

    search_term = search_text.get()
    file_name = file_text.get()
    page_number = page_text.get()
    a = ""
    a += file_name
    a += ".xlsx"
    workbook = xlsxwriter.Workbook(a)
    worksheet = workbook.add_worksheet()
    worksheet.set_column_pixels('A:A', 120)
    worksheet.set_column_pixels('B:B', 1300)
    nume_string = [" "]
    pret_string = [" "]
    search_term = search_term.replace(" ", "+")
    URL = "https://www.emag.ro/search/"
    URL += search_term
    URL += "/p"
    URL += page_number
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id = "card_grid")
    job_elements = results.find_all("div", class_ = "pad-hrz-xs" )
    job_elements2 = results.find_all("div", class_ = "card-v2-pricing")
    for job_element in job_elements:
        nume = job_element.find("a", class_ = "card-v2-title semibold mrg-btm-xxs js-product-url")
        nume_string.append(nume.text)
    for job_element2 in job_elements2:
        pret = job_element2.find("p", class_ = "product-new-price")
        pret_string.append (pret.text)
    row = 0
    worksheet.write(row, 0, 'Pret')
    worksheet.write(row, 1, 'Nume')
    row = 0
    for x in nume_string:
        worksheet.write(row + 1, 1, x)
        row += 1
    row = 0
    for x in pret_string:
        pret_moneda = x[-6:]
        pret_intreg = x[:-6]
        pret_total = pret_intreg + "," + pret_moneda
        if len(pret_total) != 2:
            worksheet.write(row + 1, 0, pret_total)
        row += 1

    workbook.close()

window = tk.Tk()
frame = tk.Frame(
    master = window,
    width = 1250,
    height = 450
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
    text = "In lista vor aparea 60 de produse.",
    master = frame,
    font = ("Times New Roman", 44)
)
number_of_items.place(x = 20, y = 340)
button.bind("<Button-1>", handle_click)
button.pack()
window.mainloop()