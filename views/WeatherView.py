from tkinter import *


class WeatherView:

    def __init__(self, master, controller, model):
        self.model = model
        self.controller = controller
        self.start_index = 0

        self.window_fill_color = 'white'
        self.font_color_focused = '#000000'
        self.font_color = '#707070'
        self.font_style = "Segoe UI"

        self.frame_border_color = '#E5E5E5'
        self.frame_fill_color = '#FBFBFB'

        self.info_label_width = 16
        self.info_label_anchor = 'w'
        self.info_label_font_size = 11

        # 0 ROW
        self.top_bar_frame = Frame(master, background=self.window_fill_color)
        self.top_bar_frame.grid(row=0, column=0, columnspan=7, sticky="ew")

        self.title_label = Label(self.top_bar_frame,
                                 text="{} - {}".format(self.model.get_location(), self.model.get_weather_description()),
                                 font=(self.font_style, 16),
                                 padx=20, pady=7,
                                 background=self.window_fill_color,
                                 fg=self.font_color)
        self.title_label.pack(side='left')

        self.date_label = Label(self.top_bar_frame,
                                text=self.model.get_time_date(),
                                font=(self.font_style, 16),
                                padx=20, pady=7,
                                background=self.window_fill_color,
                                fg=self.font_color)
        self.date_label.pack(side='right')

        # 1 ROW
        self.weather_image = PhotoImage(file=self.model.get_icon())
        self.weather_label = Label(master,
                                   image=self.weather_image,
                                   height=50, width=65,
                                   anchor=CENTER,
                                   background=self.window_fill_color,
                                   fg=self.font_color)
        self.weather_label.grid(row=1, column=0, rowspan=3)

        self.temp_label = Label(master,
                                text=self.model.get_temperature(),
                                font=(self.font_style, 26),
                                background=self.window_fill_color,
                                fg=self.font_color_focused)
        self.temp_label.grid(row=1, column=1, rowspan=3)

        # Table information block
        self.info_frame = Frame(master, width=80, height=60)
        self.info_frame.grid(row=1, column=2, columnspan=5, rowspan=3)

        self.feels_like = Label(self.info_frame,
                                text=self.model.get_feels_like(),
                                background=self.window_fill_color,
                                anchor=self.info_label_anchor,
                                width=self.info_label_width,
                                font=(self.font_style, self.info_label_font_size),
                                fg=self.font_color)
        self.feels_like.grid(row=0, column=0, columnspan=1)

        self.visibility = Label(self.info_frame,
                                text=self.model.get_visibility(),
                                background=self.window_fill_color,
                                anchor=self.info_label_anchor,
                                width=self.info_label_width,
                                font=(self.font_style, self.info_label_font_size),
                                fg=self.font_color)
        self.visibility.grid(row=0, column=1, columnspan=1)

        self.wind = Label(self.info_frame, text=self.model.get_wind(),
                          background=self.window_fill_color,
                          anchor=self.info_label_anchor,
                          width=self.info_label_width,
                          font=(self.font_style, self.info_label_font_size),
                          fg=self.font_color)
        self.wind.grid(row=0, column=2, columnspan=1)

        # 2 ROW
        self.humidity = Label(self.info_frame, text=self.model.get_humidity(),
                              background=self.window_fill_color,
                              anchor=self.info_label_anchor,
                              width=self.info_label_width,
                              font=(self.font_style, self.info_label_font_size),
                              fg=self.font_color)
        self.humidity.grid(row=1, column=0, columnspan=1)

        self.sunrise = Label(self.info_frame, text=self.model.get_sunrise(),
                             background=self.window_fill_color,
                             anchor=self.info_label_anchor,
                             width=self.info_label_width,
                             font=(self.font_style, self.info_label_font_size),
                             fg=self.font_color)
        self.sunrise.grid(row=1, column=1, columnspan=1)

        self.uv = Label(self.info_frame, text=self.model.get_uvi(),
                        background=self.window_fill_color,
                        anchor=self.info_label_anchor,
                        width=self.info_label_width,
                        font=(self.font_style, self.info_label_font_size),
                        fg=self.font_color)
        self.uv.grid(row=1, column=2, columnspan=1)

        # 3 ROW
        self.clouds = Label(self.info_frame, text=self.model.get_clouds(),
                            background=self.window_fill_color,
                            anchor=self.info_label_anchor,
                            width=self.info_label_width,
                            font=(self.font_style, self.info_label_font_size),
                            fg=self.font_color)
        self.clouds.grid(row=2, column=0, columnspan=1)

        self.sunset = Label(self.info_frame, text=self.model.get_sunset(),
                            background=self.window_fill_color,
                            anchor=self.info_label_anchor,
                            width=self.info_label_width,
                            font=(self.font_style, self.info_label_font_size),
                            fg=self.font_color)
        self.sunset.grid(row=2, column=1, columnspan=1)

        self.pressure = Label(self.info_frame, text=self.model.get_pressure(),
                              background=self.window_fill_color,
                              anchor=self.info_label_anchor,
                              width=self.info_label_width,
                              font=(self.font_style, self.info_label_font_size),
                              fg=self.font_color)
        self.pressure.grid(row=2, column=2, columnspan=1)

        # 4 ROW
        self.hourly_label = Label(master, text="Hourly",
                                  font=(self.font_style, 16),
                                  background=self.window_fill_color,
                                  padx=10, pady=5,
                                  width=7,
                                  anchor=self.info_label_anchor,
                                  fg=self.font_color)
        self.hourly_label.grid(row=4, column=0)

        self.buttons_frame = Frame(master, background=self.frame_border_color)
        self.buttons_frame.grid(row=4, column=6, columnspan=1)

        self.back_btn = Button(self.buttons_frame, text="<", width=3, relief=RIDGE,
                               background=self.window_fill_color, command=lambda: self.controller.backward(),
                               activebackground=self.frame_border_color, highlightthickness=0,
                               foreground=self.font_color, borderwidth=0, font=(self.font_style, 9))
        self.back_btn.pack(side="left", padx=2, pady=2)

        self.forward_btn = Button(self.buttons_frame, text=">", width=3, relief=RIDGE,
                                  background=self.window_fill_color, command=lambda: self.controller.forward(),
                                  activebackground=self.frame_border_color, highlightthickness=0,
                                  foreground=self.font_color, borderwidth=0, font=(self.font_style, 9))
        self.forward_btn.pack(side="right", padx=2, pady=2)

        # 5 ROW - Hourly tiles
        self.hourly_frame = Frame(master, background=self.frame_fill_color)
        self.hourly_frame.grid(row=5, column=0, columnspan=7)

        # List to make possible list scrolling
        self.h_temp_list = []
        self.h_cond_list = []
        self.h_time_list = []
        self.h_day_list = []
        self.hourly = self.model.get_hourly_info()

        # Hourly tiles drawing
        for i in range(7):
            self.hour_frame = Frame(self.hourly_frame,
                                    highlightbackground=self.frame_border_color,
                                    highlightthickness=1,
                                    background=self.frame_fill_color)
            self.hour_frame.grid(row=5, column=i, columnspan=1, padx=7)

            self.hour_temp = Label(self.hour_frame,
                                   font=(self.font_style, 18),
                                   text="{}°C".format(int(self.hourly[i]['temp'])),
                                   background=self.frame_fill_color,
                                   fg=self.font_color_focused)
            self.hour_temp.pack(side='top')
            self.h_temp_list.append(self.hour_temp)

            self.hour_cond = Label(self.hour_frame,
                                   text=self.hourly[i]['weather'][0]['main'],
                                   background=self.frame_fill_color,
                                   fg=self.font_color)
            self.hour_cond.pack(pady=2)
            self.h_cond_list.append(self.hour_cond)

            self.hour_time = Label(self.hour_frame,
                                   text=self.model.get_time(self.hourly[i]['dt']),
                                   background=self.frame_fill_color,
                                   fg=self.font_color)
            self.hour_time.pack(ipadx=20)
            self.h_time_list.append(self.hour_time)

            self.hour_day = Label(self.hour_frame,
                                  text=self.model.get_day(self.hourly[i]['dt']),
                                  background=self.frame_fill_color,
                                  fg=self.font_color)
            self.hour_day.pack(side='bottom')
            self.h_day_list.append(self.hour_day)

        # 6 ROW
        self.daily_label = Label(master, text="Daily", font=(self.font_style, 16),
                                 background=self.window_fill_color,
                                 padx=10, pady=5, width=7, anchor=self.info_label_anchor, fg=self.font_color)
        self.daily_label.grid(row=6, column=0)

        # 7 ROW - Daily tiles drawing
        self.daily_frame = Frame(master, background=self.frame_fill_color)
        self.daily_frame.grid(row=7, column=0, columnspan=7)
        daily = self.model.get_daily_info()

        # Frame 0
        self.daily_frame0 = Frame(self.daily_frame,
                                  width=80, height=60,
                                  highlightbackground=self.frame_border_color,
                                  highlightthickness=1,
                                  background=self.frame_fill_color)
        self.daily_frame0.grid(row=5, column=0, columnspan=1, padx=7)

        self.day_temp0 = Label(self.daily_frame0, font=(self.font_style, 18),
                               text="{}°C".format(int(daily[0]['temp']['day'])),
                               background=self.frame_fill_color, fg=self.font_color_focused)
        self.day_temp0.pack(side='top')

        self.day_cond0 = Label(self.daily_frame0, text=daily[0]['weather'][0]['main'],
                               background=self.frame_fill_color,
                               fg=self.font_color)
        self.day_cond0.pack()

        date = self.model.get_full_day(daily[0]['dt'])
        self.day_date0 = Label(self.daily_frame0, text=date, background=self.frame_fill_color, fg=self.font_color)
        self.day_date0.pack()

        self.details_btn0 = Button(self.daily_frame0,
                                   text="Details",
                                   width=5, relief=RIDGE,
                                   command=lambda: self.controller.show_day_details(0),
                                   background=self.window_fill_color,
                                   activebackground=self.frame_border_color,
                                   highlightthickness=0,
                                   foreground=self.font_color,
                                   borderwidth=0, font=(self.font_style, 9))
        self.details_btn0.pack(side='bottom', ipadx=16)

        # Frame 1 _________________________________________________________________________________
        self.daily_frame1 = Frame(self.daily_frame, width=80, height=60,
                                  highlightbackground=self.frame_border_color,
                                  highlightthickness=1,
                                  background=self.frame_fill_color)
        self.daily_frame1.grid(row=5, column=1, columnspan=1, padx=7)

        self.day_temp1 = Label(self.daily_frame1, font=(self.font_style, 18),
                               text="{}°C".format(int(daily[1]['temp']['day'])),
                               background=self.frame_fill_color, fg=self.font_color_focused)
        self.day_temp1.pack(side='top')

        self.day_cond1 = Label(self.daily_frame1, text=daily[1]['weather'][0]['main'],
                               background=self.frame_fill_color,
                               fg=self.font_color)
        self.day_cond1.pack()

        date = self.model.get_full_day(daily[1]['dt'])
        self.day_date1 = Label(self.daily_frame1, text=date, background=self.frame_fill_color, fg=self.font_color)
        self.day_date1.pack()

        self.details_btn1 = Button(self.daily_frame1,
                                   text="Details",
                                   width=5, relief=RIDGE,
                                   command=lambda: self.controller.show_day_details(1),
                                   background=self.window_fill_color,
                                   activebackground=self.frame_border_color,
                                   highlightthickness=0,
                                   foreground=self.font_color,
                                   borderwidth=0, font=(self.font_style, 9))
        self.details_btn1.pack(side='bottom', ipadx=16)

        # Frame 2 _________________________________________________________________________________
        self.daily_frame2 = Frame(self.daily_frame,
                                  width=80, height=60,
                                  highlightbackground=self.frame_border_color,
                                  highlightthickness=1,
                                  background=self.frame_fill_color)
        self.daily_frame2.grid(row=5, column=2, columnspan=1, padx=7)

        self.day_temp2 = Label(self.daily_frame2, font=(self.font_style, 18),
                               text="{}°C".format(int(daily[2]['temp']['day'])),
                               background=self.frame_fill_color, fg=self.font_color_focused)
        self.day_temp2.pack(side='top')

        self.day_cond2 = Label(self.daily_frame2, text=daily[2]['weather'][0]['main'],
                               background=self.frame_fill_color,
                               fg=self.font_color)
        self.day_cond2.pack()

        date = self.model.get_full_day(daily[2]['dt'])
        self.day_date2 = Label(self.daily_frame2, text=date, background=self.frame_fill_color, fg=self.font_color)
        self.day_date2.pack()

        self.details_btn2 = Button(self.daily_frame2,
                                   text="Details",
                                   width=5, relief=RIDGE,
                                   command=lambda: self.controller.show_day_details(2),
                                   background=self.window_fill_color,
                                   activebackground=self.frame_border_color, highlightthickness=0,
                                   foreground=self.font_color,
                                   borderwidth=0, font=(self.font_style, 9))
        self.details_btn2.pack(side='bottom', ipadx=16)

        # Frame 3 _________________________________________________________________________________
        self.daily_frame3 = Frame(self.daily_frame,
                                  width=80, height=60,
                                  highlightbackground=self.frame_border_color,
                                  highlightthickness=1,
                                  background=self.frame_fill_color)
        self.daily_frame3.grid(row=5, column=3, columnspan=1, padx=7)

        self.day_temp3 = Label(self.daily_frame3, font=(self.font_style, 18),
                               text="{}°C".format(int(daily[3]['temp']['day'])),
                               background=self.frame_fill_color, fg=self.font_color_focused)
        self.day_temp3.pack(side='top')

        self.day_cond3 = Label(self.daily_frame3, text=daily[3]['weather'][0]['main'],
                               background=self.frame_fill_color,
                               fg=self.font_color)
        self.day_cond3.pack()

        date = self.model.get_full_day(daily[3]['dt'])
        self.day_date3 = Label(self.daily_frame3, text=date, background=self.frame_fill_color, fg=self.font_color)
        self.day_date3.pack()

        self.details_btn3 = Button(self.daily_frame3,
                                   text="Details",
                                   width=5, relief=RIDGE,
                                   command=lambda: self.controller.show_day_details(3),
                                   background=self.window_fill_color,
                                   activebackground=self.frame_border_color,
                                   highlightthickness=0,
                                   foreground=self.font_color,
                                   borderwidth=0, font=(self.font_style, 9))
        self.details_btn3.pack(side='bottom', ipadx=16)

        # Frame 4 _________________________________________________________________________________
        self.daily_frame4 = Frame(self.daily_frame,
                                  width=80, height=60,
                                  highlightbackground=self.frame_border_color,
                                  highlightthickness=1,
                                  background=self.frame_fill_color)
        self.daily_frame4.grid(row=5, column=4, columnspan=1, padx=7)

        self.day_temp4 = Label(self.daily_frame4, font=(self.font_style, 18),
                               text="{}°C".format(int(daily[4]['temp']['day'])),
                               background=self.frame_fill_color, fg=self.font_color_focused)
        self.day_temp4.pack(side='top')

        self.day_cond4 = Label(self.daily_frame4, text=daily[4]['weather'][0]['main'],
                               background=self.frame_fill_color,
                               fg=self.font_color)
        self.day_cond4.pack()

        date = self.model.get_full_day(daily[4]['dt'])
        self.day_date4 = Label(self.daily_frame4, text=date, background=self.frame_fill_color, fg=self.font_color)
        self.day_date4.pack()

        self.details_btn4 = Button(self.daily_frame4,
                                   text="Details",
                                   width=5, relief=RIDGE,
                                   command=lambda: self.controller.show_day_details(4),
                                   background=self.window_fill_color,
                                   activebackground=self.frame_border_color,
                                   highlightthickness=0,
                                   foreground=self.font_color,
                                   borderwidth=0, font=(self.font_style, 9))
        self.details_btn4.pack(side='bottom', ipadx=16)

        # Frame 5 _________________________________________________________________________________
        self.daily_frame5 = Frame(self.daily_frame,
                                  width=80, height=60,
                                  highlightbackground=self.frame_border_color,
                                  highlightthickness=1,
                                  background=self.frame_fill_color)
        self.daily_frame5.grid(row=5, column=5, columnspan=1, padx=7)

        self.day_temp5 = Label(self.daily_frame5, font=(self.font_style, 18),
                               text="{}°C".format(int(daily[5]['temp']['day'])),
                               background=self.frame_fill_color, fg=self.font_color_focused)
        self.day_temp5.pack(side='top')

        self.day_cond5 = Label(self.daily_frame5, text=daily[5]['weather'][0]['main'],
                               background=self.frame_fill_color,
                               fg=self.font_color)
        self.day_cond5.pack()

        date = self.model.get_full_day(daily[5]['dt'])
        self.day_date5 = Label(self.daily_frame5, text=date, background=self.frame_fill_color, fg=self.font_color)
        self.day_date5.pack()

        self.details_btn5 = Button(self.daily_frame5,
                                   text="Details",
                                   width=5, relief=RIDGE,
                                   command=lambda: self.controller.show_day_details(5),
                                   background=self.window_fill_color,
                                   activebackground=self.frame_border_color,
                                   highlightthickness=0,
                                   foreground=self.font_color,
                                   borderwidth=0, font=(self.font_style, 9))
        self.details_btn5.pack(side='bottom', ipadx=16)

        # Frame 6 _________________________________________________________________________________
        self.daily_frame6 = Frame(self.daily_frame, width=80, height=60,
                                  highlightbackground=self.frame_border_color,
                                  highlightthickness=1,
                                  background=self.frame_fill_color)
        self.daily_frame6.grid(row=5, column=6, columnspan=1, padx=7)

        self.day_temp6 = Label(self.daily_frame6, font=(self.font_style, 18),
                               text="{}°C".format(int(daily[6]['temp']['day'])),
                               background=self.frame_fill_color, fg=self.font_color_focused)
        self.day_temp6.pack(side='top')

        self.day_cond6 = Label(self.daily_frame6, text=daily[6]['weather'][0]['main'],
                               background=self.frame_fill_color,
                               fg=self.font_color)
        self.day_cond6.pack()

        date = self.model.get_full_day(daily[6]['dt'])
        self.day_date6 = Label(self.daily_frame6, text=date, background=self.frame_fill_color, fg=self.font_color)
        self.day_date6.pack()

        # Bottom button
        self.details_btn6 = Button(self.daily_frame6,
                                   text="Details",
                                   width=5, relief=RIDGE,
                                   command=lambda: self.controller.show_day_details(6),
                                   background=self.window_fill_color,
                                   activebackground=self.frame_border_color,
                                   highlightthickness=0,
                                   foreground=self.font_color,
                                   borderwidth=0, font=(self.font_style, 9))
        self.details_btn6.pack(side='bottom', ipadx=16)

        # 8 ROW
        self.browser_btn = Button(master, text="Open in web browser",
                                  width=100, height=2, relief=RIDGE,
                                  background=self.window_fill_color,
                                  command=lambda: self.controller.open_web(),
                                  activebackground=self.frame_border_color,
                                  highlightthickness=0,
                                  foreground=self.font_color,
                                  borderwidth=0, font=(self.font_style, 9))
        self.browser_btn.grid(row=8, column=0, columnspan=7)

