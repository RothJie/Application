__all__ = ["APP"]

from tkinter import Tk
from tool import INFO


class APP:
    app_title = ""
    app_WIDTH = 0
    app_HEIGHT = 0
    win_WIDTH = 0
    win_HEIGHT = 0

    @classmethod
    def app_info(cls, master):
        cls.get_app_info()
        master.title(cls.app_title)
        master.geometry("{}x{}+{}+{}".format(*cls.geo(master)))
        return master

    @classmethod
    def get_app_info(cls):
        cls.app_title, cls.app_WIDTH, cls.app_HEIGHT = INFO.app_info()

    @classmethod
    def geo(cls, master: Tk):
        cls.win_WIDTH = Tk.winfo_screenwidth(master)
        cls.win_HEIGHT = Tk.winfo_screenheight(master)
        geometery = (cls.app_WIDTH, cls.app_HEIGHT, int((cls.win_WIDTH - cls.app_WIDTH) / 2),
                     int((cls.win_HEIGHT - cls.app_HEIGHT) / 2))
        return geometery
