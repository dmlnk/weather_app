from tkinter import *
from views.PollutionView import PollutionView


class PollutionController:

    def __init__(self, model):
        self.model = model
        self.window = Toplevel()
        self.view = PollutionView(self.window, self, self.model)
        self.window.geometry("360x220")
        self.window.title("Air pollution")
        self.window.configure(bg='#FFFFFF')
        self.window.columnconfigure([0,1], minsize=10, weight=10)
        self.window.rowconfigure([2], minsize=20, weight=10)
        self.window.mainloop()
