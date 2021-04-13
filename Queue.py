# --------------------------------------------------------- #
#   Title:      Queue.py                                    #
#   Author:     Drake G. Cummings                           #
#   Date:       January 22nd, 2021                          #
#   Purpose:    Class for mock-queue in python              #
# --------------------------------------------------------- #

class Queue:

    def __init__(self):
        self.items = []

    # Append
    def Append(self, newItem):
        self.items.append(newItem)

    # Pop
    def Pop(self):
        # Save last item
        lastItem = self.items[len(self.items)-1]

        # Make new list
        newList = []
        # Add every item to the new list except the last item
        for x in range(0, len(self.items)-1):
            newList.append(self.items[x])

        # Save new list
        self.items = newList

        return lastItem

    # Contains
    def Contains(self, item):
        # Create flag that activates when item is found
        itemFound = False
        for x in self.items:
            if item == x:
                itemFound = True

        return itemFound
