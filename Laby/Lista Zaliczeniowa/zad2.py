import tkinter as tk

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top',fill='both')
        container.grid(row=0, column = 0)

        pages = []
        self.frames = {}

        for shown in pages:
            shown_name = shown.__name__
            frame = shown(parent=container, controller=self)
            self.frames[shown_name] = frame
            frame.grid(row=0, column = 0)