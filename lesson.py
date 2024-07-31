def calculate(a, b, operand):
    if operand == "+":
        a += b
        print(a)
    elif operand == "-":
        a -= b
        print(a)
    elif operand == "*":
        a *= b
        print(a)
    elif operand == "/":
        a /= b

        print(a)
    else:
        print("Введенная операция не поддерживается. Попробуйте еще раз.")


def assignor(list):
    for i in list:
        a = int(list[0])
        b = int(list[2])
        operand = list[1]
        calculate(a, b, operand)
        break


def conditions(list):
    if len(list) > 3:
        print(
            "Введены неверные данные т.к формат математической операции не удовлетворяет заданию - два операнда и один оператор. Попробуйте еще раз.")
    elif ((float(list[0]) * 10) % 10 > 0) or ((float(list[2]) * 10) % 10 > 0):
        print('Введены дробные числа. Попробуйте еще раз.')
    elif 0 < int(list[0]) > 10:
        print("Калькулятор поддерживает числа от 1 до 10")

    elif 0 < int(list[2]) > 10:
        print("Калькулятор поддерживает числа от 1 до 10")

    else:
        assignor(list)


def main():
    example = ''
    while example != "exit":

        print('', end='\n')
        print(
            "Калькулятор умеет выполнять сложение, вычитание, умножение, деление. Пример записи: а + b, a - b, a * b, a / b. Калькулятор не принимает дробных чисел. Eсли хотите завершить работу програмы напишите 'exit'")
        example = input('Введите пример: ')
        if len(example) < 2:
            print("Т.к. строка не является математической операцией. Попробуйте еще раз.")
        elif example == "exit":
            print("Работа программы завершена.")
            break
        else:
            example = example.split()
            for i in example:
                if "." in example:
                    print("Введено дробное число. Попробуйте заново.")
                    break
                elif len(example) <= 0:
                    print(
                        "Т.к. строка не является математической операцией калькулятор не смог ее выполнить. Попробуйте заново.")
                    break
                else:
                    conditions(example)
                    break


main()