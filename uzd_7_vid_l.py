from doctest import testmod

def uzd7(x, y: float):
    """
    Funkcija pārbauda taisnstūri ar vertikālām līnijām x=-1 un x=3,
    kā arī horizontālām līnijām y=2 un y=-1.

    Funkcija uzd7 ņem punkta (x, y) koordinātas un atgriež:
         - 1, ja punkts atrodas taisnstūra iekšpusē,
         - 2, ja punkts atrodas uz taisnstūra malas,
         - 3, ja punkts atrodas ārpus taisnstūra.
    


    >>> uzd7(0, 0)
    1
    >>> uzd7(2, -2)
    2
    >>> uzd7(4, 3)
    3
    >>> uzd7(3, 0)
    2
    >>> uzd7(1, -2)
    2
    >>> uzd7(-1, -2)
    2
    >>> uzd7(3, 1)
    2
    >>> uzd7(-2, 0)
    3
    >>> uzd7(4, 2)
    3
    >>> uzd7(0, 0)
    1
    >>> uzd7(2, -2)
    2
    >>> uzd7(4, 3)
    3
    >>> uzd7(3, 0)
    2
    >>> uzd7(1, -2)
    2
    >>> uzd7(-1, -2)
    2
    >>> uzd7(3, 1)
    2
    >>> uzd7(-2, 0)
    3
    >>> uzd7(4, 2)
    3

    >>> uzd7(-1, 0)
    2
    >>> uzd7(0, -2)
    2
    
    >>> uzd7(2, 1)
    2
    >>> uzd7(1, 1)
    2
    
    >>> uzd7(2, -2)
    2
    >>> uzd7(1, -2)
    2
    
    >>> uzd7(3, -1)
    2
    >>> uzd7(3, 0.5)
    2

    
    """
    
    if x >= -1 and x <= 3 and y >= -2 and y <= 1:
        if x == -1 or x == 3 or y == -2 or y == 1:
            return 2
            #print("Uz robežas")
        else:
            return 1
            #print("Iekšā")
    else:
        return 3
        #print("Ārpusē")

testmod(verbose=True)
x = float(input("Ievadiet punkta x: "))
y = float(input("Ievadiet punkta y: "))

if uzd7(x,y) == 1:
    print("punkts atrodas iekšā")
elif uzd7(x,y) == 2:
    print("punkts atrodas uz robežas")
else:
    print("punkts atrodas arpusē")
