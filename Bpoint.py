#链表实现（单向链表）
class jd(object):
    #节点初始化
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist(object):
    def __init__(self,jd2):
        self.head = jd2
        self.head.next = None
        self.tail = self.head

    #添加节点
    def add(self,jd2):
        self.tail.next = jd2
        self.tail = self.tail.next

    #显示view
    def view(self):
        jd2 = self.head
        linkstr = ""
        while jd2 is not None:
            if jd2.next is not None:
                linkstr = linkstr+str(jd2.data)+"-->"
            else:
                linkstr+= str(jd2.data)
            jd2 = jd2.next
        print(linkstr)
