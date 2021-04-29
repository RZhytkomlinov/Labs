class Book():

    list_of_books = []

    def __init__(self, title_inp, author_inp, date_inp, rate_inp):
        self.title = title_inp
        self.author = author_inp
        self.date = date_inp
        self.rate = rate_inp


    def __repr__(self):
        rep = 'Book(' + self.title + ',' + str(self.author) + ',' + str(self.date) + ',' + str(self.rate) +  ')'
        return rep

    def sortowaned(self):
        return sorted(Book.list_of_books, key= lambda Book: Book.title)

    def read(self):
        print (f"Czytam książkę {self.title}")


if __name__ == '__main__':
    inp = int(input("Podaj ile książek chcesz dodać do listy: "))
    for i in range (0,inp):
        i += 1
        title_inp = str(input("Podaj title książki:"))
        author_inp = str(input("Podaj author książki:"))
        date_inp = str(input("Podaj date książki:"))
        rate_inp = str(input("Podaj rate książki:"))
        Book.list_of_books.append(Book(title_inp, author_inp,date_inp,rate_inp))
    print(Book.list_of_books[0].sortowaned())