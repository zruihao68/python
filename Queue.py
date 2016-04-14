#队列的实现
class Queue(object):
    #初始化
    def __init__(qu,size):
        qu.queue = []
        qu.size = size
        qu.head = -1    #队首指针
        qu.tail = -1   #队尾指针
    #判断是否为空
    def Empty(qu):
        if qu.head == qu.tail:
            return True
        else:
            return False
    #判卷队列是否已满
    def Full(qu):
        if qu.tail - qu.head + 1 == qu.size:
            return True
        else:
            return False
    #进
    def enQueue(qu,content):
        if qu.Full():
            print("Queue is Full!")
        else:
            qu.queue.append(content)
            qu.tail = qu.tail+1
    #出
    def outQueue(qu):
        if qu.Empty():
            print("Queue is Empty!")
        else:
            qu.head = qu.head+1
