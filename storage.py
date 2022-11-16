import export

global phonebook
phonebook = []

def record_data(data):
    phonebook.append(data)
    export.export_to_cvs(data)
    export.export_to_txt(data)


def search_data(firstname):
    for person in phonebook:
        if person[0] == firstname:
            return person
    return 'not found'