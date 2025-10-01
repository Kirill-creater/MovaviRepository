def save_result(old_func):
    def new_func(*agrs,**kwargs):
        res = old_func(*agrs,**kwargs)
        with open("result.txt","a",encoding="UTF-8") as out_file:
            print(res,file=out_file)

        return old_func(*agrs,**kwargs)
    return new_func

@save_result
def calculate(a, b, operation='+'):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "ОШИБКА: Деление на ноль."
        return a / b
    elif operation == '**':
        return a ** b
    else:
        print('Указанная операция не распознана.')
        return None

calculate(1, 2)
calculate(2, 2, "-")
calculate(3, 2, "**")