def import_contact(data: str) -> None:
    list_contacts = []
    with open(data, "r") as f1:
        while True:
            line = f1.readline()
            if ',' in line:
                contact = tuple(line.split(','))
                list_contacts.append(contact)
            elif '-' in line:
                contact = tuple(line.split('-'))
                list_contacts.append(contact)
            if not line:
                break
    with open('telephone_dictionary.csv', "a") as f2:
        for contact in list_contacts:
            f2.write(f"{','.join(contact)}")
