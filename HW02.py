"""В первом курсе мы разрабатываем на Python консольное приложение для обучения английскому.
Наша программа по очереди задает вопросы и предлагает вписать пропущенное слово."""

# Необходимые переменные
points = 0  # баллы для начисления
correct_answers = 0  # правильные ответы

# Сперва программа здоровается и предлагает начать:
print('Привет! Предлагаю проверить твои знания английского!')
print('Расскажи, как тебя зовут!')
user_name = input('Твое имя: ')

# Программа считывает имя пользователя и говорит:
print(f'\nПривет {user_name}, начинаем тренировку!')

# Программа задает по очереди три вопроса:
print('\nВопрос 1: My name ___ Vova')  # Первый вопрос
user_input = input('Ваш ответ: ')

# После ввода пользователя приложение проверяет ответ и присваивает баллы:
if user_input == 'is':
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
    points += 10
    correct_answers += 1
else:
    print('Неправильно.')  # Если ответ неверный баллы не начисляются.
    print('Правильный ответ: is')

print('\nВопрос 2: I ___ a coder')  # Второй вопрос
user_input = input('Ваш ответ: ')

if user_input == 'am':
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
    points += 10
    correct_answers += 1
else:
    print('Неправильно.')
    print('Правильный ответ: am')

print('\nВопрос 3: I live ___ Moscow')  # Третий вопрос
user_input = input('Ваш ответ: ')

if user_input == 'in':
    print('Ответ верный!')
    print('Вы получаете 10 баллов!')
    points += 10
    correct_answers += 1
else:
    print('Неправильно.')
    print('Правильный ответ: in')

# Морфологическая коррекция:
if correct_answers == 1:
    question = 'вопрос'
elif correct_answers == 4 or 2:
    question = 'вопроса'
else:
    question = 'вопросов'

# Вывод результатов
print(f'\nВот и все, {user_name}!')
print(f'Ты ответил на {correct_answers} {question} из 3 верно.')
if correct_answers >= 0:
    print(f'Как так {user_name}!')
    print('Тебе с такими знаниями только в спецшколу')
else:
    print(f'Ты заработал {points} баллов.')
    print(f'Это {round(correct_answers * 100 / 3)} процентов.')
