def sum_factorial(num) :
    if num > 0 :
        return num + sum_factorial(num-1)
    else :
        return 1

def factorial(num) :
    if num > 0 :
        return num * factorial(num-1)
    else :
        return 1

if __name__ == "__main__" :
    temp = input("숫자를 입력해주세요")
    print("{0} 까지의 합계는 {1} 입니다.".format(sum_factorial(int(temp)), factorial(int(temp))))