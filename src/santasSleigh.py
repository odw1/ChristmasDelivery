class SantasSleigh:
    def __init__(self):
        self.__packedPresents = []

    def pack(self, present):
        self.__packedPresents.append(present)

    def presentsCount(self):
        return len(self.__packedPresents)