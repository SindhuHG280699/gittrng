def show_all_in_dict(dict):
    print('We know the birthdays of:')
    for key in dict:
        print(key)
def search(query, dict):
    return dict[query] if query in dict else None


def main():
    Birthdays = {"Albert Einstein": "15/3/1890",
                 "Benjamin Franklin": "24/12/1995",
                 "Ada Lovelace": "06/06/1998"}
    print('Welcome to the birthday dictionary.')
    show_all_in_dict(Birthdays)
    query = input("Who's birthday do you want to look up?")
    result = Birthdays[query] if query in Birthdays else None
    if result == None:
        print('No Data')
    else:
        print("{}'s birthday is {}".format(query, Birthdays[query]))


if __name__ == "__main__":
    main()