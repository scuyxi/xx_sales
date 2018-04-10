"""
    项目名称：小象奶茶馆售卖系统
"""
buy_infos = []
mem_list = []
while True:
    buy_info = []
    print("Welcome to our 奶茶店！")
    print("本店有以下5个种类可供选择：\n"
          "1)原味冰奶茶 3元\t 2)香蕉冰奶茶 5元\n"
          "3)草莓冰奶茶 5元\t 4)蒟蒻冰奶茶 7元\n"
          "5)珍珠冰奶茶 7元")
    tt = input("请选择您需要的种类（1~5）:")
    tt = int(tt)
    if (tt < 1) or (tt > 5):
        print("小店只卖以上5种奶茶，新品种敬请期待")
        continue
    else:
        num = input("请输入您需要购买的数量")
        num = int(num)
        mem = input("请输入您的手机号：如是会员，可享受会员价，若不是，则注册为会员，下册享受会员价")
        if tt == 1:
            total = num * 3
            ss = '原味冰奶茶'
        elif tt == 2:
            total = num * 5
            ss = '香蕉冰奶茶'
        elif tt == 3:
            total = num * 5
            ss = '草莓冰奶茶'
        elif tt == 4:
            total = num * 7
            ss = '蒟蒻冰奶茶'
        else:
            total = num * 7
            ss = '珍珠冰奶茶'
        buy_product = "%d杯%s" % (num, ss)
        buy_info.append(buy_product)
        print("您购买的是: %d杯%s" % (num, ss))
        print("总价：{:.2f}".format(float(total)))
        total_price = "总价：{:.2f}".format(float(total))
        buy_info.append(total_price)
        mem_info = '会员' + mem
        buy_info.insert(0, mem_info)
        if mem in mem_list:
            total = 0.9 * total
            mem_price = "会员价: %.2f" % total
            buy_info.append(mem_price)
            print("会员价: %.2f" % total)
        else:
            mem_list.extend([mem])
        act_price = "应付价：{:.2f}".format(float(total))
        buy_info.append(act_price)
        print("应付价：{:.2f}".format(float(total)))
    buy_infos.append(buy_info)
    if len(buy_infos) == 2:
        print("今日已闭店，欢迎明天光临")
        break

print('今日销售信息如下：')
for info in buy_infos:
    for item in info:
        print(item, end=',')
    print("")
