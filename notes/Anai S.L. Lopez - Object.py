class NoteBook(object):
    def __init__(self, cover_title, color):
        self.pages = 4
        self.cover = True
        self.cover_title = cover_title
<<<<<<< HEAD
        self.equipped = True
=======
        self.color = color
        self.closed = True
>>>>>>> 60c788df8b2a781224c7f943279a11b5e29cb442

    def rip_page(self):
        print("RIP!!")
        print("You rip out out a page from your note book.")
        self.pages = self.pages - 1
        print(self.pages)

<<<<<<< HEAD
=======
    def write_entry(self,):
        if self.pages == 0:
            print("You can't write an entry.")
            print("You have no more pages to write on.")
            return
        elif self.pages > 0:
            entry = input("Write your entry: ")
            print(entry)
            return

>>>>>>> 60c788df8b2a781224c7f943279a11b5e29cb442
    def rip_cover(self):
        print("RIP!!!")
        print("You have ripped the cover of your note book.")
        self.cover = False

<<<<<<< HEAD
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
=======
    def open_book(self):
        command = input("Open book? ")
        if command.lower() in ["no"]:
            self.closed = True
        elif command.upper() in ["yes"]:
            self.closed = False
            print("You have open the book!")


my_book = NoteBook("Book1", "Blue")

my_book.rip_page()
my_book.open_book()
>>>>>>> 60c788df8b2a781224c7f943279a11b5e29cb442
