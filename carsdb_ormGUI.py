import tkinter as tk
from carsdb_controller import session, select_all, create_record, delete_record, edit_record
from tkinter import messagebox

FONTS = ["Tenor Sans", "Consolas"]
all_data = []
obj = None


def fill_bxbox(data):
    bx_boxas.delete(0, tk.END)
    bx_boxas.insert(0, *data)


def refresh_bxbox():
    global all_data
    all_data = select_all(session)
    fill_bxbox(all_data)


def on_delete():
    selection = bx_boxas.curselection()
    if not selection:
        messagebox.showerror("Nothing selected", "Please select row to delete")
        return
    index = selection[0]
    delete_record(session, all_data[index])
    refresh_bxbox()


def on_edit():
    global obj
    selection = bx_boxas.curselection()
    if not selection:
        messagebox.showerror("Nothing selected", "Please select row to edit")
        return
    index = selection[0]
    clear_entry_fields()
    obj = all_data[index]
    e_car_make.insert(tk.END, obj.car_make)
    e_car_model.insert(tk.END, obj.car_model)
    e_car_price.insert(tk.END, obj.car_price)
    e_year.insert(tk.END, obj.year)
    b_delete["state"] = "disabled"


def on_escape_edit():
    global obj
    obj = None
    clear_entry_fields()
    b_delete["state"] = "normal"


def clear_entry_fields():
    e_car_make.delete(0, tk.END)
    e_car_model.delete(0, tk.END)
    e_car_price.delete(0, tk.END)
    e_year.delete(0, tk.END)


def save_record():
    global obj
    car_make = e_car_make.get().strip()
    car_model = e_car_model.get().strip()
    if len(car_make) < 2 or len(car_model) < 1:
        messagebox.showerror("Make or model error", "Make or model were not entered")
        return
    if obj:
        edit_record(session,
                    obj,
                    make=car_make,
                    model=car_model,
                    price=e_car_price.get(),
                    year=e_year.get())
        obj = None
        b_delete["state"] = "normal"
    else:
        create_record(ses=session,
                      make=car_make,
                      model=car_model,
                      price=e_car_price.get(),
                      year=e_year.get())
    refresh_bxbox()
    clear_entry_fields()


win = tk.Tk()
win.geometry("1000x500")
win.option_add("*Font", (FONTS[1], 20))

fr_controls = tk.Frame(win)
sc_scrollas = tk.Scrollbar(win)
bx_boxas = tk.Listbox(win, yscrollcommand=sc_scrollas.set)
sc_scrollas.config(command=bx_boxas.yview)
bx_boxas.bind("<<ListboxSelect>>")
win.bind("<Escape>", lambda e: on_escape_edit())

l_search = tk.Label(fr_controls, text="cars")
l_car_make = tk.Label(fr_controls, text="make")
e_car_make = tk.Entry(fr_controls)
l_car_model = tk.Label(fr_controls, text="model")
e_car_model = tk.Entry(fr_controls)
l_car_price = tk.Label(fr_controls, text="price")  ####
e_car_price = tk.Entry(fr_controls)
l_year = tk.Label(fr_controls, text="year")
e_year = tk.Entry(fr_controls)
b_save = tk.Button(fr_controls, text="SAVE", command=save_record, width=10)
b_edit = tk.Button(fr_controls, text="EDIT", command=on_edit)
b_delete = tk.Button(fr_controls, text="DELETE", command=on_delete)

# bx_boxas.insert(tk.END, *select_all(c))
refresh_bxbox()

l_search.grid(row=0, column=0, sticky=tk.W)
l_car_make.grid(row=1, column=0, sticky=tk.W)
e_car_make.grid(row=1, column=1, columnspan=2)
l_car_model.grid(row=2, column=0, sticky=tk.W)
e_car_model.grid(row=2, column=1, columnspan=2)
l_car_price.grid(row=3, column=0, sticky=tk.W)
e_car_price.grid(row=3, column=1, columnspan=2)
l_year.grid(row=4, column=0, sticky=tk.W)
e_year.grid(row=4, column=1, columnspan=2)
b_save.grid(row=5, column=0, sticky=tk.W)
b_edit.grid(row=5, column=1, sticky=tk.W + tk.E)
b_delete.grid(row=5, column=2, sticky=tk.W + tk.E)

fr_controls.pack(side=tk.LEFT, anchor=tk.N)
sc_scrollas.pack(side=tk.RIGHT, fill=tk.Y)
bx_boxas.pack(fill=tk.BOTH, expand=True, padx=4)

win.eval("tk::PlaceWindow . center")
win.mainloop()

# ford' OR 1=1--
