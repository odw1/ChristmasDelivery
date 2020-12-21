import pytest

from src.present import Present
from src.toymachine import ToyMachine
from src.santasSleigh import SantasSleigh
from src.elf import Elf

def test_should_pack_present_when_available():

    present = Present()
    santasSleigh = SantasSleigh()

    elf = Elf(santasSleigh)
    elf.givePresentTo(present)

    assert santasSleigh.presentsCount() == 1
