""" Part 2: Author class - no duplicate books
Start with the program from part 1.
In this version, an author can't publish two books with the same name.
When the publish method is called, print an error message if the book given has the same name as a book currently
in the books list. Do not add the duplicate book.
(In other words, make sure the Author object's book list doesn't already contain that name). """


class Author:
    def __init__(self, name):
        self.name = name
        self.book_list = []   # Empty list

    # this makes sure there is no duplicate books
    def publish(self, title):
        if title in self.book_list:
            print('The book has already been published.')
        else:
            self.book_list.append(title)

    # This is lists the books names and the author name
    def __str__(self):
        book_list = ', '.join(self.book_list)
        return f'Name: {self.name}. Books Published: {book_list}'


def main():   # this is the data information of the author
    cristina = Author("Cristina Garcia")
    cristina.publish("Dreaming in Cuban")
    # cristina.publish("Dreaming in Cuban")
    cristina.publish("Monkey Hunting")

    agatha = Author("Agatha Christie")
    agatha.publish("Murder on the Orient Express")
    agatha.publish("Death on the Nile")

    print(cristina)
    print(agatha)


main()
