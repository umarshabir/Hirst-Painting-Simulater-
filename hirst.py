import random, turtle as t

tim = t.Turtle()
t.colormode(255)


color_list = [(234, 166, 59), (45, 112, 157), (113, 150, 203), (212, 123, 164), (16, 128, 96), (172, 44, 88)]
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

def draw_dots():
    for _ in range(10):
        for _ in range(10):
            tim.dot(20, random.choice(color_list))
            tim.penup()
            tim.forward(50)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


draw_dots()

screen = tim.Screen()
screen.exitonclick()
