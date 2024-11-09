######LAB 1

# class Stack:
#     def __init__(self):
#         self.__stk = []
#
#     def push(self, val):
#         self.__stk.append(val)
#
#     def pop(self):
#         val = self.__stk[-1]
#         del self.__stk[-1]
#         return val
#
#
# class CountingStack(Stack):
#     def __init__(self):
#         super().__init__()
#         self.__counter=0
#
#     def get_counter(self):
#         return self.__counter
#
#     def pop(self):
#         val = super().pop()
#         # Increment the counter
#         self.__counter += 1
#         # Return the popped value
#         return val
#
# stk = CountingStack()
# for i in range(100):
#     stk.push(i)
#     stk.pop()
# print(stk.get_counter())

##############ALL ABOUT STACK

# stack=[]
# def push(val):
#     stack.append(val)
#
# def pop():
#     val=stack[-1]
#     del stack[-1]
#     return val
#
# push(3)
# push(4)
# push(5)
# print(pop())
# print(pop())
# print(pop())

###########LAB 3

class  QueueError(Exception):
    # def __init__(self):
    print("Error:", "The Queue is empty")
class Queue():
    def __init__(self):
        self.queuelist=[]
    def push(self,element):
        self.queuelist.append(element)

    def get (self):
        if len(self.queuelist) >0:
            return self.queuelist.pop(0)

        else:
            raise QueueError

class subQueue(Queue):

    def chech_for_empty(self):
        return len(self.queuelist)==0

que = subQueue()
que.push(1)
que.push("dog")
que.push(False)

for i in range(6):
    if not que.chech_for_empty():
        print(que.get())
    else:
        print("Queue empty")


################MORE THAN 1 STAKE
# class Stack:
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#
# little_stack = Stack()
# another_stack = Stack()
# funny_stack = Stack()
#
# little_stack.push(1)
# another_stack.push(little_stack.pop() + 1)
# funny_stack.push(another_stack.pop() - 2)
#
# print(funny_stack.pop())

###################

# class Stack:
#     def __init__(self):
#         self.__stk = []
#
#     def push(self, val):
#         self.__stk.append(val)
#
#     def pop(self):
#         val = self.__stk[-1]
#         del self.__stk[-1]
#         return val
#
#
# class CountingStack(Stack):
#     def __init__(self):
#         super().__init__()
#         self.__counter = 0
#
#     def get_counter(self):
#         return self.__counter
#
#     def pop(self):
#         self.__counter += 1
#
#
# stk = CountingStack()
# for i in range(100):
#     stk.push(i)
#     stk.pop()
# print(stk.get_counter())

