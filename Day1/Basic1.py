### 표준 출력
# 변수에 문자담기
name = '홍길동'
greeting = '안녕'

print(name, greeting)
print(greeting, name)

text = name + '님, ' + greeting + '하세요'
print(text)

# 변수에 숫자담기
coffee1_name = '카페라떼';
coffee1_val = 4000;
coffee2_name = '카푸치노';
coffee2_val = 4500;
coffee3_name = '마끼야또';
coffee3_val = 5000;

# Case 1
print('손님, ' + coffee1_name + coffee2_name + coffee3_name + '를 주문하셨습니다.')
#print('가격은 ' + coffee1_val + coffee2_val + coffee3_val + '원 입니다.')
# TypeError 발생

# Case 2
print('손님, ' + coffee1_name + coffee2_name + coffee3_name + '를 주문하셨습니다.')
print('가격은 ' + str(coffee1_val + coffee2_val + coffee3_val) + '원 입니다.')

# Case 3
coffee_val = coffee1_val + coffee2_val + coffee3_val
print('손님, \n%s, %s, %s를 주문하셨습니다.' % (coffee1_name, coffee2_name, coffee3_name))
print('가격은 %d원 입니다.' % coffee_val)

### 표준 입력

# Case 1
name = input('당신의 이름은 무엇입니까? ')

print(name + '님, 반갑습니다.')

# Case 2
order = input('OO카페입니다. \n무엇을 주문하시겠습니까? ')
count = input('몇 잔을 드릴까요? ')

print('%s %s잔을 주문하셨습니다. \n잠시만 기다려주세요~^^' % (order, count))

# Case 3
price = 4500
cost  = price * int(count) # count 데이터 타입은 문자이므로 int형으로 바꿔줘야함

print('%s %s잔을 주문하셨습니다. \n결재하실 금액은 %s원입니다~^^' % (order, count, cost))



### 주석문
# 이 줄은 라인 코멘트입니다
print ("Hello World!")
print ("Hello World!")    # 이것도 라인 코멘트입니다
print ("Hello World!")    # 이것도 라인 코멘트입니다

"""
블럭주석, 
즉 멀티라인의 주석문은 따옴표(''' ''') 3개
"""
# 한줄주석문은 샵(#)기호
