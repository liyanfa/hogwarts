# -*- coding: utf-8 -*-
# @Time    : 2023/4/22 16:43
# @Author  : yanfali
# @File    : coffe.py
# @Software: PyCharm

"""请设计一个自助咖啡机的人机交互系统，通过投币购买咖啡，需要实现以下功能：

咖啡机展示两种可选咖啡：拿铁咖啡和美式咖啡。格式如“拿铁(20元): 浓缩咖啡，牛奶，糖”
能够选择任意一种咖啡，并投入足够的钱币（金额不够时需要重新投币）。
咖啡机制作咖啡，并且记录本次交易记录（格式如“2023-03-24 16:24:49 订单：美式咖啡️，支付20元，找零5元”）。
咖啡机询问用户是否继续购买咖啡。如果继续，则从展示咖啡开始新流程。
如果用户不继续购买，咖啡机打印所有交易记录。"""
import datetime


class Coffe:
    # 类属性
    sku_price_01 = 20
    sku_price_02 = 15

    # 静态方法
    @staticmethod
    def now():
        """处理时间"""
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def show(self):
        """展示咖啡"""
        print("------ 展示咖啡 ------")
        print(f"拿铁({self.sku_price_01}元): 浓缩咖啡，牛奶，糖")
        print(f"美式({self.sku_price_02}元): 浓缩咖啡")

    def choose(self):
        """选择咖啡"""
        print("------ 选择咖啡 ------")
        print(f"请输入数字 选择咖啡 0：拿铁，1：美式咖啡")
        num = int(input())
        type = ""
        while True:
            if num == 0:
                print("你选择规格-拿铁")
                type = "拿铁咖啡"
                break
            elif num == 1:
                print("你选择规格-美式咖啡")
                type = "美式咖啡"
                break
            else:
                print(f"当前选择数字错误，请重新选择")
                num = int(input())
                continue
        return num, type

    def pay(self, num):
        """投入钱币"""
        more = 0
        if num == 0:
            print("请投入20元")
            money = int(input())
            if money > self.sku_price_01:
                more = money - self.sku_price_01
                print(f"拿铁咖啡单价{self.sku_price_01}元，你投入{money}元，找零{more}元")
            elif money == self.sku_price_01:
                print(f"拿铁咖啡单价{self.sku_price_01}元，你投入{money}元，无需找零")
            elif money < self.sku_price_01:
                more = self.sku_price_01 - money
                print(f"拿铁咖啡单价{self.sku_price_01}元，你投入{money}元，还需投入{more}元")
            else:
                print("投入正确的金钱")
        elif num == 1:
            print("请投入15元")
            money = int(input())
            if money > self.sku_price_02:
                more = money - self.sku_price_02
                print(f"拿铁咖啡单价{self.sku_price_02}元，你投入{money}元，找零{more}元")
            elif money == self.sku_price_02:
                print(f"拿铁咖啡单价{self.sku_price_02}元，你投入{money}元，无需找零")
            elif money < self.sku_price_02:
                more = self.sku_price_02 - money
                print(f"拿铁咖啡单价{self.sku_price_02}元，你投入{money}元，还需投入{more}元")
            else:
                print("投入正确的金钱")
        else:
            money = 0
            print("选择咖啡类型错误，请检查")
        return [more, money]

    def puchase_record(self, pay_time, type, money, more):
        """打印购买记录"""
        print(f"{pay_time} 订单：{type}，支付{money}元，找零{more}元")

    def make(self, type):
        """制作咖啡"""
        print("------ 制作咖啡 ------")
        print(f"{type} ☕制作完成")

    def main(self):
        """主函数"""
        # 定义一个记录列表收集购买记录
        record = []

        # 第一次进入介绍页面
        self.show()

        # 首次选择页面
        choose_param = self.choose()
        type = choose_param[1]

        # 首次进入下单页面
        pay_param = self.pay(choose_param[0])
        more = pay_param[0]
        money = pay_param[1]
        record.append([self.now(), type, money, more])

        # 首次制作页面
        self.make(type)

        print("\n是否继续购买？Y：是，N：否")
        # 循环购买
        while True:
            #  输入是否继续购买的标识
            tag = input()
            if tag == "N":
                # 循环打印购买记录
                print("------ 购买流水 ------")
                for r in record:
                    self.puchase_record(r[0], r[1], r[2], r[3])
                print("感谢您的使用，我们下次再见")
            elif tag == "Y":
                # 重新进入制作页面
                self.show()
                # 重新进入选择页面
                choose_param = self.choose()
                type = choose_param[1]
                # 重新进入下单页面
                pay_param = self.pay(choose_param[0])
                # 重新进入制作页面
                more = pay_param[0]
                money = pay_param[1]
                self.make(type)
                print("\n是否继续购买？Y：是，N：否")
                # 记录购买记录
                r = [self.now(), type, money, more]
                record.append(r)
            else:
                print(f"请输入Y/N,你输入的是{tag}")

if __name__ == '__main__':
    c = Coffe()
    c.main()
