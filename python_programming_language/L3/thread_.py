# -*- coding: utf-8 -*-
# @Time    : 2023/5/8 19:46
# @Author  : yanfa
# @user   : yanfa 
# @File    : thread_.py
# @remark: 线程
# import threading
#
#
# def task2():
#     print("扔第二个苹果")
#
# def task3():
#     print("扔第三个苹果")
#
# def main():
# 创建线程
#     thread1=threading.Thread(target=task2)
# 启动线程
#     thread1.start()
#     thread2=threading.Thread(target=task3)
#     thread2.start()
#     print("扔第一个苹果")
#
# if __name__ == '__main__':
#     main()
#扔第二个苹果
# 扔第三个苹果
# 扔第一个苹果
import time

#GIL (Global Interpreter Lock) 是Python解释器的一个全局锁，它是为了保证在多线程情况下Python解释器的线程安全而引入的。
# 由于GIL的存在，Python的多线程并不能真正的并行执行，而是交替执行。这是因为在同一时刻，
# 只有一个线程能够拿到GIL，拥有GIL的线程才能在CPU上执行。当该线程执行完毕后，其他线程才有机会拿到GIL并执行
# def task():
#     time.sleep(5)
#
# def main():
#     start_time=time.time()
#     # 创建线程
#     thread1=threading.Thread(target=task)
#     # 启动线程start()
#     thread1.start()
#     thread2=threading.Thread(target=task)
#     thread2.start()
#     end_time=time.time()
#     # 注意主线程与从线程是轮训执行，不加等待线程执行join()，会忽略休眠的代码
#     thread1.join()
#     thread2.join()
#     print(end_time-start_time)


"""1、多线程并行执行计算密集型任务时，GIL会导致程序性能下降，因为每个线程都要抢夺GIL，而不是真正的并行执行任务。以下是一个计算密集型任务的示例："""
# import threading

# def task():
#     s = 0
#     for i in range(100000000):
#         s += i
#
# threads = [threading.Thread(target=task) for i in range(4)]
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()

""""在上面的示例中，我们创建了4个线程来执行计算密集型任务。但是由于GIL的存在，实际上这4个线程并不会真正的并行执行，而是交替执行。因此，当使用多线程来执行计算密集型任务时，无法利用多核CPU的优势。"""

"""2、多线程并行执行I/O密集型任务时，GIL不会对性能产生太大的影响，因为线程通常会在I/O操作中阻塞，释放GIL。以下是一个I/O密集型任务的示例："""
import threading
import requests

def download(url):
    response = requests.get(url)
    print(len(response.content))

urls = [
    "https://www.google.com",
    "https://www.baidu.com",
    "https://www.github.com"
]

threads = [threading.Thread(target=download, args=(url,)) for url in urls]

for t in threads:
    t.start()

for t in threads:
    t.join()

"""在上面的示例中，我们创建了3个线程来下载三个不同的网页。由于下载任务是I/O密集型的，线程通常会在下载过程中阻塞，因此GIL不会对性能产生太大的影响。因此，当使用多线程来执行I/O密集型任务时，可以更好地利用CPU的多核优势。"""
