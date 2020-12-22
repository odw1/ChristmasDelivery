from collections import deque
from queue import Queue

class MrsClaus:
    
    def __init__(self):
        self.__presentsRecieved = deque()
        self.__waitingElves = Queue()

    def recievedPresentCount(self):
        return len(self.__presentsRecieved)

    def givePresentToPack(self, present):
        
        if not self.__waitingElves.empty():
            waitingElf = self.__waitingElves.get()
            waitingElf(present)
        else:
            self.__presentsRecieved.append(present)

    def elfReady(self, givePresentTo):
        presentToGive = None
        
        if len(self.__presentsRecieved) > 0:
            presentToGive = self.__presentsRecieved.pop()
        
        if not presentToGive is None:
            givePresentTo(presentToGive)
        else:
            self.__waitingElves.put(givePresentTo)
