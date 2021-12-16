import pytest
from students import Students

# instances
student1 = Students(first_name="Kaisa", last_name="Saar", phone_number=56909604, address="Kase tee 6")
student2 = Students(first_name="Krista", last_name="Tamm", phone_number=53495472, address="Pargi tee 12")
student3 = Students(first_name="Liina", last_name="Kask", phone_number=53465783, address="Aasa tee 2")


def test_first_name():
    assert student1.get_first_name() == "Kaisa"
    assert student2.get_first_name() == "Krista"
    assert student3.get_first_name() == "Liina"

def test_last_name():
    assert student1.get_last_name() == "Saar"
    assert student2.get_last_name() == "Tamm"
    assert student3.get_last_name() == "Kask"

def test_full_name():
    assert student1.get_full_name() == "Kaisa Saar"
    assert student2.get_full_name() == "Krista Tamm"
    assert student3.get_full_name() == "Liina Kask"

def test_phone_number():
    assert student1.get_phone_number() == 56909604
    assert student2.get_phone_number() == 53495472
    assert student3.get_phone_number() == 53465783

def test_address():
    assert student1.get_address() == "Kase tee 6"
    assert student2.get_address() == "Pargi tee 12"
    assert student3.get_address() == "Aasa tee 2"
