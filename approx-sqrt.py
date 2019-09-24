#Adaped from https;//tour.golang.or/flowcontrol/8
    
#def main():

def sqrt(x):

    #Inital guess
    z = 1.0
    #Keep getting bettter estimate for the square root
    #Of x, until you are within two decimal places

    #abs = return natural number -4 = +4
    #Running an algorithm running a while loop, finding an appromation
    #to the square root, very difficult for computers to calculate in real world
    #Depending on x, might run different times
    while abs (z*z - x) >= 0.0001:
        #Get a better approx for the square root
         z -= (z*z - x) / (2 * z)

    #return z
    return z

#Calculate the square root of 8 and print it 
z = sqrt(63.0)
#Print z
print(z)
#Print the square of the square of z
print(z*z)

#8 is between sqrt of 4 and 9 
#Between 2 and 3


    


    