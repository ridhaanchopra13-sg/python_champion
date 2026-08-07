class book:
    def __init__(self,setting_title, author, is_borrowed):
        self.setting_title = setting_title
        self.author = author
        self.is_borrowed = is_borrowed
    def borrow(self):
        self.is_borrowed = True
        print("Yes this is a confirmation statement")
    def return_book(self):
        self.is_borrowed = False
        print("Yes this is a confirmation statement")