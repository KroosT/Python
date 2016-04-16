inp = raw_input('>>>Hello! Type the command with "space" please: ')
mas = inp.split()
commands = ['add', 'remove', 'list', 'find', 'quit', 'exit']
lst = set()
flag = 0
while not flag:

    null_flag = 0

    if len(mas) == 0:
        null_flag = 1

    if not null_flag:
        count = 0
        for c in commands:
            if mas[0] == c:
                count += 1
        if count == 0:
            print '>>>There is no such command! Please, retype: '

        if mas[0] == 'exit' or mas[0] == 'quit':
            break

        if mas[0] == 'add':
            lst.update(mas[1:])

        if mas[0] == 'remove':
            if len(mas) != 2:
                print '>>>Command "remove" has only 1 argument, please retry!'
            else:
                lst.difference_update(mas[1:])

        if mas[0] == 'find':
            for x in mas[1:]:
                if x in lst:
                    print '>>>Element {} is in the set!'.format(x)
                else:
                    print '>>>Element {} is not in the set!'.format(x)

        if mas[0] == 'list':
            for x in lst:
                print '{}'.format(x)

    inp = raw_input('>>>')
    mas = inp.split()

print '>>>Good Bye'
