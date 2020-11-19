from gui import *
from num_books import num_books
from num_pages import num_pages
from ranking_categories import ranking_categories
from ranking_books import ranking_books
from ranking_pages import ranking_pages

def main():
    print("\033[1;31;1m \t\t\t Monthly Report of the Reading Group.\n \033[1;;1m\tPlease Select Your Choice:\n \033[1;32;1m1 \t For Number of books read by the whole group members. \n \033[1;33;1m2 \t For Number of pages read by the whole group members. \n \033[1;34;1m3 \t For Ranking of books categories mostly read by the group members. \n \033[1;35;1m4 \t For Ranking of group members based on number of books read. \n \033[1;36;1m5 \t For Ranking of group members based on number of pages read. \n \033[1;31;1m0 \t To Exit")
    while True:
        selection = input("\033[1;37;1mEnter Your Choice: ")
        root.mainloop()
        if selection == '1':
            num_books()
        elif selection == '2':
            num_pages()
        elif selection == '3':
            ranking_categories('Sort')
        elif selection == '4':
            ranking_books('Sort')
        elif selection == '5':
            ranking_pages('Sort')

        elif selection != '1' or '2' or '3' or '4' or '5':
            if selection == '0':
                break
            else:
                print("\033[1;31mInvalid Choice!,\033[;1m Please Enter a Correct Choice")
main()
