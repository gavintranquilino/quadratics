import math
import matplotlib.pyplot as plt

VALUES = (2, 17, -84) # Change these values as the (a, b, c) values
# a, b, c

class Equation(object):
    def __init__(self):
        self.values = VALUES

    def get_zeros(self):
        a, b, c = self.values
        x = (b**2) - (4*a*c)

        x1 = (-b + math.sqrt(x)) / (2*a)
        x2 = (-b - math.sqrt(x)) / (2*a)

        return x1, x2

    def get_vertex(self):
        a, b, c = self.values

        x = (-b) / (2*a)

        y = (a*(x**2)) + (b*x) + c

        return x, y
    
    def get_standard(self):
        a, b, c = self.values

        return '{}x^2 + {}x + {}'.format(a, b, c)
    
def graph(equation):
    a, b, c = equation.values
    r1, r2 = equation.get_zeros()

    if r1 < r2:
        x = r1
        y = r2

    else:
        x = r2
        y = r1

    roots1 = []
    roots2 = []

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Set axes
    # ax.spines['left'].set_position('center')
    # ax.spines['bottom'].set_position('zero')

    # ax.spines['right'].set_color('none') # remove vertical box line
    # ax.spines['top'].set_color('none') # remove horizontal box line

    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')

    while x < y:
        base = float((a*(x**2)) + (b*x) + c)

        roots1.append(x)
        roots2.append(base)
        x += 0.0001

    plt.plot(roots1, roots2, 'g')
    plt.show()

def main():
    equation = Equation()

    standard_form = equation.get_standard()
    a, b, c = equation.values
    x1, x2 = equation.get_zeros()
    x, y = equation.get_vertex()

    print('\nStandard Form = {}\n\nx = {} and x = {}\n\nVertex = {}\n\nAOS: x = {}\n'.format(standard_form, x1, x2, (x, y), x))

    graph(equation)

if __name__ == '__main__':
    main()
    # TODO find all factors
