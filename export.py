def export_to_cvs(record):
    with open('phonebook.csv', 'a', encoding='utf-8') as data:
        data.write(';'.join(record) + '\n')


def export_to_txt(record):
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(
            f'\n{record[0]}\
            \n{record[1]}\
            \n{record[2]}\
            \n{record[3]}\n'
            )