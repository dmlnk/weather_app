import webbrowser
from tkinter import *
from views.WeatherView import WeatherView
from controllers.DayDetailsController import DayDetailsController


class WeatherController:

    def __init__(self, model):
        self.nav_index = 0
        self.model = model
        self.city_id = self.model.get_city_id()
        self.window = Toplevel()
        self.view = WeatherView(self.window, self, self.model)
        self.window.geometry("660x460")
        self.window.title("Weather")
        self.window.configure(bg='#FFFFFF')
        self.window.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize=70, weight=1)
        self.window.mainloop()

    def forward(self):
        hourly = self.view.hourly
        if self.nav_index + 7 < len(hourly):
            self.nav_index += 1
            for i in range(7):
                self.view.h_temp_list[i].config(text="{}°C".format(int(hourly[self.nav_index + i]['temp'])))
                self.view.h_cond_list[i].config(text=hourly[self.nav_index + i]['weather'][0]['main'])
                self.view.h_time_list[i].config(text=self.model.get_time(hourly[self.nav_index + i]['dt']))
                self.view.h_day_list[i].config(text=self.model.get_day(hourly[self.nav_index + i]['dt']))

    def backward(self):
        hourly = self.view.hourly
        if self.nav_index >= 1:
            self.nav_index -= 1
            for i in range(7):
                self.view.h_temp_list[i].config(text="{}°C".format(int(hourly[self.nav_index + i]['temp'])))
                self.view.h_cond_list[i].config(text=hourly[self.nav_index + i]['weather'][0]['main'] + "")
                self.view.h_time_list[i].config(text=self.model.get_time(hourly[self.nav_index + i]['dt']))
                self.view.h_day_list[i].config(text=self.model.get_day(hourly[self.nav_index + i]['dt']))

    def show_day_details(self, day_index):
        DayDetailsController(self.model, day_index)

    def open_web(self):
        webbrowser.open("https://openweathermap.org/city/{}".format(self.city_id), new=1)

