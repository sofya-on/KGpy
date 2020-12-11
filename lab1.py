import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

#выбор цвета
def choose_color(color, view):
	if color == 1:
	    cl = (1, 0, 0, view)
	if color == 2:
		cl = (1, 1, 1, view)
	if color == 3:
		cl = (1, 1, 0, view)
	if color == 4:
		cl = (0, 0, 0, view)
	return cl

#стороны призмы
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
#координаты 
def plot_prism(R, height, color, view):
	points = np.array([[0.55, 1.6, -1.],
					   [1.4, 1., -1.],
					   [1.7, 0., -1.],
					   [1.4, -1., -1.],
					   [0.55, -1.6, -1.],
					   [-0.55, -1.6, -1.],
					   [-1.4, -1., -1.],
					   [-1.7, 0., -1.],
					   [-1.4, 1., -1.],
					   [-0.55, 1.6, -1.],
					   
					   [0.275, 0.8, 0.4],
                                           [0.7, 0.5, 0.4],
					   [0.85, 0., 0.4],
					   [0.7, -0.5, 0.4],
					   [0.275, -0.8, 0.4],
					   [-0.275, -0.8, 0.4],
					   [-0.7, -0.5, 0.4],
					   [-0.85, 0., 0.4],
					   [-0.7, 0.5, 0.4],
					   [-0.275, 0.8, 0.4]])

	points[:, :-1] *= R * 0.5
	points[:, -1] *= height * 0.5#	0.5, т.к. начало координат не в (0,0), а в центре фигуры


	# построение призмы
	fig = plt.figure()
	ax = fig.add_subplot(111, projection="3d")

	prisms = [make_sides(points)]

	for i in range(len(prisms)):
		ax.add_collection3d(Poly3DCollection(prisms[i], linewidths=view, facecolors = choose_color(color, view), edgecolors='k'))

	# настройка графика
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')

	limit = height * 0.5 * 1.2
	plt.xlim([-limit, limit])
	plt.ylim([-limit, limit])
	ax.set_zlim(-limit, limit)

	plt.show()
plot_prism(1., 2., 2, 1)
