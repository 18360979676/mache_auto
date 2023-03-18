import tkinter
from decimal import Decimal


# 验证输入的文本
def varileText(content):
    price_list = content.split(' ')
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


if __name__ == '__main__':
    # 创建主窗口
    root = tkinter.Tk()
    # 设置标题
    root.title('平仓价格计算器')
    # 设置主窗口大小
    root.geometry('200x150+1300+200')
    # 设置图标
    root.iconbitmap(
        './resources/a686c9177f3e6709c93db127d88e883df8dcd000ff9b.ico')
    # 设置窗口背景色
    root['background'] = 'gray'

    CMD = root.register(varileText)
    # 输入---（开仓价格、涨跌倍数、多空方向选择）
    entry_price_multiple_direction = tkinter.Entry(
        root, validate="key", validatecommand=(CMD, '%P'), font=('微软雅黑', 15), relief=tkinter.SUNKEN)
    entry_price_multiple_direction.pack(padx=20, pady=20)

    # 输出---（开仓价格、涨跌倍数、平仓价格）
    label_text = tkinter.StringVar()
    label = tkinter.Label(root, textvariable=label_text,
                          fg='green',
                          font=('微软雅黑', 15)
                          )
    # 显示出来
    label.pack(side='bottom')

    root.mainloop()
