from random import *
def split(a, b):
    task = ''
    total = []

    for i in a:
        if i != b:
            task += str(i)
        else:
            total.append(task)
            task = ''


    return total

def main(theme):
    hard = 0
    ez = 0
    norm = 0
    totalWrite = ''

    print()
    print('Сколько вариантов:')
    manyVariant = int(input())

    print()
    print('Сколько заданий легкого уровня:')
    ez = int(input())

    print()
    print('Сколько заданий повышенного уровня:')
    norm = int(input())

    print()
    print('Сколько заданий высокого уровня:')
    hard = int(input())

    totalTask1 = []
    totalTask2 = []

    for i in range(manyVariant):

        used = []
        task = []
        answer = []



        for _ in range(ez):

            file1 = split(open('themes/' + theme + '/3.txt', 'rb').readlines()[0].decode(), '!')
            file2 = split(open('answers/' + theme + '/3.txt', 'rb').readlines()[0].decode(), '!')
            index = randint(0, len(file2) - 1)
            if index not in used:
                task.append(file1[index])
                answer.append(file2[index])
                used.append(index)
            else:
                continue

        used = []

        for _ in range(norm):

            file1 = split(open('themes/' + theme + '/4.txt', 'rb').readlines()[0].decode(), '!')
            file2 = split(open('answers/' + theme + '/4.txt', 'rb').readlines()[0].decode(), '!')
            index = randint(0, len(file2) - 1)
            if index not in used:
                task.append(file1[index])
                answer.append(file2[index])
                used.append(index)
            else:
                continue


        used = []

        for _ in range(hard):

            file1 = split(open('themes/' + theme + '/5.txt', 'rb').readlines()[0].decode(), '!')
            file2 = split(open('answers/' + theme + '/5.txt', 'rb').readlines()[0].decode(), '!')
            index = randint(0, len(file2) - 1)
            if index not in used:
                task.append(file1[index])
                answer.append(file2[index])
                used.append(index)
            else:
                continue

        totalTask1.append(task)
        totalTask2.append(answer)

        print(totalTask2)
        print(totalTask1)

    totalWrite1 = ''
    totalWrite2 = ''

    for i in range(len(totalTask1)):
        totalWrite1 += '\n' + str(i + 1) + ' Вариант' + '\n'
        for j in range(len(totalTask1[i])):
            totalWrite1 += str(j + 1) + '.' + str(totalTask1[i][j]) + '\n'

    for i in range(2):
        result = open('result.txt', 'wb')
        result.write(totalWrite1.encode('UTF-8'))
        result.close()

    for i in range(len(totalTask2)):
        totalWrite2 += '\n' + str(i + 1) + ' Вариант' + '\n'
        for j in range(len(totalTask2[i])):
            totalWrite2 += str(j + 1) + '.' + str(totalTask2[i][j]) + '\n'

    for i in range(2):
        answers = open('answers.txt', 'wb')
        answers.write(totalWrite2.encode('UTF-8'))
        answers.close()

while True:
    print('Выберите тему:')
    print()
    print('1. Двоичная арифметика')
    print('2. Перевод из одной системы счисления в другую')
    print('3. Количество информации (текстовые задачи)')
    print('4. Таблицы истинности')
    print('5. Диаграммы Эйлера')
    print('6. Кодирование информации')
    print()
    choiceTheme = int(input('Введите цифру: '))

    if choiceTheme == 1:

        main('2arif')

        break

    elif choiceTheme == 2:

        main('perevodvSS')

        break

    elif choiceTheme == 3:

        main('KolInfo')

        break

    elif choiceTheme == 4:

        main('TabIst')

        break

    elif choiceTheme == 5:

        main('Eiler')

        break

    elif choiceTheme == 6:

        main('KodInfo')

        break