from tkinter import *
from views.DayDetailsView import DayDetailsView


class DayDetailsController:

    def __init__(self, model, day_index):
        self.model = model
        self.day_index = day_index
        self.window = Toplevel()
        self.view = DayDetailsView(self.window, self, self.model)
        self.window.geometry("450x240")
        self.window.title("Details")
        self.window.configure(bg='#FFFFFF')
        self.window.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize=75, weight=1)
        self.window.mainloop()
