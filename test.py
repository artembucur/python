with open('1.txt', 'r') as my_file:

    line = my_file.readline()
    while line:
        print(line)
        line = my_file.readline()

with open('1.txt', 'a') as my_file:
    name = input('Введите имя:\n')
    my_file.write(f'\n{name}')