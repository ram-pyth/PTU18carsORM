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

l_search = tk.Label(fr_controls, text="automobilis")

# bx_boxas.insert(tk.END, *select_all(c))
fill_bxbox(select_all(session))

l_search.grid(row=0, column=0, sticky=tk.W)

fr_controls.pack(side=tk.LEFT, anchor=tk.N)
sc_scrollas.pack(side=tk.RIGHT, fill=tk.Y)
bx_boxas.pack(fill=tk.BOTH, expand=True)

win.eval("tk::PlaceWindow . center")
win.mainloop()

# ford' OR 1=1--
