# import turtle as t
# import  time
# t.hideturtle()
# t.speed(0)
# r = 20
# t.pensize(4)
# t.color("#FFA500")
# t.fillcolor("#A200FF")
# for k in range(3):
#     for j in range(4):
#       for i in range(6):
#         t.begin_fill()
#         t.circle(r)
#         t.end_fill()
#         t.rt(60)
#         time.sleep(1)
#       r = r - 5
#     t.pu()
#     t.fd(80)
#     t.pd()
#     r = 20

  # '''диапазон'''
import turtle as t

t.hideturtle()
t.pensize(5)
for r in range(40, 0, -10):
    for i in range(6):
        t.color(255, 165, r * 6)
        t.fillcolor(162, r * 6, 255)
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.rt(60)
