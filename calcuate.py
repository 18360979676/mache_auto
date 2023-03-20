import tkinter
import win32gui
import win32con
import win32com.client
from decimal import Decimal


# 验证输入的文本
def varileText(content):
    if content.keysym == 'Return':
        price_list = CMD.get().split(' ')
        if len(price_list) == 3:
            if price_list[2] == 'z':
                end_price = (Decimal(price_list[0]) * (Decimal(10) + Decimal(
                    '0.02') * Decimal(price_list[1])) / Decimal(10)).quantize(Decimal('1.1'))
                label_text.set("平仓价格:{}".format(
                    end_price))
                return True
            elif price_list[2] == 'd':
                end_price = (Decimal(price_list[0]) * (Decimal(10) - Decimal(
                    '0.02') * Decimal(price_list[1])) / Decimal(10)).quantize(Decimal('1.1'))
                label_text.set("平仓价格:{}".format(
                    end_price))
                return True
            else:
                return True
        return True
    return True


def get_all_hand(hwnd, mouse):
    if (win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd)):
        hwnd_map.update({hwnd: win32gui.GetWindowText(hwnd)})


if __name__ == '__main__':
    hwnd_map = {}
    # 创建主窗口
    root = tkinter.Tk()
    # 设置标题
    root.title('Liqui_price_computer')
    # 设置主窗口大小
    root.geometry('200x150+1300+200')
    # 设置图标
    root.iconbitmap(
        'resources/a686c9177f3e6709c93db127d88e883df8dcd000ff9b.ico')
    # 设置窗口背景色
    root['background'] = 'black'

    CMD = tkinter.StringVar()
    # 输入---（开仓价格、涨跌倍数、多空方向选择）
    entry_price_multiple_direction = tkinter.Entry(
        root, font=('微软雅黑', 15), relief=tkinter.SUNKEN, textvariable=CMD)
    entry_price_multiple_direction.bind('<KeyRelease>', varileText)
    entry_price_multiple_direction.pack(padx=20, pady=20)

    # 输出---（开仓价格、涨跌倍数、平仓价格）
    label_text = tkinter.StringVar()
    label = tkinter.Label(root, textvariable=label_text,
                          fg='green',
                          font=('微软雅黑', 15)
                          )
    # 显示出来
    label.pack(side='bottom')
    win32gui.EnumWindows(get_all_hand, 0)

    for h, t in hwnd_map.items():
        if t:
            if t == 'Liqui_price_computer':
                # print(h)

                # win32gui.BringWindowToTop(h)
                # shell = win32com.client.Dispatch("WScript.Shell")
                # shell.SendKeys('%')
                
                # #被其它窗口遮挡，调用后放到最前面
                # win32gui.SetForegroundWindow(h)

                # 保持当前窗口置顶
                win32gui.SetWindowPos(h, win32con.HWND_TOPMOST, 1300, 200, 220, 160, win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW)
                
    root.mainloop()
