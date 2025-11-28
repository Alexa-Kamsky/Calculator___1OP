from operator import index

expression_User = input("Введите Ваше арифметическое выражение: ")
list_charExpression = []
list_operators = ['+', '-', '*', '/', '(', ')']
i = 0

########    ТОКЕНЕЗАЦИЯ     ############################################################################################
while i < len(expression_User):
    char = expression_User[i]

    if char.isdigit():
        korb_for_2char_number = ""
        while i < len(expression_User) and expression_User[i].isdigit():
            korb_for_2char_number += expression_User[i]
            i += 1
        list_charExpression.append(int(korb_for_2char_number))

    elif char in list_operators:
        list_charExpression.append(char)
        i += 1

    elif char == ' ':
        i += 1
        pass

    else:
        print(f"Вы ввели неккоректное выражение. Ваш корявый символ: {char}")
        i += 1

############    RPN | алгоритм сортировочной станции    ################################################################
operatorPriority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0,
    ')': 0
}

output_list = []
operator_stack = []

def priority(operator):
    return operatorPriority.get(operator, -1)

for token in list_charExpression:
    if isinstance(token, int):
        output_list.append(token)

    elif token == '(':
        operator_stack.append(token)

    elif token == ')':
        while operator_stack and operator_stack[-1] != '(':
            output_list.append(operator_stack.pop())
        if operator_stack and operator_stack[-1] == '(':
            operator_stack.pop()

    elif token in operatorPriority:
        while operator_stack and priority(operator_stack[-1]) >= priority(token):
            output_list.append(operator_stack.pop())
        operator_stack.append(token)

    elif char == ' ':
        pass

while operator_stack:
    output_list.append(operator_stack.pop())

############     Вычисление RPN     ####################################################################################
stack_calc_RPN = []

for token in output_list:
    if isinstance(token, int) or isinstance(token, float):
        stack_calc_RPN.append(token)

    elif token in list_operators:
        right_num = stack_calc_RPN.pop()
        left_num = stack_calc_RPN.pop()

        if token == '+':
            res = left_num + right_num
        elif token == '-':
            res = left_num - right_num
        elif token == '*':
            res = left_num * right_num
        elif token == '/':
            if right_num == 0:
                print("Я делить на ноль не буду, это что такое??? переписывай")
                break
            else:
                res = left_num / right_num

        stack_calc_RPN.append(res)

for i in range(len(stack_calc_RPN)):
    if i == 0:
        print(f"Результат вашего выражения: {stack_calc_RPN[0]}")
    elif i > 0:
        print("Стек не пуст, ошибка в вычислениях RPN")
    else:
       print("Вычисления не завершены. Проверьте, не делили ли вы на ноль?")
