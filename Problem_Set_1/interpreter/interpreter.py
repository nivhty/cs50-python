expression = input("Expression: ")
x, operator, y = expression.split(" ")
x = float(x)
y = float(y)

if operator == '+':
    answer = x + y
elif operator == '-':
    answer = x - y
elif operator == '*':
    answer = x * y
elif operator == '/':
    answer = round(x / y,1)
else:
    print('Invalid syntax')

print(f"{answer:1}")
