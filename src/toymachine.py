from src.present import Present

class ToyMachine:

    def __init__(self, presentsReady):
        self.givePresentTo = None
        self.presentsReady = presentsReady

    def elfReady(self, givePresentTo):
        self.givePresentTo = givePresentTo

    def givePresentToElf(self):
        if self.givePresentTo is None: return
        if self.presentsReady < 1: return

        self.givePresentTo(Present())
        self.elfReady(None)
        self.presentsReady = self.presentsReady - 1
