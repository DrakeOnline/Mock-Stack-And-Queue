#-----------------------------------------------------------#
#   Title:      main.py                                     #
#   Author:     Drake G. Cummings                           #
#   Date:       January 22nd, 2021                          #
#   Purpose:    Driver file for linear data structures      #
#-----------------------------------------------------------#

from Stack import Stack
from Queue import Queue


#--------------------STACK METHODS--------------------#
testStack = Stack()
# .Push()
testStack.Push(5)
print(testStack.items)
testStack.Push(76)
print(testStack.items)

# .Pop()
print(testStack.Pop())

# .Contains()
print(testStack.Contains(5))
print(testStack.Contains(76))
print()


#--------------------QUEUE METHODS--------------------#
testQueue = Queue()
# .Append()
testQueue.Append("Dog")
testQueue.Append("Cat")
testQueue.Append("Turtle")
print(testQueue.items)

# .Pop()
print(testQueue.Pop())
print(testQueue.items)

# .Contains()
print(testQueue.Contains("Cat"))
print(testQueue.Contains("Lizard"))
print()
