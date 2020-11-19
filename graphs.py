from ranking_books import ranking_books
from ranking_categories import ranking_categories
from ranking_pages import ranking_pages
import numpy as np
import matplotlib.pyplot as plt

def categories_graph():
    categories_list = ranking_categories('plots')
    plt.xlabel('Categories', weight='bold')
    plt.ylabel('Number of Books', weight='bold')
    plt.hist(categories_list)
    plt.show()
    return plt.show()

def books_graph():
    books_list = ranking_books('names')
    numbers = ranking_books('numbers')
    length = np.arange(len(books_list))
    plt.figure(figsize=(18.5, 5))
    plt.xlabel('Members', weight='bold')
    plt.ylabel('Number of Books', weight='bold')
    plt.xticks(length, books_list)
    plt.bar(length, numbers)
    plt.show()
    return plt.show()

def pages_graph():
        pages_list = ranking_pages('names')
        numbers = ranking_pages('numbers')
        length = np.arange(len(pages_list))
        plt.figure(figsize=(18.5, 5))
        plt.xlabel('Members', weight='bold')
        plt.ylabel('Number of Pages', weight='bold')
        plt.xticks(length, pages_list)
        plt.bar(length, numbers)
        plt.show()
        return plt.show()
