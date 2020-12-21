import pytest

from src.present import Present
from src.toymachine import ToyMachine
from src.santasSleigh import SantasSleigh
from src.elf import Elf

def test_add_present_to_santa_sleigh_via_an_elf():

    santasSleigh = SantasSleigh()
    elf = Elf(santasSleigh)

    toyMachine = ToyMachine(5)
    toyMachine.elfReady(elf.givePresentTo)

    assert santasSleigh.presentsCount() == 0

    toyMachine.givePresentToElf()

    assert santasSleigh.presentsCount() == 1

    toyMachine.elfReady(elf.givePresentTo)
    toyMachine.givePresentToElf()

    assert santasSleigh.presentsCount() == 2
