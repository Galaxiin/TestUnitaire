class Calculator:

    def add(x, y):
        return x + y
        
    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
     return x / y
     
    def power(x, y):
        result = 1
        for i in range(y):
            result *= x
        return result
        
    def square_root(value):
        if value == 0 or value == 1:
            return value
        val = value
        precision = 0.0000001
        while abs(val - value / val) > precision:
            val = (val + value / val) / 2
        return val

    def calculate(operation, valueX, valueY):
        if operation == "add":
            result = Calculator.add(valueX, valueY)
        elif operation == "substract":
            result = Calculator.subtract(valueX, valueY)
        elif operation == "multiply":
            result = Calculator.multiply(valueX, valueY)
        elif operation == "divide":
            result = Calculator.divide(valueX, valueY)
        elif operation == "power":
            result = Calculator.power(valueX, valueY)
        elif operation == "square_root":
            result = Calculator.square_root(valueX, valueY)
        return result

# operation = input("Enter the operation you would like to perform (add,
# subtract, multiply, divide, square_root, power): ")

# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the secod number : "))

# print(calculate(operation, num1, num2))