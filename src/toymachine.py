from src.present import Present

class ToyMachine:

    def __init__(self, mrsClaus, presentsReady):
        self.__mrsClaus = mrsClaus
        self.presentsReady = presentsReady

    def startGivingPresentsToMrsClaus(self):
        for i in range(self.presentsReady):
            self.__mrsClaus.givePresentToPack(Present())
            self.presentsReady = self.presentsReady - 1

    def morePresentsReady(self, extraPresents):
        self.presentsReady = self.presentsReady =+ extraPresents
        self.startGivingPresentsToMrsClaus()
