"""
Privalova Viktoria 90
Khludina Ksenia 90
Nizovtseva Anastasia 79
"""

import turtle as t


def background():
    """
    TODO: Vika
    Function is limiting background and colouring it.
    :return: None
    """
    t.pu()
    t.fillcolor('#191970')
    t.begin_fill()
    t.goto(-500, 400)
    t.pd()
    t.speed(1000)
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


def triangle(x, y, a, fillcolor, pensize, pencolor):
    """
    TODO: Ksenia
    Function is drawing an equilateral triangle.
    :param x: first coordinate of the start of drawing triangle
    :param y: last coordinate of the start of drawing triangle
    :param a: length of the triangle side
    :param fillcolor: triangle filling colour
    :param pensize: contour width
    :param pencolor: colour of the contour
    :return: None
    """
    t.goto(x, y)
    t.pd()
    t.speed(1000)
    t.pensize(pensize)
    t.pencolor(pencolor)
    t.fillcolor(fillcolor)
    t.begin_fill()
    t.fd(a)
    t.lt(120)
    t.fd(a)
    t.lt(120)
    t.fd(a)
    t.end_fill()
    t.pu()
    t.setheading(0)


def star(x, y, a, fillcolor, pensize, pencolor):
    """
    TODO: Nastya
    Function is drawing a star.
    :param x: first coordinate of the start of drawing star
    :param y: second coordinate of the start of drawing star
    :param a: length of the side of star
    :param fillcolor: star filling colour
    :param pensize: contour width
    :param pencolor: colour of the contour
    :return: None
    """
    t.goto(x, y)
    t.pd()
    t.speed(1000)
    t.pensize(pensize)
    t.color(pencolor)
    size = a
    angle = 120
    t.fillcolor(fillcolor)
    t.begin_fill()
    for side in range(5):
        t.fd(size)
        t.rt(angle)
        t.fd(size)
        t.rt(72 - angle)
    t.end_fill()
    t.pu()


def circle(x, y, radius, fillcolor, pensize, pencolor):
    """
    TODO: Vika
    Function is drawing a circle.
    :param x: first coordinate of the center of the circle
    :param y: second coordinate of the center of the circle
    :param radius: half of diameter of the circle
    :param fillcolor: circle fill colour
    :param pensize: contour width
    :param pencolor: colour of the contour
    :return: None
    """
    t.goto(x, y)
    t.pd()
    t.speed(1000)
    t.fillcolor(fillcolor)
    t.pencolor(pencolor)
    t.begin_fill()
    t.pensize(pensize)
    t.circle(radius)
    t.end_fill()
    t.setheading(0)
    t.pu()


def square(x, y, a, fillcolor, pensize, pencolor):
    """
    TODO: Nastya
    Function is drawing a square.
    :param x: first coordinate of the start of drawing square
    :param y: second coordinate of the start of drawing square
    :param a: length of the side of the square
    :param fillcolor: square fill colour
    :param pensize: contour width
    :param pencolor: colour of the contour
    :return: None
    """
    t.speed(1000)
    t.goto(x, y)
    t.pd()
    t.fillcolor(fillcolor)
    t.pencolor(pencolor)
    t.pensize(pensize)
    t.begin_fill()
    for i in range(4):
        t.fd(a)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.setheading(0)


def rectangle(x, y, a, b, fillcolor, pensize, pencolor):
    """
    TODO: Ksenia
    Function is drawing a rectangle.
    :param x: first coordinate of the start of drawing rectangle
    :param y: second coordinate of the start of drawing rectangle
    :param a: length of the shorter side
    :param b: length of the longer side
    :param fillcolor: rectangle fill colour
    :param pensize: contour width
    :param pencolor: colour of the contour
    :return: None
    """
    t.goto(x, y)
    t.pd()
    t.speed(1000)
    t.pensize(pensize)
    t.pencolor(pencolor)
    t.fillcolor(fillcolor)
    t.begin_fill()
    for i in range(2):
        t.fd(a)
        t.lt(90)
        t.fd(b)
        t.lt(90)
    t.end_fill()
    t.setheading(0)
    t.pu()


def semicircle(x, y, radius, fillcolor, pensize, pencolor):
    """
    TODO: Vika
    Function is drawing a circle.
    :param x: first coordinate of the center of the circle
    :param y: second coordinate of the center of the circle
    :param radius: half of diameter of the circle
    :param fillcolor: circle fill colour
    :param pensize: contour width
    :param pencolor: colour of the contour
    :return: None
    """
    t.goto(x, y)
    t.setheading(90)
    t.pd()
    t.speed(1000)
    t.fillcolor(fillcolor)
    t.pencolor(pencolor)
    t.begin_fill()
    t.pensize(pensize)
    t.circle(radius, 180)
    t.end_fill()
    t.setheading(0)
    t.pu()


background()
rectangle(-500, -400, 1000, 180, 'grey', 3, 'grey')
circle(-430, 290, 50, '#edebe0', 4, '#EEE8AA')
circle(-435, 35, 15, 'grey', 4, 'grey')
circle(-445, 65, 10, 'grey', 4, 'grey')
circle(-455, 85, 8, 'grey', 4, 'grey')
square(-450, -80, 200, '#ffcce6', 1, '#DA70D6')
rectangle(-440, -80, 20, 110, "#241a12", 1, '#241a12')
triangle(-460, -80, 220, '#99bbff', 1, '#87CEEB')
square(-400, -130, 40, 'gold', 2, 'gold')
square(-350, -130, 40, 'gold', 2, 'gold')
square(-400, -180, 40, 'gold', 2, 'gold')
square(-350, -180, 40, 'gold', 2, 'gold')
rectangle(-280, -330, 177, 400, '#f5b880', 1, '#f5b880')
semicircle(-80, 70, 110, '#664d69', 1, '#664d69')
rectangle(-210, -330, 40, 30, "#664d69", 1, '#664d69')
square(-230, 0, 20, 'gold', 2, 'gold')
square(-165, 0, 20, 'gold', 2, 'gold')
square(-230, -60, 20, 'gold', 2, 'gold')
square(-165, -60, 20, 'gold', 2, 'gold')
square(-230, -120, 20, 'gold', 2, 'gold')
square(-165, -120, 20, 'gold', 2, 'gold')
square(-230, -180, 20, 'gold', 2, 'gold')
square(-165, -180, 20, 'gold', 2, 'gold')
square(-230, -240, 20, 'gold', 2, 'gold')
square(-165, -240, 20, 'gold', 2, 'gold')
star(-200, 300, 15, '#f7fc99', 2, '#BDB76B')
star(-400, 210, 20, '#f2ff00', 2, '#BDB76B')

rectangle(-50, -300, 100, 300, 'darksalmon', 3, 'darksalmon')
triangle(-70, 0, 140, 'maroon', 3, 'maroon')
rectangle(30, 40, 10, 50, 'dimgrey', 3, 'dimgrey')
rectangle(-35, -300, 20, 30, 'brown', 3, 'brown')
square(-30, -175, 15, 'gold', 3, 'gold')
square(-30, -125, 15, 'gold', 3, 'gold')
square(-30, -75, 15, 'gold', 3, 'gold')
square(-30, -25, 15, 'gold', 3, 'gold')
rectangle(0, -165, 30, 10, 'brown', 3, 'brown')
square(15, -142, 10, 'gold', 3, 'gold')
rectangle(0, -115, 30, 10, 'brown', 3, 'brown')
square(15, -92, 10, 'gold', 3, 'gold')
rectangle(0, -65, 30, 10, 'brown', 3, 'brown')
square(15, -42, 10, 'gold', 3, 'gold')
rectangle(15, -350, 150, 90, 'tan', 3, 'tan')
rectangle(15, -350, 150, 90, 'tan', 3, 'tan')
semicircle(180, -260, 90, 'darkkhaki', 3, 'darkkhaki')
rectangle(70, -350, 40, 30, 'olive', 3, 'olive')
rectangle(35, -300, 10, 30, 'gold', 3, 'gold')
rectangle(135, -300, 10, 30, 'gold', 3, 'gold')
rectangle(75, -300, 30, 10, 'gold', 3, 'gold')
rectangle(75, -280, 30, 10, 'gold', 3, 'gold')
star(-50, 200, 25, 'lightyellow', 3, 'beige')
star(0, 350, 15, 'oldlace', 3, 'beige')
star(150, 250, 10, '#f7fc99', 3, '#BDB76B')

rectangle(200, -340, 200, 400, '#DEB887', 3, '#DEB887')
triangle(182, 50, 240, '#A0522D', 1, '#A0522D')
square(345, -225, 30, 'gold', 3, '#8B4513')
square(295, -175, 30, 'gold', 3, '#8B4513')
square(245, -125, 30, 'gold', 3, '#8B4513')
square(325, -25, 30, 'gold', 3, '#8B4513')
square(275, 25, 30, 'gold', 3, '#8B4513')
rectangle(220, -340, 25, 70, '#8B4513', 3, '#8B4513')
rectangle(340, -350, 150, 250, '#87CEEB', 3, '#87CEEB')
semicircle(495, -100, 80, '#4169E1', 3, '#4169E1')
rectangle(350, -350, 30, 60, '#4169E1', 3, '#4169E1')
square(393, -225, 50, 'gold', 3, '#4169E1')
square(393, -160, 50, 'gold', 3, '#4169E1')
star(270, 350, 15, 'oldlace', 3, 'beige')
star(400, 250, 10, '#f7fc99', 3, '#BDB76B')

t.mainloop()
