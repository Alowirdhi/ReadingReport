def num_pages():
    strPages = 'number of pages'
    total = 0
    with open("inputFile.txt", "r", encoding="utf8") as file:
        for line in file:
            if strPages in line.casefold():
                total += int(line.split()[3])

    file.close()
    print("\033[1;33;1mNumber of Pages read by the group:\033[1;37;1m", total, "Pages")
    return "Number of Pages read by the group: ", total, "Pages"
