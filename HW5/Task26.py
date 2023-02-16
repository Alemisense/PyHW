# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
#

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def production(number, degree):
    if degree == 1:
        return number
    else:
        return (number * production(number, degree - 1))

print()
degree_number = int(input('Введите число: '))
degree_for_number = int(input('Введите степень числа: '))
print()

result = production(number=degree_number, degree=degree_for_number)
print(f'Число {degree_number} в степени {degree_for_number} = {result}')