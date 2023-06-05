"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time
from datetime import datetime


class Coffee:

    def __init__(self, name: str, price: int, ingredient: str):
        self.name = name
        self.price = price
        self.ingredient = ingredient

    def __str__(self):
        return f'{self.name}({self.price}元): {self.ingredient}'

class Latte(Coffee):

    def __init__(self):
        super().__init__('拿铁', 20, '浓缩咖啡，牛奶，糖')


class Americano(Coffee):

    def __init__(self):
        super().__init__('美式', 15, '浓缩咖啡')


class CoffeeMachine:

    def __init__(self):
        # 组合模式
        self.products = [Latte(), Americano()]
        self.records = []

    def display(self):
        """展示咖啡"""
        print('------ 展示咖啡 ------')
        for coffee in self.products:
            print(coffee)

    def select_coffee(self) -> Coffee:
        """选择咖啡"""
        print('------ 选择咖啡 ------')
        while True:
            selected = input('请输入数字选择咖啡 0：拿铁，1：美式咖啡')

            if selected in ('0', '1'):
                return self.products[int(selected)]
            else:
                print('输入不合法，请重新选择可选的咖啡。')
                continue

    def input_money(self, coffee: Coffee) -> int:
        """输入钱币"""
        print('------ 输入钱币 ------')
        while True:
            money = input(f'请投入{coffee.price}元')
            if int(money) < coffee.price:
                print('金额不够，请重新投币。原金额已经退回')
                continue
            else:
                return int(money)

    def make_coffee(self, coffee: Coffee, money: int):
        """制作咖啡"""
        print('------ 制作咖啡 ------')
        print('咖啡制作中，请稍候...')
        time.sleep(3)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        record = f'{now} 订单：{coffee.name}咖啡️，支付{money}元，找零{money - coffee.price}元'

        self.records.append(record)


    def print_records(self):
        """打印记录"""
        print('------ 打印记录 ------')
        for rec in self.records:
            print(rec)



if __name__ == '__main__':
    machine = CoffeeMachine()

    while True:
        # 展示咖啡
        machine.display()

        # 选择咖啡
        selected_coffee = machine.select_coffee()

        # 投入钱币
        inp_money = machine.input_money(selected_coffee)

        # 制作咖啡
        machine.make_coffee(selected_coffee, inp_money)

        # 询问是否继续
        answer = input('是否继续购买？Y:继续，N:不继续')
        if answer == 'Y':
            continue
        else:
            break

    # 打印记录
    machine.print_records()
