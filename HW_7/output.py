def output(contact_: str) -> None:
    with open("telephone_dictionary.csv", "r") as f1:
        for line in f1:
            contact = tuple(line.split(','))
            if contact_ in contact:
                print(', '.join(contact))