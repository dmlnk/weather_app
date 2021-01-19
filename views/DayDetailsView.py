from tkinter import *
from tkinter import ttk


class DayDetailsView:

    def __init__(self, master, controller, model):
        self.model = model
        self.controller = controller
        self.start_index = 0

        self.window_fill_color = 'white'

        self.font_color_focused = '#000000'
        self.font_color = '#707070'
        self.font_size = 12
        self.font_style = "Segoe UI"

        self.frame_border_color = '#E5E5E5'

        self.temp_label_width = 8
        self.temp_label_anchor = 'c'

        self.title_width = 18
        self.title_anchor = 'w'
        self.title_font_size = 10
        day = self.controller.day_index

        # 0 ROW
        self.weather_image = PhotoImage(file=self.model.get_d_icon(day))
        self.weather_label = Label(master,
                                   image=self.weather_image,
                                   height=55,
                                   width=70,
                                   anchor=CENTER,
                                   background=self.window_fill_color,
                                   fg=self.font_color)
        self.weather_label.grid(row=0, column=0, rowspan=2, padx=10, ipadx=10, ipady=5)

        self.statu_date_label = Label(master,
                                      text="{} on {}".format(self.model.get_d_description(day), self.model.get_d_date(day)),
                                      background=self.window_fill_color,
                                      anchor=self.title_anchor,
                                      width=40,
                                      font=(self.font_style, 12, 'bold'),
                                      fg=self.font_color, )
        self.statu_date_label.grid(row=0, column=1, columnspan=5)

        self.high_low_label = Label(master,
                                    text='The high will be {}, the low will be {}'
                                    .format(model.get_d_max_temp(day),
                                    model.get_d_min_temp(day)),
                                    background=self.window_fill_color,
                                    anchor=self.title_anchor, width=40,
                                    font=(self.font_style, 12), fg=self.font_color)
        self.high_low_label.grid(row=1, column=1, columnspan=5)

        # Info frame
        self.info_bar_frame = Frame(master, background=self.window_fill_color)
        self.info_bar_frame.grid(row=2, column=0, rowspan=1, columnspan=6, pady=10)

        self.precipitation = Label(self.info_bar_frame,
                                   text=self.model.get_d_precipitation(day),
                                   background=self.window_fill_color,
                                   anchor=self.title_anchor,
                                   width=self.title_width,
                                   font=(self.font_style, self.title_font_size),
                                   fg=self.font_color)
        self.precipitation.grid(row=0, column=0, columnspan=1)

        self.humidity = Label(self.info_bar_frame,
                              text=self.model.get_d_humidity(day),
                              background=self.window_fill_color,
                              anchor=self.title_anchor,
                              width=self.title_width,
                              font=(self.font_style, self.title_font_size),
                              fg=self.font_color)
        self.humidity.grid(row=1, column=0, columnspan=1)

        self.wind = Label(self.info_bar_frame,
                          text=self.model.get_d_wind(day),
                          background=self.window_fill_color,
                          anchor=self.title_anchor,
                          width=self.title_width,
                          font=(self.font_style, self.title_font_size),
                          fg=self.font_color)
        self.wind.grid(row=0, column=1, columnspan=1)

        self.uv = Label(self.info_bar_frame,
                        text=self.model.get_d_uv(day),
                        background=self.window_fill_color,
                        anchor=self.title_anchor,
                        width=self.title_width,
                        font=(self.font_style, self.title_font_size),
                        fg=self.font_color)
        self.uv.grid(row=1, column=1, columnspan=1)

        self.pressure = Label(self.info_bar_frame,
                              text=self.model.get_d_pressure(day),
                              background=self.window_fill_color,
                              anchor=self.title_anchor, width=self.title_width,
                              font=(self.font_style, self.title_font_size), 
                              fg=self.font_color)
        self.pressure.grid(row=0, column=2, columnspan=1)

        self.dew_point = Label(self.info_bar_frame,
                               text=self.model.get_d_dew_point(day),
                               background=self.window_fill_color,
                               anchor=self.title_anchor, width=self.title_width,
                               font=(self.font_style, self.title_font_size), 
                               fg=self.font_color)
        self.dew_point.grid(row=1, column=2, columnspan=1)

        # Temperature details frame
        self.temp_bar_frame = Frame(master, background=self.window_fill_color,
                                    highlightbackground=self.frame_border_color,
                                    highlightthickness=1)
        self.temp_bar_frame.grid(row=3, column=0, rowspan=1, columnspan=6, pady=10)

        # Morning
        self.morn_label = Label(self.temp_bar_frame,
                                text="Morning",
                                background=self.window_fill_color,
                                anchor=self.temp_label_anchor,
                                width=self.temp_label_width,
                                font=(self.font_style, self.title_font_size, 'bold'),
                                fg=self.font_color)
        self.morn_label.grid(row=0, column=1, columnspan=1)

        self.morn_temp = Label(self.temp_bar_frame,
                               text=self.model.get_d_morn_temp(day),
                               background=self.window_fill_color,
                               anchor=self.temp_label_anchor,
                               width=self.temp_label_width,
                               font=(self.font_style, self.title_font_size),
                               fg=self.font_color)
        self.morn_temp.grid(row=1, column=1, columnspan=1)

        self.morn_feels = Label(self.temp_bar_frame,
                                text=self.model.get_d_morn_feels(day),
                                background=self.window_fill_color,
                                anchor=self.temp_label_anchor,
                                width=self.temp_label_width,
                                font=(self.font_style, self.title_font_size),
                                fg=self.font_color)
        self.morn_feels.grid(row=2, column=1, columnspan=1)

        # Afternoon
        self.aft_label = Label(self.temp_bar_frame,
                               text="Afternoon",
                               background=self.window_fill_color,
                               anchor=self.temp_label_anchor,
                               width=self.temp_label_width,
                               font=(self.font_style, self.title_font_size, 'bold'),
                               fg=self.font_color)
        self.aft_label.grid(row=0, column=2, columnspan=1)

        self.aft_temp = Label(self.temp_bar_frame,
                              text=self.model.get_d_day_temp(day),
                              background=self.window_fill_color,
                              anchor=self.temp_label_anchor,
                              width=self.temp_label_width,
                              font=(self.font_style, self.title_font_size),
                              fg=self.font_color)
        self.aft_temp.grid(row=1, column=2, columnspan=1)

        self.aft_feels = Label(self.temp_bar_frame,
                               text=self.model.get_d_day_feels(day),
                               background=self.window_fill_color,
                               anchor=self.temp_label_anchor,
                               width=self.temp_label_width,
                               font=(self.font_style, self.title_font_size),
                               fg=self.font_color)
        self.aft_feels.grid(row=2, column=2, columnspan=1)

        # Evening
        self.evn_label = Label(self.temp_bar_frame,
                               text="Evening",
                               background=self.window_fill_color,
                               anchor=self.temp_label_anchor,
                               width=self.temp_label_width,
                               font=(self.font_style, self.title_font_size, 'bold'),
                               fg=self.font_color)
        self.evn_label.grid(row=0, column=3, columnspan=1)

        self.evn_temp = Label(self.temp_bar_frame,
                              text=self.model.get_d_evn_temp(day),
                              background=self.window_fill_color,
                              anchor=self.temp_label_anchor,
                              width=self.temp_label_width,
                              font=(self.font_style, self.title_font_size),
                              fg=self.font_color)
        self.evn_temp.grid(row=1, column=3, columnspan=1)

        self.evn_feels = Label(self.temp_bar_frame,
                               text=self.model.get_d_evn_feels(day),
                               background=self.window_fill_color,
                               anchor=self.temp_label_anchor,
                               width=self.temp_label_width,
                               font=(self.font_style, self.title_font_size),
                               fg=self.font_color)
        self.evn_feels.grid(row=2, column=3, columnspan=1)

        # Night
        self.night_label = Label(self.temp_bar_frame,
                                 text="Night",
                                 background=self.window_fill_color,
                                 anchor=self.temp_label_anchor,
                                 width=self.temp_label_width,
                                 font=(self.font_style, self.title_font_size, 'bold'),
                                 fg=self.font_color)
        self.night_label.grid(row=0, column=4, columnspan=1)

        self.night_temp = Label(self.temp_bar_frame,
                                text=self.model.get_d_night_temp(day),
                                background=self.window_fill_color,
                                anchor=self.temp_label_anchor,
                                width=self.temp_label_width,
                                font=(self.font_style, self.title_font_size),
                                fg=self.font_color)
        self.night_temp.grid(row=1, column=4, columnspan=1)

        self.night_feels = Label(self.temp_bar_frame,
                                 text=self.model.get_d_night_feels(day),
                                 background=self.window_fill_color,
                                 anchor=self.temp_label_anchor,
                                 width=self.temp_label_width,
                                 font=(self.font_style, self.title_font_size),
                                 fg=self.font_color)
        self.night_feels.grid(row=2, column=4, columnspan=1)

        self.temp_label = Label(self.temp_bar_frame,
                                text="Temperature",
                                background=self.window_fill_color,
                                anchor=self.title_anchor,
                                width=self.temp_label_width + 5,
                                font=(self.font_style, self.title_font_size),
                                fg=self.font_color)
        self.temp_label.grid(row=1, column=0, columnspan=1)

        self.feels_label = Label(self.temp_bar_frame,
                                 text="Feels like",
                                 background=self.window_fill_color,
                                 anchor=self.title_anchor,
                                 width=self.temp_label_width + 5,
                                 font=(self.font_style, self.title_font_size),
                                 fg=self.font_color)
        self.feels_label.grid(row=2, column=0, columnspan=1)
