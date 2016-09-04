"""Program description"""
text = "this is a collection of words of nice words this is a fun thing it is"
dict1 ={}
words =  text.split()
words_sorted = []

for element in words:
    dict1[element] = 0

for element in words:
    if element in dict1:
        dict1[element] += 1
# print (dict1)

for key in dict1:
    words_sorted.append(key)

words_sorted.sort()

print(words_sorted)

for element in words_sorted:
    print(element,":",dict1[element])
