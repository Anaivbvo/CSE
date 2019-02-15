class NoteBook(object):
    def __init__(self, cover_title):
        self.pages = 4
        self.cover = True
        self.cover_title = cover_title
        self.entries = True

    def rip_page(self):
        print("RIP!!")
        print("You rip out out a page from your note book.")
        self.pages = self.pages - 1
        print(self.pages)

    def write_entry(self):
        if self.pages == 0:
            print("You can't write an entry.")
            print("You have no more pages to write on.")
            return
        elif self.pages > 0:
            input("Write your entry: ")
            print(input)
            return

    def rip_cover(self):
        print("RIP!!!")
        print("You have ripped the cover of your note book.")
        self.cover = False


my_book = NoteBook("Book1")

my_book.write_entry("Entry #1..")

print(Static.RandomMine.myrandom())
