from lab06 import ensureSortedAscending
from lab06 import mergesort
from lab06 import getBestApartment
from lab06 import getWorstApartment
from lab06 import getAffordableApartments
from Apartment import Apartment

a0 = Apartment(1200, 200, "average")
a1 = Apartment(1200, 200, "excellent")
a2 = Apartment(1000, 100, "average")
a3 = Apartment(1000, 215, "excellent")
a4 = Apartment(700, 315, "bad")
a5 = Apartment(800, 250, "excellent")
apartmentList = [a0, a1, a2, a3, a4, a5]

def test_getRent():
    assert a0.getRent()==1200

def test_getmeters():
    assert a1.getMetersFromUCSB()==200

def test_getcondition():
    assert a2.getCondition()=='average'

def test_getapartmentdetails():
    assert a2.getApartmentDetails() =='(Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: average'

def test_gt():
    assert (a0>a4) == True
    assert (a5>a3) == False

def test_lt():
    assert (a4<a1) == True
    assert (a0<a5) == False

def test_eq():
    assert (a4==a5)==False

def test_ensuresorted():
    assert ensureSortedAscending(apartmentList) == False

def test_mergesort():
    numList1 = [9,8,7,6,5,4,3,2,1]
    numList2 = [1,2,3,4,5,6,7,8,9]
    mergesort(numList1)
    mergesort(numList2)
    assert numList1 == [1,2,3,4,5,6,7,8,9]
    assert numList2 == [1,2,3,4,5,6,7,8,9]
    

def test_getbestapartment():
    assert getBestApartment(apartmentList)=='(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad'
    

def test_getworstapartment():
    assert getWorstApartment(apartmentList)=='(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average'

def test_getaffordableapartments():
    assert getAffordableApartments(apartmentList, 950)=='(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad\n(Apartment) Rent: $800, Distance From UCSB: 250m, Condition: excellent\n'
