import subprocess
import ttkbootstrap as ttk


class OtherToolsWindow:

    def __init__(self, frame: ttk.Frame, config: list, type_str: str):

        num = len(config)
        # 整理工具摆放位置
        x, y = 4, 3     # 屏幕比例: x : y = 4 : 3
        h, w = 1, 4     # 按钮比例: h : w = 1 : 8
        cah = h
        caw = w / 4
        numx = x * h    # 4  列
        numy = y * w    # 24 行
        addr_x, addr_y = 0, 0  # 摆放位置标记变量

        # 确定按钮数量，几行几列
        i = num // (numx * numy) + 1 if num % (numx * numy) != 0 else num // (numx * numy)
        numx = numx * i
        numy = numy * i

        relw = w / (numx * w + (numx + 1) * caw)    # 相对父容器的宽度
        relh = h / (numy * h + (numy + 1) * cah)    # 相对父容器的高度
        relcaw = caw / (numx * w + (numx + 1) * caw)  # 相对父容器的间隙宽度
        relcah = cah / (numy * h + (numy + 1) * cah)  # 相对父容器的间隙高度

        for i, v in enumerate(config):

            relx = (relw + relcaw) * addr_x + relcaw
            rely = (relh + relcah) * addr_y + relcah

            app_exec = f"res\\other_tools\\{type_str}\\{v}\\start.bat"
            button = ttk.Button(frame, padding=5, text=v, command=lambda cmd=app_exec: subprocess.run(cmd))

            button.place(relheight=relh, relwidth=relw, relx=relx, rely=rely,)
            if i % x == x - 1:
                addr_x = 0
                addr_y += 1
            else:
                addr_x += 1