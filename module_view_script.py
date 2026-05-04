from tkinter import ttk
import tkinter as tk
import module_hasher
import module_database
def Entry(frame: ttk.Frame, name: str, row: int, column: int, pady: int, width:int = 20) -> ttk.Entry:
    entry = ttk.Entry(frame, width=width)
    entry.insert(0, name)
    
    entry.config(foreground="grey") 

    def on_focus_in(event):
        if entry.get() == name:
            entry.delete(0, tk.END)
            entry.config(foreground="white") 
            
    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, name)
            entry.config(foreground="grey") 
            
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
    entry.grid(row=row, column=column, pady=pady, sticky="ew") 
    return entry

def add_information(site: str, title: str, login: str, password: str, table_treeview):
    if ([site, title, login, password] != ["Site", "Title", "Name", "Password"]):
        module_database.add_info(site, title, login, password)
        
        table_treeview.insert("", "end", values = (module_database.get_end_info()[0], site, title, login, password))
def toggle(mode_switch, password_entry):
    if mode_switch.instate(['selected']):
        password_entry['show'] = "*"
    else:
        password_entry['show'] = ""

def open_table(table_treeview):
    table = module_database.get_all_info()
    for x in table:
        table_treeview.insert("", "end", values=(x[0], x[1], x[2], x[3], module_hasher.decode(x[4], 256)))