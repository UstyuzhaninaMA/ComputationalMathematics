import math
from matplotlib import pyplot as plt
import func as fn
import accuracy as acc

MaxPowerOfH = 21
ConstantX = 10

ApprFunctions = [acc.formula1, acc.formula2, acc.formula3, acc.formula4, acc.formula5]
Functions = [fn.function1, fn.function2, fn.function3, fn.function4, fn.function5]
DerOfFunctions = [fn.der_of_func1, fn.der_of_func2, fn.der_of_func3, fn.der_of_func4, fn.der_of_func5]
Name = ["sin(x^2)", "cos(sin(x))", "exp(sin(cos(x)))", "ln(x + 3)", "(x + 3) ^ 0,5"]

def h_from_pow(pow):
    return 2 ** (1 - pow)

def dependency(appr_derivative, derivative, function):
    x = []
    y = []
    for i in range(MaxPowerOfH):
        x.append(math.log(h_from_pow(i + 1)))
        y.append(math.log(abs(appr_derivative(ConstantX, h_from_pow(i + 1), function) - 
                    derivative(ConstantX))))
    return x, y

def depend_n_plt_it(appr_derivative, derivative, function, i):
    x, y = dependency(appr_derivative, derivative, function)
    plt.plot(x, y, label = "Use formula " + str(i + 1))

# print(h_from_pow(MaxPowerOfH))
for i in range(len(Functions)):
    plt.figure(figsize=(15, 15))
    for j in range(len(ApprFunctions)):
        depend_n_plt_it(ApprFunctions[j], DerOfFunctions[i], Functions[i], j)
    plt.legend()
    plt.title("Function " + Name[i])
    plt.show()
