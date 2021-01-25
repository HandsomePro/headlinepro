import threading
from time import sleep


def say(name):
    sleep(5)
    print('你好！ %s' % name)


def sing(name):
    sleep(3)
    print('%s 在唱歌' % name)


threading.Thread(target=say, args=('张三',)).start()
threading.Thread(target=sing, args=('李四',)).start()
