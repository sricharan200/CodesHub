# Classic way of exchanging the variables.
def classic_way_exchange(a, b):
    #Printing the assigned values
    print(f"The old value of a is {a}")
    print(f"The old value of b is {b}\n")

    #To shift the values, we need another variable i.e c

    c = b #First, we will put the value of b in c
    b = a #Second, we will put the value of a in b (b is empty due to 'First')
    a = c #Now we will put value of c in a

    #Lets print new values
    print(f"The new value of a is {a}")
    print(f"The new value of b is {b}\n")

# Much more shorter way - Pythonic Way
def pythonic_way_exchange(a, b):
    #Printing the assigned values
    print(f"The old value of a is {a}")
    print(f"The old value of b is {b}\n")

    b, a = a, b
    #Lets print new values
    print(f"The new value of a is {a}")
    print(f"The new value of b is {b}\n")

if __name__ == "__main__":
    classic_way_exchange(1, 2)
    pythonic_way_exchange(1, 2)