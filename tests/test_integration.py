import pytest

from src.present import Present
from src.toymachine import ToyMachine
from src.santasSleigh import SantasSleigh
from src.elf import Elf
from src.mrsClaus import MrsClaus

def test_add_present_to_santa_sleigh_via_an_elf():

    santasSleigh = SantasSleigh()

    mrsClaus = MrsClaus()
    toyMachine = ToyMachine(mrsClaus, 100)

    toyMachine.startGivingPresentsToMrsClaus()

    for i in range(200):
        elf = Elf(santasSleigh)
        mrsClaus.elfReady(elf.givePresentTo)

    toyMachine.morePresentsReady(100)

    assert santasSleigh.presentsCount() == 200
