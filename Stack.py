# -*- coding: utf-8 -*-
#栈的实现
class Stack(object):
    #初始化栈的大小
    def __init__(st,size):
        st.stack = []
        st.size = size
        st.top = -1

    #入栈操作，判断是否为空，栈顶的位置加一
    def push(st,content):
        if st.Full():
            print("Stack is Full!")
        else:
            st.stack.append(content)
            st.top = st.top+1

    #判断是否已满
    def Full(st):
        if st.top == st.size:
            return True
        else:
            return False

    #判断是否为空
    def Empty(st):
        if st.top == -1:
            return True
        else:
            return False

    #出栈
    def out(st):
        if st.Empty():
            print("Stack is Empty!")
        else:
            st.top = st.top-1
