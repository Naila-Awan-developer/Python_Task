
class ReverseString:
    def __init__(self, string):
        self.string = string
        self.index = len(string) -1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= 0:
            char = self.string[self.index]
            self.index -= 1
            return char
        else:
            raise StopIteration

string = "NAILA AWAN"
reverse_string = ReverseString(string)
for char in reverse_string:
    print(char)






