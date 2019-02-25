class NoteBook(object):
    def __init__(self, cover_title, color):
        self.pages = 4
        self.cover = True
        self.cover_title = cover_title
        self.color = color
        self.closed = True

    def rip_page(self):
        print("RIP!!")
        print("You rip out out a page from your note book.")
        self.pages = self.pages - 1
        print(self.pages)

    def write_entry(self,):
        if self.pages == 0:
            print("You can't write an entry.")
            print("You have no more pages to write on.")
            return
        elif self.pages > 0:
            entry = input("Write your entry: ")
            print(entry)
            return

    def rip_cover(self):
        print("RIP!!!")
        print("You have ripped the cover of your note book.")
        self.cover = False

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
