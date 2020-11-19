def num_books():
    counter = 0
    strBooks = 'book'
    with open("inputFile.txt", "r", encoding="utf8") as file:
        for line in file:
            if strBooks in line.casefold():
                counter += 1
                if 'Title' in line:
                    counter -= 1

    file.close()
    print("\033[1;32;1mNumber of Books Read by the group:\033[1;37;1m", counter)
    return "Number of Books Read by the group: ", counter
