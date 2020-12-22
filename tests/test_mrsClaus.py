import pytest

from src.mrsClaus import MrsClaus
from src.present import Present

@pytest.fixture
def mrsClaus_with_presents():
        
    mrsClaus = MrsClaus()

    for i in range(100):
        mrsClaus.givePresentToPack(Present())

    return mrsClaus

def test_should_not_give_presents_when_no_elfs_ready(mrsClaus_with_presents):

    mrsClaus = mrsClaus_with_presents

    assert mrsClaus.recievedPresentCount() == 100

def test_should_give_present_when_one_elf_ready(mrsClaus_with_presents):

    presentsReceived = 0

    def presentRecievier(present):
        nonlocal presentsReceived
        presentsReceived = presentsReceived + 1
    
    mrsClaus = mrsClaus_with_presents

    assert mrsClaus.recievedPresentCount() == 100

    mrsClaus.elfReady(presentRecievier)

    assert mrsClaus.recievedPresentCount() == 99

    assert presentsReceived == 1

def test_should_give_present_to_elf_when_presents_arrive_after_elf_is_ready():

    presentsReceived = 0

    def presentRecievier(present):
        nonlocal presentsReceived
        presentsReceived = presentsReceived + 1

    mrsClaus = MrsClaus()
    mrsClaus.elfReady(presentRecievier)

    for i in range(100):
        mrsClaus.givePresentToPack(Present())

    assert mrsClaus.recievedPresentCount() == 99

    assert presentsReceived == 1

def test_should_give_present_to_when_elves_and_presents_available(mrsClaus_with_presents):

    presentsReceived = 0

    def presentRecievier(present):
        nonlocal presentsReceived
        presentsReceived = presentsReceived + 1
    
    mrsClaus = mrsClaus_with_presents

    assert mrsClaus.recievedPresentCount() == 100

    for i in range(200):
        mrsClaus.elfReady(presentRecievier)

    assert mrsClaus.recievedPresentCount() == 0

    assert presentsReceived == 100

    for i in range(100):
        mrsClaus.givePresentToPack(Present())

    assert mrsClaus.recievedPresentCount() == 0

    assert presentsReceived == 200

