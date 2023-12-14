import tkinter as tk
from carsdb_controller import session, select_all

FONTS = ["Tenor Sans", "Consolas"]


def fill_bxbox(data):
    bx_boxas.delete(0, tk.END)
    bx_boxas.insert(0, *data)

win = tk.Tk()
win.geometry("1000x500")
win.option_add("*Font", (FONTS[1], 20))

fr_controls = tk.Frame(win)
sc_scrollas = tk.Scrollbar(win)
bx_boxas = tk.Listbox(win, yscrollcommand=sc_scrollas.set)
sc_scrollas.config(command=bx_boxas.yview)

l_search = tk.Label(fr_controls, text="cars")
l_car_make = tk.Label(fr_controls, text="make")
e_car_make = tk.Entry(fr_controls)
l_car_model = tk.Label(fr_controls, text="model")
e_car_model = tk.Entry(fr_controls)
l_car_price = tk.Label(fr_controls, text="price") ####
e_car_price = tk.Entry(fr_controls)
l_year = tk.Label(fr_controls, text="year")
e_year = tk.Entry(fr_controls)

# bx_boxas.insert(tk.END, *select_all(c))
fill_bxbox(select_all(session))

l_search.grid(row=0, column=0, sticky=tk.W)
l_car_make.grid(row=1, column=0, sticky=tk.W)
e_car_make.grid(row=1, column=1, columnspan=2)
l_car_model.grid(row=2, column=0, sticky=tk.W)
e_car_model.grid(row=2, column=1, columnspan=2)
l_car_price.grid(row=3, column=0, sticky=tk.W)
e_car_price.grid(row=3, column=1, columnspan=2)
l_year.grid(row=4, column=0, sticky=tk.W)
e_year.grid(row=4, column=1, columnspan=2)




fr_controls.pack(side=tk.LEFT, anchor=tk.N)
sc_scrollas.pack(side=tk.RIGHT, fill=tk.Y)
bx_boxas.pack(fill=tk.BOTH, expand=True, padx=4)

win.eval("tk::PlaceWindow . center")
win.mainloop()

# ford' OR 1=1--
