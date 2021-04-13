# ----------------------------------------------------------#
#   Title:      main.py                                     #
#   Author:     Drake G. Cummings                           #
#   Date:       January 22nd, 2021                          #
#   Purpose:    Driver file for linear data structures      #
# ----------------------------------------------------------#

from Stack import Stack
from Queue import Queue
from Carmen import Carmen


# -------------------STACK METHODS------------------- #
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


# -------------------QUEUE METHODS------------------- #
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


# -------------------QUEUE METHODS------------------- #
testCarmen = Carmen()

# Test of 10
tens = []
tests = 10
tens.append(testCarmen.TestComplexity(tests))
tens.append(testCarmen.TestComplexity(tests))
tens.append(testCarmen.TestComplexity(tests))
tensAverage = sum(tens)/len(tens)
print(f"Average for 10 elements: {tensAverage} seconds")
print("")

# Test of 100
hundreds = []
tests = 100
hundreds.append(testCarmen.TestComplexity(tests))
hundreds.append(testCarmen.TestComplexity(tests))
hundreds.append(testCarmen.TestComplexity(tests))
hundredsAverage = sum(hundreds)/len(hundreds)
print(f"Average for 100 elements: {hundredsAverage} seconds")
print("")

# Test of 1,000
thousands = []
tests = 1000
thousands.append(testCarmen.TestComplexity(tests))
thousands.append(testCarmen.TestComplexity(tests))
thousands.append(testCarmen.TestComplexity(tests))
thousandsAverage = sum(thousands)/len(thousands)
print(f"Average for 1,000 elements: {thousandsAverage} seconds")
print("")

# Test of 100,000
hundredThousands = []
tests = 100000
hundredThousands.append(testCarmen.TestComplexity(tests))
hundredThousands.append(testCarmen.TestComplexity(tests))
hundredThousands.append(testCarmen.TestComplexity(tests))
hundredThousandsAverage = sum(hundredThousands)/len(hundredThousands)
print(f"Average for 100,000 elements: {hundredThousandsAverage} seconds")
print("")

# Test of 1,000,000
millions = []
tests = 1000000
millions.append(testCarmen.TestComplexity(tests))
millions.append(testCarmen.TestComplexity(tests))
millions.append(testCarmen.TestComplexity(tests))
millionsAverage = sum(millions)/len(millions)
print(f"Average for 1,000,000 elements: {millionsAverage} seconds")
print("")


# Discussion
print("If you look at the image file included in this project")
print("you will see the graph appears linear as the elements")
print("increase drastically. This causes me to believe that")
print("it is of O(n) complexity. This is because")
print("I was always testing the extreme time cases.")
print("-Drake Cummings")
