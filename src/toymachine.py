from src.present import Present

class ToyMachine:

    def __init__(self, presentsReady):
        self.__givePresentTo = None
        self.presentsReady = presentsReady

    def elfReady(self, givePresentTo):
        self.__givePresentTo = givePresentTo

    def givePresentToElf(self):
        if self.__givePresentTo is None: return
        if self.presentsReady < 1: return

        self.__givePresentTo(Present())
        self.elfReady(None)
        self.presentsReady = self.presentsReady - 1
