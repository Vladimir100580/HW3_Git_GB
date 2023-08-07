# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.


def print_operation_table(operation, num_rows=7, num_columns=7):
    for n in range(1, num_rows + 1):
        for m in range(1, num_columns + 1):
            print(operation(n, m), end='  ')
        print()

print_operation_table(lambda x, y: x * y)
# Ну, прям, очень крутая программа
