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


def triangle():
    """
    TODO: Ksenia
    Function is drawing a triangle.
    :return:
    """
    pass


def star():
    """
    TODO: Nastya
    Function is drawing a star.
    :return:
    """
    t.pendown()
    t. speed(0)
    t.pensize(2)
    t.color('pink')
    for i in range(250):
        for colours in ['red', 'blue']:
            t.color(colours)
            t.forward(2*i)
            t.left(150)
    t.forward(500)
    t.exitonclick()


