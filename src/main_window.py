import os
import tkinter as tk
import ttkbootstrap as ttk

from ttkbootstrap.constants import *

from .lib import *
from .terminal_tool import TerminalToolWindow
from .common_tools import RunsWindow
from .other_tools import OtherToolsWindow


class MainWindow:
    __root = None
    frame_show = None               # 当前显示界面
    runc_frame = None               # 启动器界面
    simple_tools_frame = None       # 小工具界面
    termianl_tools_frame = None     # 命令行工具界面
    about_frame = None              # 关于界面

    apps = get_runs_config()
    termianl_tools_config = get_terminal_tools_config()
    other_tools_config = get_other_tools_config()

    frames = []
    res = []

    def __init__(self):
        self.init_tk()
        self.init_menu()
        self.init_runs()
        self.init_simple_tools()
        self.init_terminal_tools()
        self.init_about()

        self.frame_show = self.simple_tools_frame
        self.frame_show.pack()

    def init_tk(self):
        self.__root = ttk.Window(themename="morph", iconphoto="res/images/icon.png")
        self.__root.title("NNZ")
        root_width = self.__root.winfo_screenwidth()
        root_height = self.__root.winfo_screenheight()
        self.__root.geometry(
            f"{int(root_width * 0.618)}x{int(root_height * 0.618)}+{int(root_width * 0.1)}+{int(root_height * 0.1)}")

    def init_menu(self):
        self.menu = tk.Menu(self.__root)
        self.__root.config(menu=self.menu)
        func = lambda x: (lambda: self.change_frame(x))

        self.menu.add_command(label="常用工具", command=lambda: self.change_frame(self.runc_frame))
        self.menu.add_command(label="便利工具", command=lambda: self.change_frame(self.simple_tools_frame))
        self.menu.add_command(label="终端工具", command=lambda: self.change_frame(self.termianl_tools_frame))
        func = lambda x: (lambda: self.change_frame(x))
        for i in self.other_tools_config:
            frame = ttk.Frame(self.__root)

            # frame = ttk.Frame(self.__root)
            OtherToolsWindow(frame, self.other_tools_config[i], i)
            self.menu.add_command(label=i, command=func(frame))

        self.menu.add_command(label="关于", command=lambda: self.change_frame(self.about_frame))

    def init_runs(self):
        self.runc_frame = ttk.Frame(self.__root)
        RunsWindow(self.runc_frame, self.apps)

    def init_simple_tools(self):
        self.simple_tools_frame = ttk.Frame(self.__root)
        a = "asd"

    def init_terminal_tools(self):

        self.termianl_tools_frame = ttk.Frame(self.__root)

        notebook = ttk.Notebook(self.termianl_tools_frame)
        notebook.pack(fill='both', expand=True, padx=5)

        for config in self.termianl_tools_config:

            tool = TerminalToolWindow(config)
            tool.init(notebook)

            # 左侧选项面板

    def other_tools(self):
        func = lambda x: (lambda: self.change_frame(x))
        for i in self.other_tools_config:
            frame = ttk.Frame(self.__root)

            # frame = ttk.Frame(self.__root)
            OtherToolsWindow(frame, self.other_tools_config[i])
            self.menu.add_command(label=i, command=func(frame))

    def init_about(self):
        self.about_frame = ttk.Frame(self.__root)
        about_str = "I'm Zer0-hex\n\nEmail: Zer0-hex@outlook.com\n\nBlog: https://Zer0-hex.github.io\n\nGithub: https://Github.com/Zer0-hex\n\n"
        tk.Label(self.about_frame, font=(None, 18), justify=CENTER, text=about_str).pack(side=TOP, fill=BOTH, expand=YES)

    def change_frame(self, frame):
        if self.frame_show is not frame:
            self.frame_show.pack_forget()
            self.frame_show = frame
            self.frame_show.pack(fill='both', expand=True)

    def loop(self):
        self.__root.mainloop()
