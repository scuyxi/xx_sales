"""
小象奶茶馆业绩蒸蒸日上，顾客赞不绝口，越来越多的顾客希望每次可以尝鲜多种口味，老板对你开发的价格结算系统功能称赞有加并且希望你能继续美化，你一边洋洋得意，一边打算将系统更新，使之更加规范有效，于是，你不辞辛苦地主动开始对系统进行模式化封装：
要求：
1、 增加每位顾客的购买品种，可多次输入奶茶编号（每次一种）和数量，并设置退出选项。
2、 将每位顾客的购买信息（奶茶品种和数量）记录在字典中，使用字典计算总消费额。
3、 顾客购物信息打印时，分别显示每种口味奶茶的编号和数量，末尾显示总金额。
4、 非会员顾客要求设置会员号及手机号，并且将会员号与手机号记录为字典形式。
5、 将每位顾客的每条购物信息记录为一个字典（每种口味一个字典，分别记录会员号、奶茶编号、购买数量），并将所有顾客的购物信息记入列表。 6、 将顾客的购物过程、购物信息打印、购物详情记录分别封装为函数。
7、 设置主函数，在主函数中调用上条所定义的函数。
"""


def all_product():
    products = {
        "原味冰奶茶": 3,
        "香蕉冰奶茶": 5,
        "草莓冰奶茶": 5,
        "蒟蒻冰奶茶": 7,
        "珍珠冰奶茶": 7}
    return products


def print_all_products(products):
    print("本店共有%d种商品在售：" % (len(products)))
    for name, price in products.items():
        print(name + (":%.2f" % price))


def sale_system():
    # 所有人购物信息
    all_shopping_info = []
    # 会员信息
    all_mem_info = []

    products = all_product()
    # 默认为新用户
    new_consumer = True
    while True:
        if new_consumer:
            # 购物车
            shopping_car = []
            shopping_info = set()
            print("欢迎光临本店")
            mem_no = input("请输入会员号：")
            mem_phone = input("请输入会员手机号")
            mem_info = {"mem_no": mem_no, "mem_phone": mem_phone}
            print_all_products(products)
        product_type = input("请输入您需要的商品种类")
        if product_type in products.keys():
            product_num = input("请输入您需要的数量")
            product_num = int(product_num)
            shopping_item = {"product_type": product_type, "product_num": product_num}
            shopping_car.append(shopping_item)
        else:
            print("暂无该商品销售")
        if_go_on = input("是否继续购物：y/n")
        if if_go_on.lower() == "y":
            new_consumer = False
            continue
        else:
            new_consumer = True
            # 结算
            coupon = 1
            if mem_info in all_mem_info:
                # 老会员可享受会员价
                coupon = 0.9
            else:
                # 将新会员加入到会员列表中
                all_mem_info.append(mem_info)
            total_price = 0
            for item in shopping_car:
                p_type = item["product_type"]
                num = item["product_num"]
                total_price += products.get(p_type, 0) * num
            total_price *= coupon

            shopping_info = {
                "mem_no": mem_no,
                "shopping_list": shopping_car,
                "total_price": total_price
            }
            all_shopping_info.append(shopping_info)
            print(shopping_info)
            print(all_shopping_info)


sale_system()