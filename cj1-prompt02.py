def Separator():
    print('------')

def SumTwoFloats():
    a = 1.5
    b = 2.5
    print(f'The sum of `a` ({a}, {type(a)}) and `b` ({b}, {type}) is:')
    c = a+b
    print(c)
    print(f'This has the resulting type {type(c)}')

def DiffTwoInts():
    a = 10
    b = 5
    print(f'The difference between `a` ({a}, {type(a)}) and `b` ({b}, {type}) is:')
    c = abs(a-b)
    print(c)
    print(f'This has the resulting type {type(c)}')

def ProdOneFloatOneInt():
    a = 2.5
    b = 5
    print(f'The product between `a` ({a}, {type(a)}) and `b` ({b}, {type}) is:')
    c = a*b
    print(c)
    print(f'This has the resulting type {type(c)}')

def main():
    SumTwoFloats()
    Separator()
    DiffTwoInts()
    Separator()
    ProdOneFloatOneInt()


if __name__ == "__main__":
    main()