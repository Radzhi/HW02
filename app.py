"""Программа тест для инженера заправщика картриджей"""

# Необходимые переменные
right_answers = 0

# Сперва программа здоровается и предлагает начать
print('Привет! Тебе необходимо пройти тест. \nЕсли ты ответишь на все вопросы, ты получить работу')
print('Напиши свое имя и нажми Enter, чтобы начать')

# Пользователь вводит свое имя
user_name = input('=> ')
print(f'{20 * "-"} \nПривет {user_name}. Тебе нужно угадать бренд компании по модели картриджа')

# Первый вопрос
print('Тест 1: Картридж Q2612A')
user_input = input('Ваш ответ: ').upper()
if user_input == 'HP':
    print('Верно. Это HP')
    right_answers += 1
else:
    print('Неверно. Это HP')

# Второй вопрос
print('Тест 1: Картридж D101S')
user_input = input('Ваш ответ: ').upper()
if user_input == 'SAMSUNG':
    print('Верно. Это SAMSUNG')
    right_answers += 1
else:
    print('Неверно. Это SAMSUNG')

# Третий вопрос
print('Тест 1: Картридж TK-1140')
user_input = input('Ваш ответ: ').upper()
if user_input == 'KYOCERA':
    print('Верно. Это KYOCERA')
    right_answers += 1
else:
    print('Неверно. Это KYOCERA')

# Подведение итогов и вывод статистики
print(f'{20 * "-"} \nТест завершен. Ты ответил на {right_answers} вопроса из 3')
if right_answers == 3:
    print(f'Это {round(right_answers / 3 * 100)}%. Ты принят на работу {user_name}.')
else:
    print(f'Это {round(right_answers / 3 * 100)}%. Ты идешь работать дворником')
