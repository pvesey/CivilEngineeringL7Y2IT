import math as m


A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0




print(' --------------')
print(' --- PAGE 1 ---')
print(' --------------')
## First Image

b = 0.35
h = 0.15


A = (b*h)/2
Xc = (2*b)/3
Yc = h/3

Ixc = (b*(h**3))/36

Iyc = (h*(b**3))/36 

Ic = (b*(h**3))/12

Iy = (h*(b**3))/4


#print(A, Xc, Yc, Ixc, Iyc, Ic, Iy)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ixc:\t', Ixc)
print('Iyc:\t', Iyc)
print('Ic:\t', Ic)
print('Iy:\t', Iy)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0

## Second Image
b = 0.7
h = 0.2


A = (b*h)/2
Xc = b/3
Yc = h/3

Ixc = (b*(h**3))/36

Iyc = (h*(b**3))/36 

Ic = (b*(h**3))/12

Iy = (h*(b**3))/12

# print(A, Xc, Yc, Ixc, Iyc, Ic, Iy)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ixc:\t', Ixc)
print('Iyc:\t', Iyc)
print('Ic:\t', Ic)
print('Iy:\t', Iy)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0

# Third Image

a = 1.5
b = 2.2
h = 1.5


A = (b*h)/2
Xc = (a+ b)/3
Yc = h/3

Ixc = (b*(h**3))/36

Iyc = ((b*h)*((b**2) -(a*b) + (a**2)))/36

Ic = (b*(h**3))/12

Iy = ((b*h)*((b**2) +(a*b) + (a**2)))/12

# print(A, Xc, Yc, Ixc, Iyc, Ic, Iy)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ixc:\t', Ixc)
print('Iyc:\t', Iyc)
print('Ic:\t', Ic)
print('Iy:\t', Iy)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0

#Fourth Figure

b = 3.0
h = 5.0


A = (b*h)
Xc = b/2
Yc = h/2

Ixc = (b*(h**3))/12

Iyc = (h*(b**3))/12 

Ic = (b*(h**3))/3

Iy = (h*(b**3))/3

J = ((b*h)*((b**2) + (h**2)))/12

# print(A, Xc, Yc, Ixc, Iyc, Ic, Iy, J)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ixc:\t', Ixc)
print('Iyc:\t', Iyc)
print('Ic:\t', Ic)
print('Iy:\t', Iy)
print('J:\t', J)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0

# Fifth Figure

a = 1.5
b = 2.5
theta = m.radians(45) 

A = a * b * m.sin(theta)
Xc = (b + (a*m.cos(theta)))/2
Yc = (a * m.sin(theta))/2

Ixc = (a**3 *b * (m.sin(theta)**3))/12
Iyc = (a*b*m.sin(theta)*(b**2 + (a**2*m.cos(theta)**2)))/12

Ix = (a**3 *b * (m.sin(theta)**3))/3
Iy = (((a*b*m.sin(theta))*((b + (a*m.cos(theta)))**2))/3) - ((a**2 * b**2 * m.sin(theta)* m.cos(theta))/6)
print('CORRECTION')
print(Iy)
print('CORRECTION')

# ab Sin(theta)
FirstPart = ((a*b*m.sin(theta)) * (b+(a *m.sin(theta)))**2)/3
SecondPart = (a**2 * b**2 * m.sin(theta) * m.cos(theta))/6

Iy = FirstPart - SecondPart 

# print(A, Xc, Yc, Ixc, Iyc, Ic, Iy)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ixc:\t', Ixc)
print('Iyc:\t', Iyc)
print('Ix:\t', Ix)
print('Iy:\t', Iy)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0


#PAGE 2 Circle Stuff
print(' --------------')
print(' --- PAGE 2 ---')
print(' --------------')

## First Image
a = 1.2

A = m.pi*a**2
Xc = a
Yc = a

Ixc = (m.pi*a**4)/4

Iyc = (m.pi*a**4)/4 

Ic = (5*m.pi*a**4)/4

Iy = (5*m.pi*a**4)/4

J = (m.pi*a**4)/2
##### TESTS TEST TEST
# print(A, Xc, Yc, Ixc, Iyc, Ic, Iy, J)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ixc:\t', Ixc)
print('Iyc:\t', Iyc)
print('Ic:\t', Ic)
print('Iy:\t', Iy)
print('J:\t', J)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0

## Second Image
a = 3.1
b= 3.0

A = m.pi*(a**2 - b**2)
Xc = a
Yc = a

Ixc = (m.pi*(a**4 - b**4))/4

Iyc = (m.pi*(a**4 - b**4))/4 

Ic = ((5*m.pi*a**4)/4) - (m.pi*a**2*b**2) - ((m.pi*b**4)/4) 

Iy = ((5*m.pi*a**4)/4) - (m.pi*a**2*b**2) - ((m.pi*b**4)/4)

J = (m.pi*(a**4-b**4))/2

# print(A, Xc, Yc, Ixc, Iyc, Ic, Iy, J)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ixc:\t', Ixc)
print('Iyc:\t', Iyc)
print('Ic:\t', Ic)
print('Iy:\t', Iy)
print('J:\t', J)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0

## Third Image
a = 0.75


A = (m.pi*a**2)/2
Xc = a
Yc = (4*a)/(3*m.pi)

Ixc = (a**4*(9*m.pi**2 - 64))/(72*m.pi)

Iyc = (m.pi*a**4)/8 

Ic = (m.pi*a**4)/8 

Iy = (5*m.pi*a**4)/8


# print(A, Xc, Yc, Ixc, Iyc, Ic, Iy)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ixc:\t', Ixc)
print('Iyc:\t', Iyc)
print('Ic:\t', Ic)
print('Iy:\t', Iy)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0



## Fourth Image
a = 0.6
theta = m.radians(30)

A = a**2*theta
Xc = ((2*a)/3)*(m.sin(theta)/theta)
Yc = 0

Ic = (a**4*(theta - m.sin(theta)*m.cos(theta)))/4 

Iy = (a**4*(theta + m.sin(theta)*m.cos(theta)))/4


# print(A, Xc, Yc, Ic, Iy)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ic:\t', Ic)
print('Iy:\t', Iy)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0


## Fifth Image
a = 0.45
theta = m.radians(17.5)

A = a**2*(theta - (m.sin(2*theta)/2))

Xc = ((2*a)/3)*((m.sin(theta)**3)/(theta - (m.sin(theta)*m.cos(theta))))

Yc = 0

Ix = ((A*a**2)/4)*(1-((2*(m.sin(theta))**3*m.cos(theta))/((3*theta)-(3*m.sin(theta)*m.cos(theta))))) 

##
##  Q * [1- R/S]
##

Q = (A*a**2)/4
R = 2 * (m.sin(theta)**3) * m.cos(theta)
S = (3*theta) - (3 * m.sin(theta) * m.cos(theta))
IxRework = Q * (1 - (R/S))


Iy = (A*a**2/4)*(1-((2*m.sin(theta)**3*m.cos(theta))/((theta)-(3*m.sin(theta)*m.cos(theta))))) 

# print(A, Xc, Yc, Ic, Iy)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ix:\t', Ix)
print('IxRework:\t', IxRework)
print('1.39--10-5')
print('Iy:\t', Iy)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0

#SHEET 3
#Diagram 1
print(' --------------')
print(' --- PAGE 3 ---')
print(' --------------')

a = 1.4
b = 0.15

A = (4*a*b)/3
Xc = (3*a)/5
Yc = 0

Ixc = (4*a*b**3)/15

Iyc = (16*a**3*b)/175

Ix = Ixc

Iy = (4*a**3*b)/7

# print(A, Xc, Yc, Ixc, Iyc, Ix, Iy)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ixc:\t', Ixc)
print('Iyc:\t', Iyc)
print('Ix:\t', Ix)
print('Iy:\t', Iy)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0




#  Diagram 2

a = 2.75
b = 0.35

A = (2*a*b)/3
Xc = (3*a)/5
Yc = (3*b)/8

Ix = (2*a*b**3)/15

Iy = (2*a**3*b)/7

# print(A, Xc, Yc, Ix, Iy)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ix:\t', Ix)
print('Iy:\t', Iy)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0




# Diagram 3


b = 2.50
h = 0.75
n = 2


A = (b*h)/(n+1)
Xc = ((n+1)/(n+2))*b
Yc = (h/2)*((n+1)/(2*n+1))

Ix = (b*h**3)/(3*((3*n) +1))

Iy = (h*b**3)/(n+3)


# print(A, Xc, Yc, Ix, Iy)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ix:\t', Ix)
print('Iy:\t', Iy)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0


# Diagram 4


b = 2.50
h = 1.50
n = 2.0


A = ((n)/(n+1))*(b*h)
Xc = ((n+1)/(2*n+1))*b
Yc = ((n+1)/(2*(n+2)))*h

Ix = ((n)/(3*(n+3)))*b*h**3

Iy = ((n)/(3*n+1))*b**3*h

# print(A, Xc, Yc, Ix, Iy)
print(' --------------')
print('A:\t', A)
print('Xc:\t', Xc)
print('Yc:\t', Yc)
print('Ix:\t', Ix)
print('Iy:\t', Iy)
print(' --------------')
A = Xc = Yc = Ixc = Iyc = Ic = Iy = Ix = J = 0

