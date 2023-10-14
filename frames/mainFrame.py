from config import APP
from tkinter import *


class MainFrame(Frame):
    def __init__(self, master: Tk, **kwargs):
        super(MainFrame, self).__init__(master, **kwargs)
        self.configInfo()

    def configInfo(self):
        """配置该窗口的信息"""

    def widget(self):
        """该窗口的组件"""
        pass
