def get_input_data():   
    message = [
        'Введите фамилию:  ',
        'Введите имя:      ',
        'Введите номер:    ',
        'Введите описание: '        
        ]
    data = []
    
    for i in range(4):
        data.append(input(message[i]))
    return data


def get_mode():
    mode = '_'
    while mode not in 'wfq':
        mode = input('Выберите действие: w (запись) / f (поиск) / q (выход)\n')
    return mode
     

def get_input_first_name():
    return input('Введите искомую фамилию: ')


def print_info(data):
    if data != 'not found':
        print(
            f'Результат поиска: \
            \nФамилия:  {data[0]}\
            \nИмя:      {data[1]}\
            \nНомер:    {data[2]}\
            \nОписание: {data[3]}'
            )
    else: print('Фамилия не найдена.')