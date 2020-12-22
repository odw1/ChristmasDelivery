import pytest

from src.toymachine import ToyMachine
from src.mrsClaus import MrsClaus

def test_should_give_present_when_available():
    
    mrsClaus = MrsClaus()
    toyMachine = ToyMachine(mrsClaus, 5)
    toyMachine.startGivingPresentsToMrsClaus()
    
    assert mrsClaus.recievedPresentCount() == 5
    assert toyMachine.presentsReady == 0

def test_should_not_give_present_when_not_available():

    mrsClaus = MrsClaus()
    toyMachine = ToyMachine(mrsClaus, 0)
    toyMachine.startGivingPresentsToMrsClaus()
    
    assert mrsClaus.recievedPresentCount() == 0
    assert toyMachine.presentsReady == 0

def test_should_add_more_presents():

    mrsClaus = MrsClaus()
    toyMachine = ToyMachine(mrsClaus, 0)
    toyMachine.startGivingPresentsToMrsClaus()
    
    assert mrsClaus.recievedPresentCount() == 0
    assert toyMachine.presentsReady == 0

    toyMachine.morePresentsReady(50)

    assert mrsClaus.recievedPresentCount() == 50
    assert toyMachine.presentsReady == 0