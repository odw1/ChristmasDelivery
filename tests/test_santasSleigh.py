import pytest

from src.santasSleigh import SantasSleigh
from src.present import Present

def test_should_have_no_presents():
    santasSleigh = SantasSleigh()

    assert santasSleigh.presentsCount() == 0

def test_should_store_packed_presents():
    santasSleigh = SantasSleigh()

    santasSleigh.pack(Present)

    assert santasSleigh.presentsCount() == 1