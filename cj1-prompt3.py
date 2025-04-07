def f(x):
    return x**3 + 8

def main():
    # call f(x) with 9
    result = f(9)
    print(result)

    # print yay if result > 27
    if result > 27:
        print("YAY!")
    

if __name__ == '__main__':
    main()