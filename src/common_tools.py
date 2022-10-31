import subprocess
import ttkbootstrap as ttk
from PIL import Image, ImageTk


class RunsWindow:
    runc_frame: ttk.Frame
    res = []

    def __init__(self, root: ttk.Frame, apps: list):

        self.runc_frame = ttk.Frame(root, padding=10, borderwidth=1, relief='ridge')
        self.runc_frame.pack(fill=ttk.BOTH, expand=ttk.YES, padx=5, pady=5)
        num = len(apps)
        # 整理工具摆放位置
        x, y = 4, 3  # 屏幕比例: x:y = 4:3
        addr_x, addr_y = 0, 0  # 摆放位置标记变量

        for i in range(num // 7 + 2):
            n = x * i * y * i
            if n > num:
                break

        x = 4 * i
        y = 3 * i
        relw = 1 / ((5 / 4) * x + 1 / 4)  # 相对父容器的宽度
        relh = 1 / ((5 / 4) * y + 1 / 4)  # 相对父容器的高度

        for i, (name, app_exec, app_img) in enumerate(apps):

            img = Image.open(app_img)
            logo = ImageTk.PhotoImage(img.resize((80, 80)))  # 统一logo大小
            button = ttk.Button(self.runc_frame, image=logo, text=name, compound=ttk.TOP,
                                command=lambda cmd=app_exec: subprocess.run(cmd), style="COMMAND, OUTLINE")

            relx = (5 / 4) * addr_x * relw + (1 / 4) * relw
            rely = (5 / 4) * addr_y * relh + (1 / 4) * relh
            button.place(anchor=ttk.NW, relheight=relh, relwidth=relw, relx=relx, rely=rely)

            if i % x == x - 1:
                addr_x = 0
                addr_y += 1
            else:
                addr_x += 1

            self.res.append((button, logo))
