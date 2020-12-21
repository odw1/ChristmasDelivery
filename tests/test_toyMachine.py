import pytest

from src.toymachine import ToyMachine

def test_should_give_present_when_available():
    
    presentsRecievied = 0

    def presentReciver(present):
        nonlocal presentsRecievied

        if present != None:
            presentsRecievied = presentsRecievied + 1
    
    toyMachine = ToyMachine(5)
    toyMachine.elfReady(presentReciver)
    toyMachine.givePresentToElf()
    
    assert presentsRecievied == 1
    assert toyMachine.presentsReady == 4

def test_should_not_give_present_when_not_available():

    presentsRecievied = 0

    def presentReciver(present):
        nonlocal presentsRecievied

        if present != None:
            presentsRecievied = presentsRecievied + 1
    
    toyMachine = ToyMachine(0)
    toyMachine.elfReady(presentReciver)
    toyMachine.givePresentToElf()
    
    assert presentsRecievied == 0
    assert toyMachine.presentsReady == 0

def test_should_not_give_present_when_no_elf_ready():
    
    toyMachine = ToyMachine(5)
    toyMachine.givePresentToElf()
    
    assert toyMachine.presentsReady == 5

def test_should_not_give_present_when_elf_busy():
    
    presentsRecievied = 0

    def presentReciver(present):
        nonlocal presentsRecievied

        if present != None:
            presentsRecievied = presentsRecievied + 1
    
    toyMachine = ToyMachine(5)
    toyMachine.elfReady(presentReciver)
    toyMachine.givePresentToElf()
    
    assert presentsRecievied == 1
    assert toyMachine.presentsReady == 4

    toyMachine.givePresentToElf()

    assert presentsRecievied == 1
    assert toyMachine.presentsReady == 4

def test_should_give_second_present_when_elf_ready():
    
    presentsRecievied = 0

    def presentReciver(present):
        nonlocal presentsRecievied

        if present != None:
            presentsRecievied = presentsRecievied + 1
    
    toyMachine = ToyMachine(5)
    toyMachine.elfReady(presentReciver)
    toyMachine.givePresentToElf()
    
    assert presentsRecievied == 1
    assert toyMachine.presentsReady == 4

    toyMachine.givePresentToElf()

    assert presentsRecievied == 1
    assert toyMachine.presentsReady == 4

    toyMachine.elfReady(presentReciver)
    toyMachine.givePresentToElf()

    assert presentsRecievied == 2
    assert toyMachine.presentsReady == 3