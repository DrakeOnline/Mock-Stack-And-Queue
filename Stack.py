# --------------------------------------------------------- #
#   Title:      Stack.py                                    #
#   Author:     Drake G. Cummings                           #
#   Date:       January 22nd, 2021                          #
#   Purpose:    Class for mock-stack in python              #
# --------------------------------------------------------- #

class Stack:

    def __init__(self):
        self.items = []

    # Push
    def Push(self, newItem):
        newList = []

        # Add new item to front of list
        newList.append(newItem)

        # Add the rest of the list
        for x in self.items:
            newList.append(x)

        # Overwrite old list
        self.items = newList

    # Pop
    def Pop(self):
        # Save first item to return
        firstItem = self.items[0]

        # Make new list
        newList = []
        for x in range(1, len(self.items)):
            newList.append(self.items[x])

        # Save new list
        self.items = newList

        # Return first item
        return firstItem

    # Contains
    def Contains(self, item):

        # Create flag that activates when item is found
        itemFound = False
        for x in self.items:
            if item == x:
                itemFound = True

        return itemFound
