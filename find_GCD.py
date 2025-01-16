#Initialize a class to implement the Euclidean Algorithm for finding GCD of number a and b.

class EuclideanAlgorithm:
    #Define a function to calculate GCD using the Euclidean Algorithm
    #a and b should be positive integer
    def find_GCD(a,b):
        #Ensure a and b are integer
        if a<=0 or b<=0:
            print("Input positive numbers.")
        #Inpliment the Euclidean Algorithm
        while b!=0:
            reminder=a-a//b*b
            a,b=b,reminder
        return a



