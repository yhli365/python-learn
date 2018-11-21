"""
案例描述：设计一个汇率换算器程序，其功能是将外币换算成人民币，或者相反。
为了使程序简单，目前只考虑一种外币（如：美元）
作者：梁XX
功能：汇率兑换
版本：1.0
日期：01/08/2017
"""

# 汇率
USD_VS_RMB = 6.77

# 人民币的输入
rmb_str_value = input('请输入人民币(CNY)金额：')

# 将字符串转换为数字
rmb_value = eval(rmb_str_value)

# 汇率计算
usd_value = rmb_value / USD_VS_RMB

# 输出结果
print('美元(USD)金额是：', usd_value)

