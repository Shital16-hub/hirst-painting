import colorgram
import turtle as t
import random

# rgb_list = []
# colors = colorgram.extract('DHS5905_771_0.jpg', 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_list.append(rgb_color)
#
# print(rgb_list)
# From above code we got bellow color list of input image

t.colormode(255)
timmy = t.Turtle()
color_list = [(228, 225, 222), (231, 206, 83), (229, 147, 85), (217, 227, 219),
              (119, 166, 186), (160, 13, 19), (232, 221, 226), (30, 110, 159),
              (235, 81, 44), (215, 222, 228), (5, 99, 37), (176, 19, 14), (187, 187, 25),
              (121, 177, 144), (207, 62, 22), (23, 132, 41), (245, 201, 4), (10, 42, 77),
              (13, 64, 41), (137, 83, 98), (83, 17, 24), (46, 168, 74), (3, 66, 140),
              (173, 133, 149), (36, 25, 21)]

timmy.setheading(225)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.fd(315)
timmy.setheading(360)
no_dots = 100

for dots in range(1, no_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.fd(50)

    if dots%10 == 0:
        timmy.setheading(90)
        timmy.fd(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = t.Screen()
screen.exitonclick()





