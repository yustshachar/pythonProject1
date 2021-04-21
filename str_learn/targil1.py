word=input("enter word: ")
word_new=""
for i in word:
    if i.upper()!="A":
        word_new=word_new+i
print(word_new)