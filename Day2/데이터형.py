# 숫자형 - 기본연산
x = 50
y = 4.

print("x = ", x)
print("y = ", y)
print("x + y = " , x+y)
print("x - y = " , x-y)
print("x * y = " , x*y)
print("x / y = " , x/y)
print("x //y = " , x//y)
print("x % y = " , x%y)
print("-x = "    , -x)
print("+x = "    , +x)
print("x ** y = ", x**y)
print("pow(x,y) = ", pow(x,y))


# 논리형 - 비교연산자와 논리연산자
x = 4
y = 9

print("x == y = ", x==y)
print("x != y = ", x!=y)

print("x < y  = ", x<y)
print("x > y  = ", x>y)

print("int(True)  = ", int(True))
print("int(False) = ", int(False))


# 문자형 - 이스케이프 문자
text1 = "안녕하세요!\n하나금융\t임직원여러분 !"

text2 = '''
빅데이터를 위한 파이썬과정에서
만나뵙게되어 반갑습니다.
끝까지 '화이팅' 하세요!!!
'''
print(text1)
print(text2)

# 문자형함수1
test = '파이썬 프로그래밍 재미있다!'    # 문자열을 변수에 저장

result = test.startswith('파이썬')        # 문자열이 '파이썬으로 시작하는지 확인
print(result)
result = test.endswith('!')               # 문자열이 '!'로 끝나는지 확인
print(result)
result = test.endswith('어려워요!')       # 문자열이 '어려워요!'로 끝나는지 확인
print(result)
result = test.replace('파이썬', 'Python')   # 문자열중 '파이썬'을 'Python'으로 변경
print(result)

# 문자형함수2
test = 'Python Programming is Interesting!'

result = test.upper()      # 문자열을 모두 대문자로 변경
print(result)
result = test.lower()      # 문자열을 모두 소문자로 변경
print(result)
result = '/'.join(test)      # 문자열의 각 문자 사이에 '/'문자 집어 넣기
print(result)

# 데이터형 확인
num_data = 350
str_data = '350'

print(type(num_data))
print(type(str_data))

# 에러발생
# sum = num_data + str_data
# sum

# 데이터형 변환
sum = int(str_data) + num_data
print('합계는? ', str(sum))