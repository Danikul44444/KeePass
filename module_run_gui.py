import module_database
import tkinter as tk
from tkinter import ttk
from module_view_script import *

module_database.create_table()

root = tk.Tk()
root.title("KeePass")
root.geometry("950x500")

style = ttk.Style(root)

try:
    root.tk.call("source", "theme/forest-dark.tcl")
    style.theme_use("forest-dark")
except tk.TclError:
    print("Тема не найдена, используется стандартная.")


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame_window = tk.Frame(root)
frame_window.grid(row=0, column=0, sticky="nsew")
frame_window.grid_columnconfigure(1, weight=1) 
frame_window.grid_rowconfigure(1, weight=1)    



left_panel = ttk.Frame(frame_window)
left_panel.grid(row=0, column=0, rowspan=2, sticky="ns", padx=5, pady=5)

left_panel.grid_columnconfigure(0, weight=1)


# --- search
frame_search = ttk.LabelFrame(left_panel, text="Search")
frame_search.grid(row=0, column=0, sticky="ew", pady=(0, 10))
frame_search.grid_columnconfigure(0, weight=1)

search_entry = Entry(frame=frame_search, name="search", row=0, column=0, pady=5, width=15)

btn_search = ttk.Button(frame_search, text="Search", width=6) 
btn_search.grid(row=0, column=1, pady=5, padx=(0, 5))

frame_info = ttk.LabelFrame(left_panel, text="Add Information")
frame_info.grid(row=1, column=0, sticky="ew", pady=10)
frame_info.grid_columnconfigure(0, weight=1)

width_entry = 25
pady_entry = 5

title_entry =Entry(frame_info, "Title", 1, 0, pady=pady_entry, width=width_entry) 
name_entry = Entry(frame_info, "Name", 2, 0, pady=pady_entry, width=width_entry)

password_entry = Entry(frame_info, "Password", 3, 0, pady=pady_entry, width=width_entry)
check_frame = ttk.Frame(frame_info)
check_frame.grid(row=4, column=0, sticky="w", pady=5)

mode_switch = ttk.Checkbutton(check_frame, text="Show Password", style="Switch", command=toggle)
mode_switch.grid(row=0, column=0)

site_entry = Entry(frame_info, "Site", 5, 0, width=width_entry, pady=pady_entry)


add_info = ttk.Button(frame_info, text="ADD INFO", command=lambda: add_information(site_entry.get(), title_entry.get(), name_entry.get(), password_entry.get(), table_treeview))
add_info.grid(row=6, column=0, pady=(10, 5), sticky="ew") 
frame_info.grid(row=1, column=0, sticky="ew", pady=10)

# -- Table
right_panel = ttk.Frame(frame_window)
right_panel.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=(5, 5), pady=5)
right_panel.grid_rowconfigure(0, weight=1)
right_panel.grid_columnconfigure(0, weight=1)

columns = ("ID", "SITE", "TITLE", "LOGIN", "PASSWORD")
table_treeview = ttk.Treeview(right_panel, columns=columns, show="headings")


table_treeview.heading("ID", text="ID")
table_treeview.column("ID", width=40, anchor="center")

table_treeview.heading("SITE", text="SITE")
table_treeview.column("SITE", width=120)

table_treeview.heading("TITLE", text="TITLE")
table_treeview.column("TITLE", width=150)

table_treeview.heading("LOGIN", text="LOGIN")
table_treeview.column("LOGIN", width=150)

table_treeview.heading("PASSWORD", text="PASSWORD")
table_treeview.column("PASSWORD", width=150)

table_treeview.grid(row=0, column=0, sticky="nsew")

open_table(table_treeview)
scrollbar = ttk.Scrollbar(right_panel, orient=tk.VERTICAL, command=table_treeview.yview)
table_treeview.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")


root.mainloop()