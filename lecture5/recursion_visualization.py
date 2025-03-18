import turtle
t = turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.right(90)
turtle.done()


import turtle
t = turtle.Turtle()

t.pencolor('red')
t.pensize(3)
for i in range(5):
    t.forward(100)
    t.right(144)
t.hideturtle()

turtle.done()


import turtle

t= turtle.Turtle()
def drawSpiral(t, lineLen):
    if lineLen >0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t,lineLen-5)
drawSpiral(t,100)

turtle.done()


import turtle
def tree(branch_len):#树干太短不画，即递归结束条件
    if branch_len >5:#画树干
        t.forward(branch_len)
        t.right(20) #右倾斜20度
        tree(branch_len - 15) #递归调用，画右边的小树，树干减15
        t.left(40)#向左回40度，即左倾斜20度
        tree(branch_len- 15) #递归调用，画左边的小树，树干减15
        t.right(20) #向右回20度，即回正
        t.backward(branch_len) #海龟退回原位置


t= turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)#画树干长度75的二叉树
tree(75)
t.hideturtle()
turtle.done()

