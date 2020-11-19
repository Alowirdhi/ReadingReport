from collections import Counter

def ranking_categories(value):
    strCategory = 'category'
    counter = Counter()
    with open("inputFile.txt", "r", encoding="utf8") as file:
        for line in file:
            if strCategory in line.casefold():
                line = line.strip().split(":")
                words = line[1].split()
                counter.update(words)

    if value == 'label':
        print('\033[1;34;1mRanking of books categories mostly read by the group members: \033[1;37;1m',counter.most_common())
        return "Ranking of books categories mostly read by the group members: ", counter.most_common()
    elif value == 'plots':
        return list(counter.elements())
    else:
        print('\033[1;34;1mRanking of books categories mostly read by the group members: \033[1;37;1m',counter.most_common())
