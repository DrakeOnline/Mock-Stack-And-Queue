# --------------------------------------------------------- #
#   Title:      Carmen.py                                   #
#   Author:     Drake G. Cummings                           #
#   Date:       April 13th, 2021                            #
#   Purpose:    Class for mock-queue extension in python    #
# --------------------------------------------------------- #

from Queue import Queue
import time


class Carmen(Queue):
    """
    A method to return the current position of Carmen
    in a string form
    """
    def FindCarmen(self):
        for x in range(0, len(self.items)):
            if self.items[x] == "Carmen":
                return f"{self.items[x]} is {x}th in line"

    """
    A method to test the finding time of n elements
    Parameters:
        n: the number of elements to test
    """
    def TestComplexity(self, n):

        # Clear queue
        self.items = []

        # Fill queue with Bob
        for x in range(0, n):
            self.Append("Bob")

        # Change one to "Carmen"
        self.items[n-1] = "Carmen"

        startTime = time.time()
        print(self.FindCarmen())

        # This causes the time to actually register
        time.sleep(2.7)
        endTime = time.time()

        # Clear queue
        self.items = []
        return(endTime - startTime - 2.7)
