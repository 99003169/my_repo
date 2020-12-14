def test(a , b, fcomp):
    c = fcomp(a,b)
    print(c)
    
def mysum(a,b):
    return a + b
    
def multiply(a,b)
    return a * b
    
test(10, 20, mysum)               #function name as arg
test(12, 15, multiply)
test(fcomp=mysum, a=15, b=25)

# test(10, 20, sum(1,2) )       #wrong, function call as arg
