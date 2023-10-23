import doctest 

def figura(x,y):
'''
>>> figura(0,2)
'''

if p_x>=1 and p_x<=3 and p_y>=-2 and p_y<=1:
    if p_x==-1 or p_x==3 or p_y==-2 or p_y ==1:
        print("Figura robezlinijā")
    else:
        print("Figura iekša")
else:
    print("Figura arpus")


doctest.testmod(name='testing', verbose=True)
