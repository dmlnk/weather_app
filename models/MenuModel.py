class MenuModel:

    def __init__(self):
        self.recent_list = []

    def save_request(self, user_input):
        length = len(self.recent_list)
        if length > 0 and self.recent_list[length-1] == user_input or user_input=="":
            return

        if length < 10:
            self.recent_list.append(user_input)
        else:
            self.recent_list.pop(0)
            self.recent_list.append(user_input)

        self.export_to_file()

    def export_to_file(self):
        file = open("comm_hist.txt", "w", encoding="utf-8")

        if file is None:
            file = open("comm_hist.txt", "x", encoding="utf-8")

        file.write("SEARCH_HISTORY\n")
        for search in self.recent_list:
            file.write(str(search) + '\n')
        file.close()

    def read_file(self):
        try:
            file = open("comm_hist.txt", "r", encoding="utf-8")
        except FileNotFoundError:
            return None

        if file.readline() == "SEARCH_HISTORY\n":
            while True:
                line = file.readline()
                if not line:
                    break
                self.recent_list.append(line.rstrip("\n"))
        else:
            return None
        file.close()
