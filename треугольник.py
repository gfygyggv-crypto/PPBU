import turtle as t
t.hideturtle() # скрыть
t.pensize(3) # толщина линии
t.color('red')
#t.rt(60)
for i in range(4, 56, 4):
    t.fd(i) #вперед
    t.rt(90)
t.rt(270)
for i in range(52, 0, -4):
    t.fd(i) #вперед
    t.rt(90) #налево