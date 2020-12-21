class Elf:
    def __init__(self, santasSleigh):
        self.santasSleigh = santasSleigh

    def givePresentTo(self, present):
        self.santasSleigh.pack(present)