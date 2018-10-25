import turtle
import time
import math

basicLength = 100

# for i in range(4) :
#     turtle.forward(basicLength)
#     turtle.left(90)
#
# turtle.left(45)
# turtle.forward(math.sqrt(basicLength**2 * 2 ))
#
# turtle.left(135)
# turtle.forward(basicLength)
# turtle.left(135)
# turtle.forward(math.sqrt(basicLength**2 * 2 ))
#
# turtle.left(135)
# turtle.forward(basicLength)
#
# turtle.left(45)
# turtle.forward(math.sqrt((basicLength/2)**2 * 2))
# turtle.left(90)
# turtle.forward(math.sqrt((basicLength/2)**2 * 2))
#
# turtle.done()

flag = 120
count = 0
for i in range(6) :
    turtle.forward(50)
    turtle.left(60)

turtle.right(flag)

for i in range(6) :
    turtle.forward(50)
    turtle.left(60)

while(count != 5) :
    turtle.right(flag)

    for i in range(7) :
        turtle.forward(50)
        turtle.left(60)

    count = count + 1

turtle.done()


"""
import turtle as t
n = 80
a = 60

t.color('red')
t.pensize(5)

for _ in range(6):
	t.forward(n)
	t.right(a)
	for _ in range(6):
		t.forward(n)
		t.left(a)

t.done()
"""