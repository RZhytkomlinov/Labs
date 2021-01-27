import tkinter as tk


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):

        tasks = [Home, Zad1, Zad2, Zad3, Zad4, Zad5, Zad6, Zad7]

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid(column=0, row=0)

        self.frames = {}

        for shown in tasks:
            shown_name = shown.__name__
            frame = shown(parent=container, controller=self)
            self.frames[shown_name] = frame
            frame.grid(row='0', column='0', sticky='snew')

        self.show_frame('Home')

    def show_frame(self, shown_name):
        frame = self.frames[shown_name]
        frame.tkraise()


class Home(tk.Frame, tk.StringVar):
    def __init__(self, parent, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.buttons()

    def buttons(self):
        tasks = [Zad1, Zad2, Zad3, Zad4, Zad5, Zad6, Zad7]
        i = 1
        for page in tasks:
            page_name = page.__name__
            button = tk.Button(
                self, text=i, command=lambda page_name=page_name: self.controller.show_frame(page_name)).pack()
            i+=1


class Zad1(tk.Frame):
    def __init__(self, parent, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        text = tk.StringVar()
        label = tk.Label(self, text="Wprowadź kwotę brutto:")
        brutto_input = tk.Entry(self, textvariable=text)
        show = tk.Button(self, text="Show", command=lambda: self.netto(text))
        label.pack()
        brutto_input.pack()
        show.pack()

    def netto(self, text):
        self.text = text
        netto_output = tk.Label(self, height=2, width=15, text='Suma netto: ' + text.get())
        netto_output.pack()
        # try:
        #     brutto = float(input.get())
        #     print(brutto)
        # except:
        #     e = tk.Label(self, text='Wprowadź kwotę, a nie String')


class Zad2(tk.Frame):
    def __init__(self, parent, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        Label = tk.Label(self, text="Wprowadź kwotę brutto:")
        input = tk.Entry(self)
        try:
            brutto = float(input.get())
        except:
            e = tk.Label(self, text='Wprowadź kwotę, a nie String')


class Zad3(tk.Frame):
    def __init__(self, parent, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        Label = tk.Label(self, text="Wprowadź kwotę brutto:")
        input = tk.Entry(self)
        try:
            brutto = float(input.get())
        except:
            e = tk.Label(self, text='Wprowadź kwotę, a nie String')


class Zad4(tk.Frame):
    def __init__(self, parent, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        Label = tk.Label(self, text="Wprowadź kwotę brutto:")
        input = tk.Entry(self)
        try:
            brutto = float(input.get())
        except:
            e = tk.Label(self, text='Wprowadź kwotę, a nie String')


class Zad5(tk.Frame):
    def __init__(self, parent, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        Label = tk.Label(self, text="Wprowadź kwotę brutto:")
        input = tk.Entry(self)
        try:
            brutto = float(input.get())
        except:
            e = tk.Label(self, text='Wprowadź kwotę, a nie String')


class Zad6(tk.Frame):
    def __init__(self, parent, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        Label = tk.Label(self, text="Wprowadź kwotę brutto:")
        input = tk.Entry(self)
        try:
            brutto = float(input.get())
        except:
            e = tk.Label(self, text='Wprowadź kwotę, a nie String')


class Zad7(tk.Frame):
    def __init__(self, parent, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        Label = tk.Label(self, text="Kurwa kwotę brutto:")
        Label.pack()
        input = tk.Entry(self)
        try:
            brutto = float(input.get())
        except:
            e = tk.Label(self, text='Wprowadź kwotę, a nie String')


if __name__ == "__main__":
    app = Main()
    app.title('Lista Zaliczeniowa')
    app.geometry('500x500')
    app.mainloop()
