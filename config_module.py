import tkinter as tk
from tkinter import filedialog



class Choice:
    def __init__(self, master):
        self.master = master
        self.origin_folder = tk.StringVar()
        self.destination_folder = tk.StringVar()
        self.struc_selection = tk.IntVar()

        tk.Label(master, text="Select Origin Folder:").pack()
        tk.Entry(master, textvariable=self.origin_folder, width=30).pack()
        tk.Button(master, text="...", command=self.get_origin).pack()

        tk.Label(master, text="Select Destination Folder:").pack()
        tk.Entry(master, textvariable=self.destination_folder, width=30).pack()
        tk.Button(master, text="...", command=self.get_destination).pack()

        tk.Label(master, text="Structure:").pack()
        tk.Radiobutton(master, text="1. YYYY-MM-DD", variable=self.struc_selection, value=1).pack()
        tk.Radiobutton(master, text="2. MM-DD", variable=self.struc_selection, value=2).pack()
        tk.Radiobutton(master, text="3. YYYY/MM/DD", variable=self.struc_selection, value=3).pack()
        tk.Radiobutton(master, text="4. YYYYMMDD", variable=self.struc_selection, value=4).pack()

        tk.Button(master, text="OK", command=self.accept).pack()

    def get_origin(self):
        self.origin_folder.set(tk.filedialog.askdirectory())
        return self.origin_folder.get()

    def get_destination(self):
        self.destination_folder.set(tk.filedialog.askdirectory())
        return self.destination_folder.get()

    def accept(self):
        self.origin = self.origin_folder.get()
        self.destination = self.destination_folder.get()
        self.structure = self.struc_selection.get()
        self.master.destroy()

# root = tk.Tk()
# app = Choice(root)
# root.mainloop()
