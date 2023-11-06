from doctest import testmod
def uzd9(x, y: float)  -> int:
    """
    Funkcija pārbauda trijstūri ar vertikālām līnijām x=0,
    kā arī horizontālām līnijām y=-1 un y=-1.5x+3

    Funkcija uzd9 ņem punkta (x, y) koordinātas un atgriež:
         - 1, ja punkts atrodas trijstūra iekšpusē,
         - 2, ja punkts atrodas uz trīsstūra malas,
         - 3, ja punkts atrodas ārpus trijstūra.

    Piemēri:
    >>> uzd9(0, -1)
    1
    >>> uzd9(0, 3)
    1
    >>> uzd9(-5, 0)
    3
    >>> uzd9(2, -2)
    3
    >>> uzd9(1, 3)
    3
    >>> uzd9(0, -1.5)
    3
    >>> uzd9(-1, 2)
    3
    >>> uzd9(2, 0)
    1
    >>> uzd9(-3, 1)
    3
    >>> uzd9(3, -1)
    3
    >>> uzd9(0, 1.5)
    1

    >>> uzd9(-4, 2)
    3
    >>> uzd9(4, -2)
    3
    >>> uzd9(0, 0)
    1
    >>> uzd9(0, -1.49)
    3
    >>> uzd9(0, 3.01)
    3
    """

    if x >= 0 and y >=-1 and y <= -1.5*x+3:
        if x==0 or y==-1 or y==-1.5*x+3:
            return 1
        else:
            return 2
    else:
        return 3


testmod(verbose=True)
x = float(input("Ievadiet punkta x: "))
y = float(input("Ievadiet punkta y: "))

if uzd9(x,y) == 1:
    print("punkts atrodas iekšā")
elif uzd9(x,y) == 2:
    print("punkts atrodas uz robežas")
else:
    print("punkts atrodas arpusē")

