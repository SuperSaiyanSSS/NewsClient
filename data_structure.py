# coding=utf-8
from __future__ import unicode_literals, print_function
import gc
import Queue
from PyQt4 import QtCore, QtGui


class TwoWayNode(object):
    def __init__(self, data=0, pre=None, next=None, ans=None):
        self.data = data
        self.pre = pre
        self.next = next
        self.ans = ans


class TwoWayLinkedList(object):
    """
    存储上一条-下一条的内容
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.tail = self.head

    def getLength(self):
        p = self.head
        i = 0
        while(p!=None):
            i = i+1
            p = p.next
        return i

    def insert(self, i, newdata):
        if(i-1>self.getLength()):
            raise IndexError
        newNode = TwoWayNode(newdata)
        j = 1
        p = self.head
        # 三种特殊情况：链表为空，插入最后一个，插入第一个
        if(self.getLength()==0):
            if(i!=1):
                raise IndexError, '链表为空，只能插到第一个'
            else:
                self.head = newNode
                self.tail = newNode
                return 0
        if(self.getLength()==i-1):
            self.append(newdata)
            return 0
        if(i==1):
            self.head = newNode
            p.pre = newNode
            newNode.next = p
            return 0
        while(j<i-1):
            p = p.next
            j = j+1
        p.next.pre = newNode
        newNode.next = p.next
        p.next = newNode
        newNode.pre = p
        if(i==self.getLength()):
            p.tail = newNode
        return 0

    def append(self, newdata, newans=None):
        newNode = TwoWayNode(newdata, ans=newans)
        if(self.getLength()!=0):
            self.tail.next = newNode
            newNode.pre = self.tail
            self.tail = newNode
            return 0
        else:
            self.head = newNode
            self.tail = newNode
            return 0

    def getLastValue(self):
        return self.tail.data

    def getValue(self, i):
        if(i > self.getLength()):
            raise IndexError
        j = 1
        p = self.head
        while(j<i):
            j = j+1
            p = p.next
        return p.data

    def destroy(self):
        del self
        gc.collect()


class Node(object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.tail = self.head

    def getLength(self):
        i = 0
        p = self.head
        while(p!=None):
            p = p.next
            i = i+1
        return i

    def insert(self, i, data):
        newNode = Node(data)
        j = 1
        if(i-1>self.getLength()):
            raise IndexError, '插入的节点位置超过了链表！'
        p = self.head
        if(i==self.getLength()+1):
            self.tail = newNode
        if(i==1):
            self.head = newNode
            newNode.next = p
            return 0
        while(j<i-1):
            p = p.next
            j = j+1
        newNode.next = p.next
        p.next = newNode
        return 0

    def append(self, data):
        newNode = Node(data)
        if(self.getLength()!=0):
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode
        return 0

    def getLastValue(self):
        return self.tail.data

    def getValue(self, i):
        j = 1
        if(i>self.getLength()):
            raise IndexError, '要找的位置超过了链表长度！'
        p = self.head
        while(j<i):
            p = p.next
            j = j+1
        return p.data

    def destroy(self):
        del self
        gc.collect()


class LinkedQueue(object):
    """
    多线程时的任务队列
    """
    def __init__(self):
        self.head = self.tail = Node()
        self.number = 0

    def enqueue(self, newnode):
        self.tail.data = newnode
        self.tail.next = Node()
        self.tail = self.tail.next
        if(self.getLength()==0):
            self.head.next = self.tail
        self.number = self.number+1

    def dequeue(self):
        if(self.tail==self.head):
            raise IndexError, '队列为空!'
        p = self.head
        self.head = self.head.next
        self.number = self.number -1
        return p.data

    def getLength(self):
        return self.number

    def isEmpty(self):
        if(self.getLength()==0):
            return True
        return False


class GeneralNode(object):
    """
    存储观海听涛的帖子内容
    子链表有tid、标题、时间、作者、正文、回帖等信息
    """
    def __init__(self, data=0, pre=None, next=None, brother=None):
        self.data = data
        self.pre = pre
        self.next = next
        self.brother = brother


class GeneralLinkedList(TwoWayLinkedList):
    def __init__(self):
        super(GeneralLinkedList, self).__init__()

    def getBrother(self, node):
        return node.brother


class BSTreeNode(object):
    def __init__(self, data=0, brother=None, son=None):
        self.data = data
        self.brother = brother
        self.son = son


class BSTree(object):
    """
    用于存放本地新闻链接
    按照省份-市区-类型-具体链接进行存储
    """
    def __init__(self):
        self.root = None
        self.createTree()
        self.province = ""

    def createTree(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        queue = LinkedQueue()
        a = BSTreeNode('中国')
        queue.enqueue(a)
        self.root = a
        p0 = self.root
        f = open('bstree.txt', 'r')
        while not queue.isEmpty():
            p0 = queue.dequeue()
            newson_list = f.readline().strip()
            if not newson_list:
                print(queue.getLength())
                break
            newson_list = newson_list.split("!!!")
            if newson_list[-1]=="":
                del newson_list[-1]
            if(newson_list[0][0]!='#'):
                p1 = BSTreeNode(newson_list[0])
                p0.son = p1
                for i in range(len(newson_list)-1):
                    p1.brother = BSTreeNode(newson_list[i+1])
                    queue.enqueue(p1)
                    p1 = p1.brother
                p1.brother = None
                queue.enqueue(p1)
                if p1.data=="":
                    print(111111111)
            else:
              #  print(p0.data)
                p1 = BSTreeNode(newson_list[0][1:])
                p0.son = p1
                for i in range(len(newson_list)-1):
                    p1.brother = BSTreeNode(newson_list[i+1])
                    p1.son = None
                    p1 = p1.brother
                p1.brother = None
                p1.son = None

    def findProvince(self):
        province_list = []
        p = self.root.son
        while p.brother is not None:
            province_list.append(p.data)
            p = p.brother
        return province_list

    def findCity(self, province):
        city_list = []
        self.province = province
        p = self.root.son
        while p is not None:
            if p.data == province:
                break
            p = p.brother
        p = p.son
        while p is not None:
            city_list.append(p.data)
            p = p.brother
        return city_list

    def findWebsite(self, city):
        website_list = []
        p = self.root.son
        while p is not None:
            if p.data == self.province:
                p = p.son
                while p is not None:
                    if p.data == city:
                        p = p.son
                        while p is not None:
                            website_list.append(p.data)
                            p = p.brother
                        return website_list
                    p = p.brother
            p = p.brother


class HeapNode(object):
    def __init__(self, time, text):
        self.time = time
        self.text = text


class MaxHeap(object):
    """
    最大堆
    用于存放新闻，按时间顺序
    """
    def __init__(self, capacity, Elements):
        self.capacity = capacity
        self.size = len(Elements)
        self.Elements = Elements
        self.Elements.insert(0, HeapNode('999999999999999999', u"无"))

    def isFull(self):
        if self.size ==self.capacity:
            return True
        return False

    def insert(self, newnode):
        if self.isFull():
            print("最大堆已满")
            return False
        self.size = self.size + 1
        i = self.size
        # 将新结点插到最后 比较其和其父结点大小 并上滤
        while int(self.Elements[i/2].time) < int(newnode.time):
            self.Elements[i] = self.Elements[i/2]
            i = i/2
        self.Elements[i] = newnode
        return True

    def isEmpty(self):
        if self.size==0:
            return True
        return False

    def deleteMax(self):
        if self.isEmpty():
            print("最大堆已空")
            return False
        # 取出第一个值（最大值）
        maxnode = self.Elements[1]
        self.size = self.size -1
        # 由于size减少一，那么自然想到减去最后一个值
        # 将最后一个值放在第一个值位置上
        tempnode = self.Elements[self.size]
        parent = 1
        # 当有孩子结点时
        while parent*2 <= self.size:
            # 左孩子结点是父结点位置的２倍
            child = parent*2
            # 当有右孩子且左孩子小于右孩子时，取右孩子进行比较
            if child <self.size and int(self.Elements[child].time) < int(self.Elements[child+1].time):
                child = child + 1
            # 当temp值小于右孩子，则交换位置
            if int(tempnode.time) >= int(self.Elements[child].time):
                break
            else:
                self.Elements[parent] = self.Elements[child]
                parent = child
        # 找到了合适位置
        self.Elements[parent] = tempnode
        return maxnode

    # 下滤：将Elements[]中以Elements[p]为根的子堆调整为最大堆
    # 和删除类似，只不过指定了根结点的位置
    def percDown(self, p):
        # 取出该子堆的根结点存放的值
        print(u"现在的父亲结点是第", str(p), u"个")
        tempnode = self.Elements[p]
        parent = p
        while parent*2 <=self.size:
            child = parent*2
            if child!=self.size and int(self.Elements[child].time) < int(self.Elements[child+1].time):
                child = child + 1
            if int(tempnode.time) >= int(self.Elements[child].time):
                break
            else:
                self.Elements[parent] = self.Elements[child]
                parent = child
        self.Elements[parent] = tempnode

    # 调整Elements[]中的元素 使其满足最大堆的有序性
    # 这里假设所有self.size个元素已经存在Elements[]中
    def buildHeap(self):
        # 从最后一个结点的父节点开始， 到根节点1
        i = self.size/2
        while i > 0:
            self.percDown(i)
            i = i - 1

    def check(self):
        a = self.size
        while a>0:
            print(self.Elements[a].time)
            a -= 1
        print(self.Elements[0].time)


if __name__ == "__main__":
    a = BSTree()
    a.createTree()
    print(111111)
    print(a.root.son.son.data)

    # a = TwoWayLinkedList()
    # print(a.getLength())
    # a.insert(1,-2)
    # print(a.getLength())
    # print(a.getLastValue())
    # print(a.getValue(1))
    # a.insert(1,100)
    # a.insert(3,400)
    # print(a.getValue(3))
    # a.destroy()

    print('ddddddddddddddddd')
    b = LinkedList()
    # b.initList()
    print(b.getLength())
    b.append(200)
    print(b.getLength())
    print(b.getLastValue())
    b.insert(1,50)
    b.insert(3,150)
    print(b.getLastValue())
    print(b.getValue(3))
    print(b.getLastValue())
    print(b)