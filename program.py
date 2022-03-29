import inspect
from math import sqrt

message = inspect.cleandoc('''Добро пожаловать в самую лучшую 
                              программу для вычисления 
                              квадратного корня из заданного числа''')
message = message.replace("\n","")

def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Непосредственно вычисляет корень из заданного значения,
       если оно НЕ меньше или равно нулю"""
    if your_number <= 0:
        return    
    root = calculate_square_root(your_number)
    answer = inspect.cleandoc(f'''Мы вычислили корень квадратный из 
                               введенного вами числа. Это будет: 
                               {root}''')
    answer = answer.replace("\n","")
    print(answer)


print(message)
calc(25.5)
