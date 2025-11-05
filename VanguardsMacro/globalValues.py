class GlobalValues:
    def __init__(self):
        self.dx = 200
        self.dy = 100
        self.window_x = 1100
        self.window_y = 800
        self.stop_hotkey = 'l'
    def change_dx(self, num):
        self.dx = 200
    def change_dy(self, num):
        self.dy = num
    def change_window_x(self, num):
        self.window_x = num
    def change_window_y(self, num):
        self.window_y = num
    def change_self_hotkey(self, char):
        self.stop_hotkey = char

global_values = GlobalValues()

