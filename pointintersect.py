import matplotlib.pyplot as plt
import numpy as np

#def cruzreta(c1, p1, c2, p2):
# reta r: y = a1x + b1
# reta s: y = a2x + b2
# o ponto de intersecao por exemplo quando yr = ys
# yr = ys
# a1x + b1 = a2x + b2
# (a1 - a2)x = (b2 - b1)
# x = (b2 - b1)/(a1 - a2)
# y = a1x + b1 = a1( (b2 - b1)/(a1 - a2) ) + b1
# y = (a1.b2 - b1.a2)(a1 - a2)
# function [cr] = cruzreta(xc1,yc1,xp1,yp1,xc2,yc2,xp2,yp2) 

#c1 = [2.1, 1.2];
#c2 = [1.2, 2.1];
#p1 = [0.1, 1.2];
#p2 = [1.3, 0.];

# creating an empty list
c1 = []
c2 = []
p1 = []
p2 = []

# number of elements as input
n = 2

# iterating till the range
for i in range(0, n):
	ele = float(input("Digite os valores de x e y para C1: "))

	c1.append(ele) # adding the element

# iterating till the range
for i in range(0, n):
	ele = float(input("Digite os valores de x e y para C2: "))

	c2.append(ele) # adding the element

# iterating till the range
for i in range(0, n):
	ele = float(input("Digite os valores de x e y para P1: "))

	p1.append(ele) # adding the element

# iterating till the range
for i in range(0, n):
	ele = float(input("Digite os valores de x e y para P2: "))

	p2.append(ele) # adding the element

xc1 = c1[0]; yc1 = c1[1];
xp1 = p1[0]; yp1 = p1[1];

xc2 = c2[0]; yc2 = c2[1];
xp2 = p2[0]; yp2 = p2[1];

r1 = [c1, p1]
r2 = [c2, p2]

horiz = input('nome do eixo na horizontal:   ' + 's');
vert = input('nome do eixo vertical:   ' + 's');

mr1 = (yp1 - yc1) / (xp1 - xc1) # coeficiente angular de r1
mr2 = (yp2 - yc2) / (xp2 - xc2) # coeficiente angular de r2

br1 = -1 * (mr1 * xc1 - yc1) # coeficiente linear de r1
br2 = -1 * (mr2 * xc2 - yc2) # coeficiente linear de r2

# br1 = yc1 - mr1*xc1 # coeficiente linear de r1
# br2 = yc2 - mr2*xc2 # coeficiente linear de r2

# y - yc1 = mr1(x - xc1) equa�ao da reta 1
# y - yc2 = mr2(x - xc2) equa�ao da reta 2

x = (-(mr2*xc2) + yc2 + (mr1*xc1) - yc1) / (mr1 - mr2); # x do cruzamento
y = (mr1*x)  - (mr1*xc1) + yc1; # y do cruzamento

plt.plot(c1, p1, "-b", label="r1")
plt.plot(c2, p2, "-r", label="r2")
plt.plot(x,y,'+g')
plt.xlabel(horiz)
plt.ylabel(vert)
plt.legend(loc="upper left")
print("As linhas se cruzam nos pontos x e y abaixo:")
print(x)
print(y)