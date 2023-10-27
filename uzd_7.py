import doctest


def parbaudit_taisnsturis(p_x, p_y: float):

"""
    >>>parbaudit_taisnsturis(2,1)
    >>>parbaudit_taisnsturis(-2,-1)
    >>>parbaudit_taisnsturis(0,0)

"""

    if p_x >= -1  and p_x<= 3 and p_y >= -2 and p_y <= 1:
        if p_x == -1  and p_x== 3 and p_y == -2 and p_y == 1:
            return 2
        else:
            return 1
    else:
        return 3


doctest.testmod(verbose = True)


    
