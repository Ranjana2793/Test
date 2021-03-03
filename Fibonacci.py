
def Fibonacci(nterms):
    fibolist =[]
    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        return "Please enter a positive integer"
    elif nterms == 1:
        return n1
    else:
        print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        fibolist.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    return fibolist

if __name__=="__main__":
    nterms = int(input("How many terms? "))
    Fibonacci(nterms)

       

