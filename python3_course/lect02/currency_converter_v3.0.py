"""
案例描述：设计一个汇率换算器程序，其功能是将外币换算成人民币，或者相反。
为了使程序简单，目前只考虑一种外币（如：美元）
作者：梁XX
功能：汇率兑换
版本：3.0
日期：01/08/2017
2.0 增加功能：根据输入判断是人民币还是美元，进行相应的转换计算。
3.0 增加功能：程序可以一直运行，直到用户选择退出
"""

# 汇率
USD_VS_RMB = 6.77

# 带单位的货币输入
currency_str_value = input('请输入带单位的货币金额：')

# 获取货币单位
unit = currency_str_value[-3:]

if unit == 'CNY':
    # 输入的是人民币
    rmb_str_value = currency_str_value[:-3]
    # 将字符串转换为数字
    rmb_value = eval(rmb_str_value)
    # 汇率计算
    usd_value = rmb_value / USD_VS_RMB

    # 输出结果
    print('美元(USD)金额是：', usd_value)

elif unit == 'USD':
    # 输入的是美元
    usd_str_value = currency_str_value[:-3]
    # 将字符串转换为数字
    usd_value = eval(usd_str_value)
    # 汇率计算
    rmb_value = usd_value * USD_VS_RMB

    # 输出结果
    print('人民币(CNY)金额是：', rmb_value)

else:
    # 其他情况
    print('目前版本尚不支持该种货币！')
