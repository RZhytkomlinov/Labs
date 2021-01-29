import tkinter as tk


class Main(tk.Frame):
    def __init__(self,parent):
        super(Main, self).__init__()
        parent = app

    def new(self):
        self.button.grid.forget()

    for page in range (0,7):
        button = tk.Button(
            text=f'Zadanie {page+1}', borderwidth=2, width=20, relief='groove', anchor='sw',
            command=new(parent)).grid(row=page, column=0, pady=5)


app = tk.Tk()

app.geometry('500x500')
app.mainloop()
