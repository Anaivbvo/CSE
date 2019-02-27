class NoteBook(object):
    def __init__(self, cover_title):
        self.pages = 4
        self.cover = True
        self.cover_title = cover_title
        self.equipped = True

    def rip_page(self):
        print("RIP!!")
        print("You rip out out a page from your note book.")
        self.pages = self.pages - 1
        print(self.pages)

    def rip_cover(self):
        print("RIP!!!")
        print("You have ripped the cover of your note book.")
        self.cover = False

    def throw_book(self):
        answer = input("do you want to throw book")
        if answer.lower() is "yes":
            print("Ypu throw the book!")
            print("But it's a nice book, so you retrieve it back.")
        if answer.lower() is "no":
            print("You don't throw the book.")


my_book = NoteBook("Note-book No.1")

my_book.rip_cover()
my_book.rip_page()
my_book.throw_book()
