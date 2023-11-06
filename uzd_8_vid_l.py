from doctest import testmod
def uzd8(x, y: float):
    """
    Funkcija pārbauda taisnstūri ar vertikālām līnijām x=-5 un x=2,
    kā arī horizontālām līnijām y=-1 un y=3.

    Funkcija uzd8 ņem punkta (x, y) koordinātas un atgriež:
         - 1, ja punkts atrodas taisnstūra iekšpusē,
         - 2, ja punkts atrodas uz taisnstūra malas,
         - 3, ja punkts atrodas ārpus taisnstūra.
    Piemēri:
    >>> uzd8(0, 0)
    1
    >>> uzd8(2, -2)
    2
    >>> uzd8(4, 3)
    3
    >>> uzd8(3, 0)
    2
    >>> uzd8(1, -2)
    2
    >>> uzd8(-1, -2)
    2
    >>> uzd8(3, 1)
    2
    >>> uzd8(-2, 0)
    3
    >>> uzd8(4, 2)
    3
    >>> uzd8(0, 0)
    1
    >>> uzd8(2, -2)
    2

    >>> uzd8(4, 2)
    3

    >>> uzd8(-1, 0)
    2
    >>> uzd8(0, -2)
    2
    
    >>> uzd8(2, 1)
    2
    >>> uzd8(1, 1)
    2
    >>> uzd8(2, -2)
    2
    >>> uzd8(1, -2)
    2
    >>> uzd8(3, -1)
    2
    >>> uzd8(-5, -1)
    2

    
    """
    
    if x >= -5 and x <= 2 and y >= -1 and y <= 3:
        if x == -5 or x == 2 or y == -1 or y == 3:
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

if uzd8(x,y) == 1:
    print("punkts atrodas iekšā")
elif uzd8(x,y) == 2:
    print("punkts atrodas uz robežas")
else:
    print("punkts atrodas arpusē")
    
