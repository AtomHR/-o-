def my_salary(sum1, sum2, sum3):
    # sum1 - выроботка в час
    # sum2 - ставка в час
    # sum3 - премия
    a = (sum1 * sum2) + sum3
    return f'Ваша зарплата: {a}'

print(f'{my_salary(int(input("Сколько часов вы проработали? ")), int(input("Какая ставка в час? ")), int(input("Сколько составила премия? ")))}')
