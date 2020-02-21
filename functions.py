def triangle(x):
    """
    Print triangle
    """
    b = 1
    while b <= int(x):
        print('#' * b)
        b += 1
    return triangle


def sum_in_string(x):
    """
    На вход функции подаём параметр х - произвольная строка.
    На выходе получаем сумму всех цифр
    """
    s = 0
    for i in x:
        try:
            s += int(i)
        except ValueError:
            continue
    print(s)


def args_sum(*args):
    """
    Функция суммирования произвольного кол-ва аргументов
    """
    s = 0
    for i in args:
        s += i
    return s
