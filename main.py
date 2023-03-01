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
    t.goto(-500, 400)
    t.pd()
    t.fd(1000)
    t.rt(90)
    t.fd(800)
    t.rt(90)
    t.fd(1000)
    t.rt(90)
    t.fd(800)
    t.done()


background()


def triangle(x, y, a, c, angle1, fillcolour, pensize, pencolor):
    """
    TODO: Ksenia
    Function is drawing an isosceles triangle. #равнобедренный треугольник
    :param x: first coordinate of the start of drawing triangle
    :param y: last coordinate of the start of drawing triangle
    :param a: lenght of the side of the triangle, other side (b) is equal
    :param c: length of the base of the triangle
    :param angle1: an angle between sides a and b. other two angles (angle2, angle3) are same and equal = (180-angle1)/2 #угол между равными сторонами
    :param fillcolour: triangle fill colour #цвет заливки треугольника
    :param pensize: contour width
    :param pencolor: colour of the contour
    :return:
    """
    pass


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
    t.pd()
    t.speed(0)
    t.pensize(2)
    t.color('pink')
    for i in range(250):
        for colours in ['red', 'blue']:
            t.color(colours)
            t.fd(2*i)
            t.lt(150)
    t.fd(500)
    t.done()


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
    pass


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
    pass


def rectangle(x, y, a, b, fillcolour, pensize, pencolour):
    """
    TODO: Ksenia
    Function is drawing a rectangle.
    :param x: first coordinate of the start of drawing rectangle
    :param y: second coordinate of the start of drawing rectangle
    :param a: length of the longer side
    :param b: length of the shorter side
    :param fillcolour: rectangle fill colour
    :param pensize: contour width
    :param pencolour: colour of the contour
    :return:
    """
    pass




