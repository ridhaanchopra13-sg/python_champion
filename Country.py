class India:
    def Capital(self):
        print("The capital of india is New Delhi")
    def Language(self):
            print("The most common language in india is Hindi")
    def Type(self):
            print("The type of india is developing")
class USA:
    def Capital(self):
        print("The capital of USA is Washington DC")
    def Language(self):
            print("The most common language in USA is english")
    def Type(self):
            print("The type of USA is developed")
I = India()
U = USA()
for S in(U,I):
    S.Capital()
    S.Language()
    S.Type()