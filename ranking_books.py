import operator

def ranking_books(value):
    result_list = {}
    strInput = open('inputFile.txt', 'r').read()
    counter = strInput.lower().count("member ")
    for i in range(1, counter + 1):
        finalindex = len(strInput)
        FirstIndex = strInput.index("Member " + str(i))
        if i != counter:
            lastIndex = strInput.index("Member " + str(i + 1))
        else:
            lastIndex = finalindex

        newstr = strInput[FirstIndex:lastIndex].lower()
        x = newstr.count("book")
        for lines in newstr.splitlines():
            if "name" in lines:
                name = lines[6:]
                result_list[name] = 1

            if 'title' in lines:
                if "book" in lines:
                    x = x - 1

        result_list.update({name: x})
    sorted_d = dict(sorted(result_list.items(), key=operator.itemgetter(1), reverse=True))

    if value == 'label':
        print('\033[1;35;1mRanking of group members based on number of books read: \033[1;37;1m', sorted_d)
        return "Ranking of group members based on number of books read: ", sorted_d
    elif value == 'names':
        return list(sorted_d.keys())
    elif value == 'numbers':
        return list(sorted_d.values())
    else:
        print('\033[1;35;1mRanking of group members based on number of books read: \033[1;37;1m',sorted_d)
