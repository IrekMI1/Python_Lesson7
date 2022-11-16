import view
import storage

def start_phonebook():
    while True:
        working_mode = view.get_mode()
        if working_mode == 'w':
            info = view.get_input_data()
            storage.record_data(info)
            print('Данные записаны.')
        elif working_mode == 'f':
            first_name = view.get_input_first_name()
            info = storage.search_data(first_name)
            view.print_info(info)
        elif working_mode == 'q':
            break