from equation import Equation, graph


def main():

    # User input
    while True:
        try:
            a = int(
                input('What is the "a" value of your equation? (in standard form):\n')
            )
            b = int(input('"b" value? (in standard form):\n'))
            c = int(input('"c" value? (in standard form):\n'))
            break

        except:
            pass

    # Equation class
    equation = Equation((a, b, c))

    standard_form = equation.get_standard_form()
    vertex_form = equation.get_vertex_form()
    a, b, c = equation.values
    x1, x2 = equation.get_zeros()
    x, y = equation.get_vertex()

    print(
        """
    [+] Standard Form = {}\n
    [+] Vertex Form = {}\n
    [+] 1st zero/root = {}\n
    [+] 2nd zero/root = {}\n
    [+] Vertex = {}\n
    [+] AOS: x = {}""".format(
            standard_form, vertex_form, x1, x2, (x, y), x
        )
    )

    graph(equation)


if __name__ == "__main__":
    main()
