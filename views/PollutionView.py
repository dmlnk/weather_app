from tkinter import *


class PollutionView:

    def __init__(self, master, controller, model):
        self.model = model
        self.controller = controller

        self.window_fill_color = 'white'
        self.font_color = '#707070'
        self.font_style = "Segoe UI"
        self.label_font_size = 10
        self.label_width = 20
        self.label_anchor = 'w'

        self.quality_index = Label(master,
                                   text="Air Quality:",
                                   background=self.window_fill_color,
                                   anchor="w",
                                   font=(self.font_style, 12), )
        self.quality_index.grid(row=0, column=0, columnspan=2, sticky="ew")

        answer = self.model.get_quality_index()
        self.quality_index = Label(master,
                                   text=answer['status'],
                                   background=self.window_fill_color,
                                   anchor="c",
                                   font=(self.font_style, 26, 'bold'),
                                   fg=answer['color'])
        self.quality_index.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.quality_index = Label(master,
                                   text="Concentration of:",
                                   background=self.window_fill_color,
                                   anchor="w",
                                   font=(self.font_style, 12))
        self.quality_index.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.info_bar_frame = Frame(master, width=50, background=self.window_fill_color, )
        self.info_bar_frame.grid(row=3, column=1, columnspan=2, sticky='ew', pady=20)

        self.co_label = Label(self.info_bar_frame,
                              text=self.model.get_co(),
                              background=self.window_fill_color,
                              anchor=self.label_anchor,
                              width=self.label_width,
                              font=(self.font_style, self.label_font_size),
                              fg=self.font_color)
        self.co_label.grid(row=0, column=0, columnspan=1)

        self.no_label = Label(self.info_bar_frame,
                              text=self.model.get_no(),
                              background=self.window_fill_color,
                              anchor=self.label_anchor,
                              width=self.label_width,
                              font=(self.font_style, self.label_font_size),
                              fg=self.font_color)
        self.no_label.grid(row=1, column=0, columnspan=1)

        self.no2_label = Label(self.info_bar_frame,
                               text=self.model.get_no2(),
                               background=self.window_fill_color,
                               anchor=self.label_anchor,
                               width=self.label_width,
                               font=(self.font_style, self.label_font_size),
                               fg=self.font_color)
        self.no2_label.grid(row=2, column=0, columnspan=1)

        self.o3_label = Label(self.info_bar_frame,
                              text=self.model.get_o3(),
                              background=self.window_fill_color,
                              anchor=self.label_anchor,
                              width=self.label_width,
                              font=(self.font_style, self.label_font_size),
                              fg=self.font_color)
        self.o3_label.grid(row=3, column=0, columnspan=1)

        self.so2_label = Label(self.info_bar_frame,
                               text=self.model.get_so2(),
                               background=self.window_fill_color,
                               anchor=self.label_anchor,
                               width=self.label_width,
                               font=(self.font_style, self.label_font_size),
                               fg=self.font_color)
        self.so2_label.grid(row=0, column=1, columnspan=1)

        self.pm2_5_label = Label(self.info_bar_frame,
                                 text=self.model.get_pm2_5(),
                                 background=self.window_fill_color,
                                 anchor=self.label_anchor,
                                 width=self.label_width,
                                 font=(self.font_style, self.label_font_size),
                                 fg=self.font_color)
        self.pm2_5_label.grid(row=1, column=1, columnspan=1)

        self.pm10_label = Label(self.info_bar_frame,
                                text=self.model.get_pm10(),
                                background=self.window_fill_color,
                                anchor=self.label_anchor,
                                width=self.label_width,
                                font=(self.font_style, self.label_font_size),
                                fg=self.font_color)
        self.pm10_label.grid(row=2, column=1, columnspan=1)

        self.nh3_label = Label(self.info_bar_frame,
                               text=self.model.get_nh3(),
                               background=self.window_fill_color,
                               anchor=self.label_anchor,
                               width=self.label_width,
                               font=(self.font_style, self.label_font_size),
                               fg=self.font_color)
        self.nh3_label.grid(row=3, column=1, columnspan=1)
