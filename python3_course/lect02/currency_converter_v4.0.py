"""
案例描述：设计一个汇率换算器程序，其功能是将外币换算成人民币，或者相反。
为了使程序简单，目前只考虑一种外币（如：美元）
作者：梁XX
功能：汇率兑换
版本：4.0
日期：01/08/2017
2.0 增加功能：根据输入判断是人民币还是美元，进行相应的转换计算。
3.0 增加功能：程序可以一直运行，直到用户选择退出
4.0 增加功能：将汇率兑换功能封装到函数中
"""


def convert_currency(im, er):
    """
    汇率兑换函数
    :param im: 金额
    :param er: 汇率
    :return:
    """
    # pass
    out = im * er
    return out


# 汇率
USD_VS_RMB = 6.77

# 带单位的货币输入
currency_str_value = input('请输入带单位的货币金额：')

# 获取货币单位
unit = currency_str_value[-3:]

if unit == 'CNY':
    exchange_rate = 1 / USD_VS_RMB

elif unit == 'USD':
    exchange_rate = USD_VS_RMB

else:
    exchange_rate = -1

if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])
    # 调用函数
    out_money = convert_currency(in_money, exchange_rate)
    print('兑换后的金额：', out_money)
else:
    print('不支持该种货币！')
