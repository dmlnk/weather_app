from tkinter import *
from tkinter import ttk


class MenuView:

    def __init__(self, master, controller):
        self.controller = controller

        self.window_fill_color = 'white'

        self.font_color = '#707070'
        self.font_size = 12
        self.btn_font_size = 10
        self.btn_width = 12
        self.font_style = "Segoe UI"

        self.frame_border_color = '#A1A0A0'
        self.frame_fill_color = '#F2F2F2'

        self.search_bar_frame = Frame(master, background=self.frame_fill_color,
                                      highlightbackground=self.frame_border_color,
                                      highlightthickness=2)
        self.search_bar_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=4, ipadx=5, ipady=5, sticky="ew")
        self.search_bar_frame.columnconfigure([0, 1, 2], minsize=1, weight=1)
        self.search_bar_frame.rowconfigure([0, 1, 2], minsize=1, weight=1)

        self.input_label = Label(self.search_bar_frame,
                                 text="Type a city name or choose from recent:",
                                 background='#F2F2F2',
                                 anchor="w",
                                 fg=self.font_color,
                                 font=(self.font_style, self.font_size, "bold"))
        self.input_label.grid(row=0, column=0, columnspan=3, padx=12, pady=2,sticky="ew")

        self.input_cbox = ttk.Combobox(self.search_bar_frame, width=40)
        self.input_cbox.grid(row=1, column=0, columnspan=3, padx=15, ipady=5, sticky="ew")

        self.map_btn = Button(master,
                              text="Open map",
                              font=(self.font_style, self.btn_font_size, "bold"),
                              width=self.btn_width,
                              background=self.window_fill_color,
                              foreground=self.font_color,
                              relief=RIDGE,
                              command=self.controller.show_map)
        self.map_btn.grid(row=1, column=0, ipady=5)

        self.air_btn = Button(master,
                              text="Air pollution",
                              font=(self.font_style, self.btn_font_size, "bold"),
                              width=self.btn_width,
                              background=self.window_fill_color,
                              foreground=self.font_color,
                              relief=RIDGE,
                              command=self.controller.show_pollution)
        self.air_btn.grid(row=1, column=1, ipady=5)

        self.forecast_btn = Button(master,
                                   text="Forecast",
                                   font=(self.font_style, self.btn_font_size, "bold"),
                                   width=self.btn_width,
                                   background=self.window_fill_color,
                                   foreground=self.font_color,
                                   relief=RIDGE,
                                   command=controller.show_forecast)
        self.forecast_btn.grid(row=1, column=2, ipady=5)

        self.statusbar = Label(master, bd=1, font=(self.font_style, 10, "bold"),
                               text="Ready", relief=SUNKEN, anchor=W,
                               background=self.window_fill_color)
        self.statusbar.grid(row=2, column=0, columnspan=3, sticky="ew", ipady=2)

