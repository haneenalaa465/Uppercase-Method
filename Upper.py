class MyString(str):
    def Upper(self):
        result = ""
        for char in self:
            ascii_code = ord(char)
            if 97 <= ascii_code <= 122:
                result += chr(ascii_code - 32)
            else:
                result += char
        return result

my_string = MyString("Haneeeen Alaa")
print(my_string.Upper()) 
