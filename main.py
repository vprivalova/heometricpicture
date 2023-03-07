"""
Privalova Viktoria
Khludina Ksenia
Nizovtseva Anastasia

"""

import turtle as t


def background():
    """
    TODO: Vika
    Function is limiting background and colouring it.
    :return:
    """
    t.pu()
    t.fillcolor('#191970')
    t.begin_fill()
    t.goto(-500, 400)
    t.pd()
    t.speed(8)
    t.fd(1000)
    t.rt(90)
    t.fd(800)
    t.rt(90)
    t.fd(1000)
    t.rt(90)
    t.fd(800)
    t.end_fill()
    t.pu()
    t.goto(0, 0)
    t.rt(90)


def triangle(x, y, a, fillcolour, pensize, pencolor):
    """
    TODO: Ksenia
    Function is drawing an isosceles triangle. #равнобедренный треугольник
    :param x: first coordinate of the start of drawing triangle
    :param y: last coordinate of the start of drawing triangle
    :param a: lenght of the side of the triangle, other side (b) is equal
    :param fillcolour: triangle fill colour #цвет заливки треугольника
    :param pensize: contour width
    :param pencolor: colour of the contour
    :return:
    """
    t.goto(x, y)
    t.pd()
    t.speed(8)
    t.pensize(pensize)
    t.pencolor(pencolor)
    t.fillcolor(fillcolour)
    t.begin_fill()
    t.fd(a)
    t.lt(120)
    t.fd(a)
    t.lt(120)
    t.fd(a)
    t.end_fill()
    t.pu()
    t.setheading(0)


def star(x, y, a, fillcolour, pensize, pencolour):
    """
    TODO: Nastya
    Function is drawing a star.
    :param x: first coordinate of the start of drawing star
    :param y: second coordinate of the start of drawing star
    :param a: length of the side of star
    :param fillcolour: star fill colour
    :param pensize: contour width
    :param pencolour: colour of the contour
    :return:
    """

    t.goto(x, y)
    t.pd()
    t.speed(8)
    t.pensize(pensize)
    t.color(pencolour)
    size = a
    angle = 120
    t.fillcolor(fillcolour)
    t.begin_fill()
    for side in range(5):
        t.fd(size)
        t.rt(angle)
        t.fd(size)
        t.rt(72 - angle)

    t.end_fill()
    t.pu()


def circle(x, y, radius, fillcolour, pensize, pencolour):
    """
    TODO: Vika
    Function is drawing a circle.
    :param x: first coordinate of the center of the circle
    :param y: second coordinate of the center of the circle
    :param radius: half of diameter of the circle
    :param fillcolour: circle fill colour
    :param pensize: contour width
    :param pencolour: colour of the contour
    :return:
    """
    t.goto(x, y)
    t.pd()
    t.speed(8)
    t.fillcolor(fillcolour)
    t.pencolor(pencolour)
    t.begin_fill()
    t.pensize(pensize)
    t.circle(radius)
    t.end_fill()
    t.setheading(0)
    t.pu()


def semicircle(x, y, radius, fillcolour, pensize, pencolour):
    """
    TODO: Vika
    Function is drawing a circle.
    :param x: first coordinate of the center of the circle
    :param y: second coordinate of the center of the circle
    :param radius: half of diameter of the circle
    :param fillcolour: circle fill colour
    :param pensize: contour width
    :param pencolour: colour of the contour
    :return:
    """
    t.goto(x, y)
    t.setheading(90)
    t.pd()
    t.speed(8)
    t.fillcolor(fillcolour)
    t.pencolor(pencolour)
    t.begin_fill()
    t.pensize(pensize)
    t.circle(radius, 180)
    t.end_fill()
    t.setheading(0)
    t.pu()


def square(x, y, a, fillcolour, pensize, pencolour):
    """
    TODO: Nastya
    Function is drawing a square.
    :param x: first coordinate of the start of drawing square
    :param y: second coordinate of the start of drawing square
    :param a: length of the side of the square
    :param fillcolour: square fill colour
    :param pensize: contour width
    :param pencolour: colour of the contour
    :return:
    """
    t.speed(8)
    t.goto(x, y)
    t.pd()
    t.fillcolor(fillcolour)
    t.pencolor(pencolour)
    t.pensize(pensize)
    t.begin_fill()
    for i in range(4):
        t.forward(a)
        t.right(90)

    t.end_fill()
    t.pu()
    t.setheading(0)



def rectangle(x, y, a, b, fillcolour, pensize, pencolour):
    """
    TODO: Ksenia
    Function is drawing a rectangle.
    :param x: first coordinate of the start of drawing rectangle
    :param y: second coordinate of the start of drawing rectangle
    :param a: length of the shorter side
    :param b: length of the longer side
    :param fillcolour: rectangle fill colour
    :param pensize: contour width
    :param pencolour: colour of the contour
    :return:
    """
    t.goto(x, y)
    t.pd()
    t.speed(8)
    t.pensize(pensize)
    t.pencolor(pencolour)
    t.fillcolor(fillcolour)
    t.begin_fill()
    for i in range(2):
        t.fd(a)
        t.lt(90)
        t.fd(b)
        t.lt(90)
    t.end_fill()
    t.pu()
    t.setheading(0)


background()
circle(-420, 295, 50, '#edebe0', 4, '#EEE8AA')
square(-480, -200, 200, '#EE82EE', 4, '#DA70D6')
triangle(-480, -200, 200, '#ADD8E6', 4, '#87CEEB')
square(-430, -250, 100, 'yellow', 2, '#423f30')
rectangle(-280, -400, 177, 400, "#FF7F50", 4, '#FF6347')
semicircle(-103, 0, 88.5, '#00FA9A', 4, '#66CDAA')
square(-215, -70, 50, 'yellow', 2, '#423f30')
square(-215, -170, 50, 'yellow', 2, '#423f30')
square(-215, -270, 50, 'yellow', 2, '#423f30')
star(-200, 300, 20, '#f7fc99', 2, '#BDB76B')
star(-400, 170, 20, '#f2ff00', 2, '#BDB76B')


t.goto(-100,-400)
t.setheading(90)
t.pd()
t.pencolor('white')
t.fd(800)

#тут область насти
t.pu()
t.goto(200,-400)
t.setheading(90)
t.pd()
t.pencolor('white')
t.fd(800)
t.pu()
#тут область ксюши
t.mainloop()





# triangle(0, 0, 40, 'yellow', 3, 'blue')
# circle(50, 50, 20, 'red', 3, 'green')
# semicircle(50, 50, 20, 'red', 3, 'green')
# square(-200, 90, 50, 'yellow', 3, 'blue')
# star(40, 40, 'black', 3, 'yellow')
# rectangle(-60, 60, 70, 30, "green", 3, 'black')