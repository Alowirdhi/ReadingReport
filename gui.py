from tkinter import *
from graphs import *
from num_books import num_books
from num_pages import num_pages
from ranking_categories import ranking_categories
from ranking_books import ranking_books
from ranking_pages import ranking_pages

root = Tk()
root.title('Reading Report')
root.iconbitmap('icon.ico')
root.geometry("1650x600")

option = StringVar()
option.set("Show the Number of books read by the whole group members")

r1 = Radiobutton(root, text="Show the Number of books read by the whole group members",font='bold', value=1, variable=option)
r1.pack()

r2 = Radiobutton(root, text="Show the Number of pages read by the whole group members",font='bold', value=2, variable=option)
r2.pack()

r3 = Radiobutton(root, text="Show the Ranking of books categories mostly read by the group members",font='bold', value=3, variable=option)
r3.pack()

r4 = Radiobutton(root, text=" Show the Ranking of group members based on number of books read",font='bold', value=4, variable=option)
r4.pack()

r5 = Radiobutton(root, text="Show the Ranking of group members based on number of pages read",font='bold', value=5, variable=option)
r5.pack()

def clicked(value):
    if value == '1':
        myLabel = Label(root, text=num_books(),foreground="blue")
        myLabel.pack()
    elif value == '2':
        myLabel = Label(root, text=num_pages(),foreground="green")
        myLabel.pack()
    elif value == '3':
        myLabel = Label(root, text=ranking_categories('label'),foreground="cyan4")
        myLabel.pack()
    elif value == '4':
        myLabel = Label(root, text=ranking_books('label'),foreground="purple")
        myLabel.pack()

    else:
        myLabel = Label(root, text=ranking_pages('label'),foreground="gold4")
        myLabel.pack()

def graphs(value):
    if value == '3':
        categories_graph()
    elif value == '4':
        books_graph()
    elif value == '5':
        pages_graph()

resultButton = Button(root, text="Show Result",bg='snow3', font='bold', command=lambda: clicked(option.get()))
resultButton.pack()

graph_button = Button(root, text="Show Graph",bg='snow4', font='bold', command=lambda: graphs((option.get())))
graph_button.pack()

quit_button = Button(root, text="Exit !",bg="red",font='bold', command=exit)
quit_button.pack()

mainloop()
