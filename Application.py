from tkinter import *
from config import APP
from frames import MainFrame

app = Tk()
main_frame = MainFrame(APP.app_info(app))
main_frame.pack()
app.mainloop()
