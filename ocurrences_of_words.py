"""Program description"""
words=[]
word =""
text = input("Enter text")
for character in text:
    if character != " ":
        word += character
    else:
        words.append(word)
        word = ""
print(words)
