from tkinter import *
from tkinter import ttk
import main
from main import FORGE, resarch


class RUN_STATUE(object):
    def GREEN_STATUE(self):
        num_iterations = int(entry.get())
        ocr = checkbox_var4.get()
        if checkbox_var1.get():
            for _ in range(num_iterations):
                FORGE.GREEN_STATUE_S(ocr=ocr)
        elif checkbox_var2.get():
            for _ in range(num_iterations):
                FORGE.GREEN_STATUE_M(ocr=ocr)
        elif checkbox_var3.get():
            for _ in range(num_iterations):
                FORGE.GREEN_STATUE_L(ocr=ocr)

    def BULE_STATUE(self):
        num_iterations = int(entry.get())
        ocr = checkbox_var4.get()
        if checkbox_var1.get():
            for _ in range(num_iterations):
                FORGE.BULE_STATUE_S(ocr=ocr)
        elif checkbox_var2.get():
            for _ in range(num_iterations):
                FORGE.BULE_STATUE_M(ocr=ocr)
        else:
            for _ in range(num_iterations):
                FORGE.BULE_STATUE_L(ocr=ocr)

    def RED_STATUE(self):
        num_iterations = int(entry.get())
        ocr = checkbox_var4.get()
        if checkbox_var1.get():
            for _ in range(num_iterations):
                FORGE.RED_STATUE_S(ocr=ocr)
        elif checkbox_var2.get():
            for _ in range(num_iterations):
                FORGE.RED_STATUE_M(ocr=ocr)
        else:
            for _ in range(num_iterations):
                FORGE.RED_STATUE_L(ocr=ocr)

    def PURPLE_STATUE(self):
        num_iterations = int(entry.get())
        ocr = checkbox_var4.get()
        if checkbox_var1.get():
            for _ in range(num_iterations):
                FORGE.PURPLE_STATUE_S(ocr=ocr)
        elif checkbox_var2.get():
            for _ in range(num_iterations):
                FORGE.PURPLE_STATUE_M(ocr=ocr)
        else:
            for _ in range(num_iterations):
                FORGE.PURPLE_STATUE_L(ocr=ocr)


class RUN_DIAOKEJI(object):
    def GREEN_DIAOKEJI(self):
        num_iterations = int(entry.get())
        for _ in range(num_iterations):
            resarch.GREEN_DIAOKEJI()

    def BULE_DIAOKEJI(self):
        num_iterations = int(entry.get())
        for _ in range(num_iterations):
            resarch.BULE_DIAOKEJI()

    def RED_DIAOKEJI(self):
        num_iterations = int(entry.get())
        for _ in range(num_iterations):
            resarch.RED_DIAOKEJI()

    def PURPLE_DIAOKEJI(self):
        num_iterations = int(entry.get())
        for _ in range(num_iterations):
            resarch.PURPLE_DIAOKEJI()

root = Tk()
root.title("水晶序列预测")
root.geometry("430x250")

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="水晶序列预测").grid(column=0, row=0, pady=10)

# 创建输入框
ttk.Label(frm, text="次数:").grid(column=0, row=1, pady=5)
entry = ttk.Entry(frm)
entry.grid(column=1, row=1)

# 创建勾选框变量
checkbox_var1 = BooleanVar()
checkbox_var2 = BooleanVar()
checkbox_var3 = BooleanVar()
checkbox_var4 = BooleanVar()

# 创建勾选框
checkbox = ttk.Checkbutton(frm, text="小型水晶", variable=checkbox_var1)
checkbox.grid(column=1, row=2, pady=5, columnspan=2)
checkbox = ttk.Checkbutton(frm, text="中型水晶", variable=checkbox_var2)
checkbox.grid(column=1, row=3, pady=5, columnspan=2)
checkbox = ttk.Checkbutton(frm, text="大型水晶", variable=checkbox_var3)
checkbox.grid(column=1, row=4, pady=5, columnspan=2)
checkbox = ttk.Checkbutton(frm, text="写入excel", variable=checkbox_var4)
checkbox.grid(column=1, row=5, pady=5, columnspan=2)

RUN_STATUE = RUN_STATUE()
RUN_DIAOKEJI = RUN_DIAOKEJI()

# 创建按钮
ttk.Button(frm, text="绿水晶", command=lambda: RUN_STATUE.GREEN_STATUE()).grid(column=0, row=2, pady=5)
ttk.Button(frm, text="蓝水晶", command=lambda: RUN_STATUE.BULE_STATUE()).grid(column=0, row=3, pady=5)
ttk.Button(frm, text="红水晶", command=lambda: RUN_STATUE.RED_STATUE()).grid(column=0, row=4, pady=5)
ttk.Button(frm, text="紫水晶", command=lambda: RUN_STATUE.PURPLE_STATUE()).grid(column=0, row=5, pady=5)
ttk.Button(frm, text="绿雕刻", command=lambda: RUN_DIAOKEJI.GREEN_DIAOKEJI()).grid(column=3, row=2, pady=5)
ttk.Button(frm, text="蓝雕刻", command=lambda: RUN_DIAOKEJI.BULE_DIAOKEJI()).grid(column=3, row=3, pady=5)
ttk.Button(frm, text="红雕刻", command=lambda: RUN_DIAOKEJI.RED_DIAOKEJI()).grid(column=3, row=4, pady=5)
ttk.Button(frm, text="紫雕刻", command=lambda: RUN_DIAOKEJI.PURPLE_DIAOKEJI()).grid(column=3, row=5, pady=5)

# 创建结果标签
label_result = ttk.Label(frm, text="")
label_result.grid(column=0, row=6, columnspan=2, pady=10)

if __name__ == '__main__':
    root.mainloop()