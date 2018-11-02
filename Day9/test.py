def test1_multiply(x) :
    plus = 0
    for i in list(str(2**x)) :
        plus = plus + int(i)
    print(plus)

if __name__ == "__main__" :
    test1_multiply(1000)

