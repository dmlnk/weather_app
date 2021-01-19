import webbrowser
from tkinter import *
from models.WeatherModel import WeatherModel
from models.MenuModel import MenuModel
from views.MenuView import MenuView
from controllers.WeatherController import WeatherController
from controllers.PollutionController import PollutionController


class MenuController:

    def __init__(self):
        self.weather_model = None
        self.model = MenuModel()
        self.root = Tk()
        self.view = MenuView(self.root, self)

        self.root.rowconfigure([1], minsize=10, weight=1)
        self.root.columnconfigure([0, 1, 2], minsize=10, weight=1)
        self.root.geometry("400x170")
        self.root.title("Open weather map client")
        self.root.configure(bg='#ffffff')

        self.load_list()
        self.root.mainloop()

    def prepare_to_perform(self):
        self.send_msg_status_bar("Opening forecast. This may take a while")
        self.weather_model = WeatherModel()
        user_input = self.view.input_cbox.get()

        self.save_request(user_input)
        self.update_recent_list()

        if self.weather_model.current_api_call(user_input) is False:
            self.send_msg_status_bar("City not found")
            return

        city_coords = self.weather_model.get_coords()
        if city_coords is None:
            self.send_msg_status_bar('City not found')
            return

        return city_coords

    def show_forecast(self):
        city_coords = self.prepare_to_perform()
        if city_coords is None:
            return

        lat = city_coords["lat"]
        lon = city_coords["lon"]
        self.weather_model.weather_api_call(lat, lon)
        self.send_msg_status_bar("Done")
        WeatherController(self.weather_model)

    def show_map(self, zoom=10, cities=True):
        city_coords = self.prepare_to_perform()
        if city_coords is None:
            return

        lat = city_coords["lat"]
        lon = city_coords["lon"]
        webbrowser.open('https://openweathermap.org/weathermap?basemap=map&cities=%s&layer=radar&lat=%s&lon=%s&zoom=%d' \
                        % (str(cities).lower(), lat, lon, zoom))
        self.send_msg_status_bar("Done")

    def show_pollution(self):
        city_coords = self.prepare_to_perform()
        lat = city_coords["lat"]
        lon = city_coords["lon"]
        self.weather_model.pollution_api_call(lat, lon)
        self.send_msg_status_bar("Done")
        PollutionController(self.weather_model)

    def send_msg_status_bar(self, message):
        self.view.statusbar.config(text=message)

    def save_request(self, user_input):
        self.model.save_request(user_input)

    def load_list(self):
        self.model.read_file()
        self.update_recent_list()

    def update_recent_list(self):
        self.view.input_cbox['values'] = self.model.recent_list[::-1]
