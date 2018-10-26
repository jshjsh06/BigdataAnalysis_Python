count = 0
numberList = ['1', '2', '3' ,'4' ,'5', '6', '7', '8', '9', '0']
temp = input("숫자를 입력해주세요 : ")

while True :
    for i in range(len(temp)) :
        for x in numberList :
            if temp[i] == x :
                count = count + 1
                break

    if count == len(temp) :
        break
    else :
        pass
    print("입력한 값이 숫자가 아닙니다.")
    temp = input("숫자를 입력해주세요 : ")

sum = 0
for i in range(int(temp)+1) :
    sum = sum + i

print(sum)

num = 0
