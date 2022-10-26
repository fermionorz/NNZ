import os
import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from ttkbootstrap.constants import *

from .lib import get_runs_config, get_terminal_tools_config
from .terminal_tool import TerminalToolWindow


class MainWindow:
    __root = None
    frame_show = None               # 当前显示界面
    runc_frame = None               # 启动器界面
    simple_tools_frame = None       # 小工具界面
    termianl_tools_frame = None     # 命令行工具界面
    about_frame = None              # 关于界面

    apps = get_runs_config()
    termianl_tools_config = get_terminal_tools_config()
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
        menu = tk.Menu(self.__root)
        self.__root.config(menu=menu)
        menu.add_command(label="启动器", command=lambda: self.change_frame(self.runc_frame))
        # menu.add_command(label="渗透小工具", command=lambda: self.change_frame(self.simple_tools_frame))
        menu.add_command(label="命令行工具", command=lambda: self.change_frame(self.termianl_tools_frame))
        menu.add_command(label="关于", command=lambda: self.change_frame(self.about_frame))

    def init_runs(self):
        self.runc_frame = ttk.Frame(self.__root)
        runs_frame = ttk.Frame(self.runc_frame, padding=10, borderwidth=1, relief='ridge')
        runs_frame.pack(fill=BOTH, expand=YES, padx=5, pady=5)
        num = len(self.apps)
        x, y = 4, 3             # 屏幕比例: x:y = 4:3
        addr_x, addr_y = 0, 0   # 摆放位置标记变量

        for i in range(num//7+2):
            n = x * i * y * i
            if n > num:
                break

        x = 4 * i
        y = 3 * i
        relw = 1 / ((5 / 4) * x + 1/4)  # 相对父容器的宽度
        relh = 1 / ((5 / 4) * y + 1/4)     # 相对父容器的高度

        for i, (name, app_exec, app_img) in enumerate(self.apps):

            img = Image.open(app_img)
            logo = ImageTk.PhotoImage(img.resize((80, 80)))     # 统一logo大小
            button = ttk.Button(runs_frame, image=logo, text=name, compound=tk.TOP, command=lambda cmd=app_exec: os.system(cmd), style="COMMAND, OUTLINE")

            relx = (5/4) * addr_x * relw + (1/4) * relw
            rely = (5/4) * addr_y * relh + (1/4) * relh
            button.place(anchor=NW, relheight=relh, relwidth=relw, relx=relx, rely=rely)

            if i % x == x-1:
                addr_x = 0
                addr_y += 1
            else:
                addr_x += 1
            self.res.append((button, logo))

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
