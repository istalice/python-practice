name="传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_growth_factor = 1.2
growth_days =  7
money = stock_price * stock_price_growth_factor ** growth_days
# 输出
print(f"公司：{name} ，", f"股票代码:{stock_code}，", f"当前股价：{stock_price}")

#利用f "{}" 写的

   #print(f"每日增长系数是：{stock_price_growth_factor}，", f"经过{growth_days} 天的增长后，", f"股价达到了：{money}")
  # 利用%占位符写
  #print("每日增长系数是：%f，", "经过%d 天的增长后，", "股价达到了：%.2f" %) 写错了
 print("每日增长系数：%.1f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_growth_factor, growth_days,money))