""" Part 1: Author class
Create a new class called Author.  Create a regular class, not a dataclass.
An Author has a name, and a list of books published.
When you create a new Author, they don't have any books. So create an empty books list attribute in the __init__ method.
Your Author class should have a publish method, which takes the title of a book as an argument. Add the title of this
book to this object's books list.
Add a __str__ method that returns a String with the author's name, and the names of all of their book's titles.
Write a main function to test your class, create some example authors, and publish some example books. """


class Author:  # defines the author
    def __init__(self, name):
        self.name = name
        self.book_list = []  # empty list

    # this appends the books in the author's list published
    def publish(self, title):
        self.book_list.append(title)

    # This is lists the books names and the author name
    def __str__(self):
        book_list = ', '.join(self.book_list)
        return f'Name: {self.name}. Books Published: {book_list}'
    

def main():  # this is the data information of the author
    cristina = Author("Cristina Garcia")
    cristina.publish("Dreaming in Cuban")
    cristina.publish("Monkey Hunting")

    agatha = Author("Agatha Christie")
    agatha.publish("Murder on the Orient Express")
    agatha.publish("Death on the Nile")

    print(cristina)
    print(agatha)


main()