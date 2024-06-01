import random
import threading
import time


# 线程类似于同时执行多个不同程序，多线程运行有如下优点：
# z使用线程可以把占据长时间的程序中的任务放到后台去处理。
# z程序的运行速度可能加快z在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。
# 在这种情况下我们可以释放一些珍贵的资源如内存占用等等。
# z每个线程都有自己的一组CPU寄存器，称为线程的上下文，该上下文反映了线程上次运行该线程的CPU寄存器的状态。
# z在其他线程正在运行时，线程可以暂时搁置（也称为睡眠），这就是线程的退让

# 从结果看到，主线程启动子线程r后结束，但是子线程并未结束，继续显示完reading4后才结束。
# 其中，r.setDaemon(False)设置线程r为后台线程，后台线程不因主线程的结束而结束。
# 如何设置r.setDaemon(True)，使r为前台线程。
def reading():
    for i in range(5):
        print("reading", i)
        time.sleep(random.randint(1, 2))


def test():
    r = threading.Thread(target=reading)
    r.daemon = True
    r.start()
    r.join()
    print("test end")


t = threading.Thread(target=test)
# t.setDaemon(False)
t.daemon = False
t.start()
t.join()
print("Main Thread End")
