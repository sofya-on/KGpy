from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import sqrt, cos, pi


def init(a, h, alpha):
    global xrot
    global yrot
    global ambient  # Рассеянное освещение
    global prismcolor
    global lightpos
    global var  # Переменная для изменения цветы с клавиатуры
    global n  # Точность аппроксимации
    global points
    global t
    points = np.array([[0.3875, 0.4, -0.3],
                       [0.6, 0.25, -0.3],
                       [0.675, 0., -0.3],
                       [0.6, -0.25, -0.3],
                       [0.3875, -0.4, -0.3],
                       [0.1125, -0.4, -0.3],
                       [-0.1, -0.25, -0.3],
                       [-0.175, 0., -0.3],
                       [-0.1, 0.25, -0.3],
                       [0.1125, 0.4, -0.3],

                       [0.30375, 0.2, 0.],
                       [0.41, 0.125, 0.],
                       [0.4475, 0., 0.],
                       [0.41, -0.125, 0.],
                       [0.30375, -0.2, 0.],
                       [0.16625, -0.2, 0.],
                       [0.05, -0.125, 0.],
                       [0.0275, 0., 0.],
                       [0.06, 0.125, 0.],
                       [0.16625, 0.2, 0.]])

    t = 0.
    var = 0
    xrot = 0.0
    yrot = 0.0
    ambient = (1.0, 1.0, 1.0, 1)
    prismcolor = (1, 1, 1, 1)
    lightpos = (1.0, 1.0, 1.0)

    glClearColor(0.5, 0.0, 0.5, 1.0)
    gluOrtho2D(-2.5, 2.5, -2.5, 2.5)  # Отдаление от рисунка при открытии окна
    glRotatef(-90, 1.0, 0.0, 0.0)  # Положение рисунка при открытии окна
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # Определяем текущую модель освещения
    glEnable(GL_LIGHTING)  # Включаем освещение
    glEnable(GL_LIGHT0)  # Включаем один источник света
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Определяем положение источника света


# функция обработки специальных клавиш
def specialkeys(key, x, y):
    global xrot
    global yrot
    global var
    if key == GLUT_KEY_UP:
        xrot -= 5.0
    if key == GLUT_KEY_DOWN:
        xrot += 5.0
    if key == GLUT_KEY_LEFT:
        yrot -= 5.0
    if key == GLUT_KEY_RIGHT:
        yrot += 5.0
    if key == GLUT_KEY_F1:
        if var == 1:
            var = 2
        elif var == 2:
            var = 3
        else:
            var = 1
    if key == GLUT_KEY_F2:
        var = 4
    if key == GLUT_KEY_F3:
        var = 5

    glutPostRedisplay()  # Функция перерисовки


def TimeFunction(value):
    global t

    glutPostRedisplay()
    glutTimerFunc(60, TimeFunction, 1)
    t += 0.01 * 2 * pi
    if (t == pi):
        t = 0


# выбор цвета
def choose_color(color):
    if color == 1:
        cl = (1, 0, 0, view)
    if color == 2:
        cl = (1, 1, 1, view)
    if color == 3:
        cl = (1, 1, 0, view)
    if color == 4:
        cl = (0, 0, 0, view)
    return cl


# стороны призмы
def make_sides(p):
    sides = [[p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9]],
             [p[10],p[11],p[12],p[13],p[14],p[15],p[16],p[17],p[18],p[19]],
             [p[0],p[1],p[11],p[10]],
             [p[1],p[2],p[12],p[11]],
             [p[2],p[3],p[13],p[12]],
             [p[3],p[4],p[14],p[13]],
             [p[4],p[5],p[15],p[14]],
             [p[5],p[6],p[16],p[15]],
             [p[6],p[7],p[17],p[16]],
             [p[7],p[8],p[18],p[17]],
             [p[8],p[9],p[19],p[18]],
             [p[9],p[0],p[10],p[19]]]
    return sides


def draw():
    global xrot
    global yrot
    global lightpos
    global prismcolor
    global var
    global points
    global n

    # перерисовка фигуры с изменениями
    if var == 1:
        prismcolor = (0, 0, 0, 0)
    if var == 2:
        prismcolor = (0, 1, 0, 1)
    if var == 3:
        prismcolor = (1, 0, 0, 1)
    if var == 4:
        n = 20
    if var == 5:  # меняем параметры освещения
        glEnable(GL_LIGHT0)
        light0_diffuse = [1.0, 1.0, 1.0];
        light0_direction = [1.0, 1.0, 1.0, 1];
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse);
        glLightfv(GL_LIGHT0, GL_POSITION, light0_direction);

    glClear(GL_COLOR_BUFFER_BIT)  # Очищаем экран и заливаем серым цветом
    glPushMatrix()  # Сохраняем текущее положение "камеры"
    glRotatef(xrot, 1.0, 0.0, 0.0)  # Вращаем по оси X на величину xrot
    glRotatef(yrot, 0.0, 1.0, 0.0)  # Вращаем по оси Y на величину yrot
    if var != 5:
        glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Источник света вращаем вместе с фигурой

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, prismcolor)

    prisms = []
    list_of_points = [points]
    for i in range(len(list_of_points)):
        prisms += [make_sides(list_of_points[i])]

    # построение фигуры
    glBegin(GL_POLYGON)  # берём пустую матрицу точек для добавления туда многоугольников
    glColor3f(0., 0., 0.)
    for q in range(len(prisms)):
        for i in range(len(prisms[q])):
            for j in range(len(prisms[q][i])):  # добавляем точки покоординатно, проходя по всем наборам всех наборов, созданных ранее
                x = prisms[q][i][j][0] + cos(t)
                y = prisms[q][i][j][1]
                z = prisms[q][i][j][2]
                glVertex3f(x, y, z)
    glEnd()

    glPopMatrix()  # Возвращаем сохраненное положение "камеры"
    glutSwapBuffers()  # Выводим все нарисованное в памяти на экран


# сама работа OpenGL
def main(a=1., h=1., alpha=8):
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(523, 150)
    glutInit(sys.argv)
    glutCreateWindow(b"Figure")
    glutDisplayFunc(draw)
    glutSpecialFunc(specialkeys)
    glutTimerFunc(600, TimeFunction, 1)
    init(a, h, alpha)
    glutMainLoop()
main()
