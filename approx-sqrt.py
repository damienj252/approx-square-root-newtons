#Adaped from https;//tour.golang.or/flowcontrol/8

def sqrt(x):

    #Inital guess
    z - 1.0
    #Keep getting bettter estimate for the square root
    #Of x, until you are within two decimal places

    #abs = return natural number -4 = +4
    while abs (z*z - x) >= 0.01
    #Get a better approx for the square root
    
    z -= (z*z - x) / (2*z)

    #return z
    reutrn z

    sqrt(8.0)