
from Apartment import Apartment


def ensureSortedAscending(apartmentlist):
    
    for i in range(len(apartmentlist)-1):
        if apartmentlist[i]>apartmentlist[i+1]:
            return False

    return True

def mergesort(apartmentlist):

    if len(apartmentlist)>1:
        mid = len(apartmentlist)//2

        lefthalf = apartmentlist[:mid]
        righthalf = apartmentlist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0

        while i<len(lefthalf) and j<len(righthalf):

            if lefthalf[i] < righthalf[j] or lefthalf[i] == righthalf[j]:
                apartmentlist[k] = lefthalf[i]
                i = i+1

            else:
                apartmentlist[k] = righthalf[j]
                j = j+1

            k = k+1
            
        #if theres anything left in left or right half
        while i< len(lefthalf):
            apartmentlist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            apartmentlist[k] = righthalf[j]
            j = j+1
            k = k+1

def getBestApartment(apartmentlist):

    mergesort(apartmentlist)
    best = apartmentlist[0]

    return best.getApartmentDetails()



def getWorstApartment(apartmentlist):

    mergesort(apartmentlist)
    worst = apartmentlist[-1]
    return worst.getApartmentDetails()

def getAffordableApartments(apartmentlist, budget):
    s = ''
    mergesort(apartmentlist)
    for items in apartmentlist:
        if items.rent < budget or items.rent==budget:
            s += items.getApartmentDetails() + "\n"

    return s.rstrip('\n')
    




a0 = Apartment(1200, 200, "average")
a1 = Apartment(1200, 200, "excellent")
a2 = Apartment(1000, 100, "average")
a3 = Apartment(1000, 215, "excellent")
a4 = Apartment(700, 315, "bad")
a5 = Apartment(800, 250, "excellent")
apartmentList = [a0, a1, a2, a3, a4, a5]


