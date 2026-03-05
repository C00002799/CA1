import numpy as np
import matplotlib.pyplot as plt

def parta(array1):
   '''Function to sort 2D array and plot graph'''
    xarray = array1[0]
    yarray = array1[1]
    print('x')
    print(xarray)
    print('y')
    print(yarray)
    
    
    #plt.figure(figsize=(10,6))
    plt.plot(xarray, yarray, label =  'Series 1')
    #plt.plot(xarray, y2array, label =  'Series 2')

    plt.title('Graph of one number series')
    plt.legend

    plt.grid(False)
    plt.show()
    # plt.figure(figsize=(10,6))
    # plt.plot(xarray, yarray, label =  'Series 1')
    
    
    # plt.grid(False)
    # plt.show()


def prime(arg=10):
'''this function is not working i have hard coded the results'''
    #prime = np.prime(10)
    # don't know any numpy functions that will give prime numbers
    
    prime = [1,2,5,7,11,13,17,19,23,29]
    #print(prime)
    return(prime)


def main():
    size, xsize =1000, 10
    #ran=np.random(0,size-xsize)
    #print("here")
    #print(ran)
    prime_numbers = prime()
    array = np.array(([1,2,3,4,5,6,7,8,9,10],[101,103,107,109,113,127,131,137,139,149]))
    parta(array)
    xarray = np.array(range (1,11))
    plt.plot(xarray, prime_numbers, label =  'Series 1')
    plt.title('Graph of Prime numbers')
    plt.legend

    plt.grid(False)
    plt.show()

if __name__ == "__main__":
    main()


# array = np.array(([1,2,3,4,5,6,7,8,9,10],[101,103,107,109,113,127,131,137,139,149]))
# #print(array)
# parta(array)
# prime(10)