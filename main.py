import matplotlib.pyplot as plt
import numpy as np

def generate_graph(equation_to_generate, type_of_graph_to_generate):

    equation_to_generate = equation_to_generate.split(" ")

    if type_of_graph_to_generate == 1:
        x_coefficient = int((equation_to_generate[0])[0])
        list_of_y = []

        # Generation of y points
        if equation_to_generate[1] == "+":
            for i in range(0, 21, 1):
                list_of_y.append(x_coefficient*i + int(equation_to_generate[-1]))

        elif equation_to_generate[1] == "-":
            for i in range(0, 21, 1):
                list_of_y.append(x_coefficient*i - int(equation_to_generate[-1]))
        
        # Plotting of graph
        plt.plot(list_of_y) 
        plt.show()

    elif type_of_graph_to_generate == 2:
        x_coefficient_1 = int((equation_to_generate[0])[0])
        x_coefficient_2 = int((equation_to_generate[2])[0])
        list_of_y = []

        # Generation of y points
        if equation_to_generate[1] == "+" and equation_to_generate[3] == "-":
            for i in range(0, 21, 1):
                list_of_y.append(x_coefficient_1*i**2 + x_coefficient_2*i - int(equation_to_generate[-1]))

        elif equation_to_generate[1] == "-" and equation_to_generate[3] == "-":
            for i in range(0, 21, 1):
                list_of_y.append(x_coefficient_1*i**2 - x_coefficient_2*i - int(equation_to_generate[-1]))
        
        elif equation_to_generate[1] == "-" and equation_to_generate[3] == "+":
            for i in range(0, 21, 1):
                list_of_y.append(x_coefficient_1*i**2 - x_coefficient_2*i + int(equation_to_generate[-1]))

        elif equation_to_generate[1] == "+" and equation_to_generate[3] == "+":
            for i in range(0, 21, 1):
                list_of_y.append(x_coefficient_1*i**2 + x_coefficient_2*i + int(equation_to_generate[-1]))
        
        # Plotting of graph
        plt.plot(list_of_y) 
        plt.show()


def process_equation(equation, type_of_graph_to_process): # Conducts format check of the graph
    split_equation = equation.split(" ")

    for i in split_equation: # Iteration through split_equation to check for decimal points
        if "." in i:
            print("This program does not accept decimal places")
            return "Equation not accepted!"
    
    if type_of_graph_to_process == 1: # Checking whether there are the right number of coefficients in a linear graph 
        if len(split_equation) == 3:
            return "Equation accepted!"
        else:
            print("Too many or too little coefficients")
            return "Equation not accepted!"

    elif type_of_graph_to_process == 2: # Checking whether there are the right number of coefficients in a quadratic graph
        if len(split_equation) == 5:
            return "Equation accepted!"
        else:
            print("Too many or too little coefficients")
            return "Equation not accepted!"

list_of_graphs = {1: "Linear",
                  2: "Quadratic"}

type_of_graph = 0

while not (type_of_graph == 1 or type_of_graph == 2): # Equality check for validation of data
    try:
        type_of_graph = int(input("[1] Linear\n[2] Quadratic\n Selection: "))
    except:
        print("Please enter an integer")

print(f"{list_of_graphs[type_of_graph]} has been selected")

equation_of_graph = input("Enter equation of graph: y = ")
print(process_equation(equation_of_graph, type_of_graph))

if process_equation(equation_of_graph, type_of_graph) == "Equation accepted!":
    generate_graph(equation_of_graph, type_of_graph)
