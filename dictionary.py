# Made with love - Akash Singh ♥️
import json

data=json.load(open("dataset.json"))
#print(type(data))
def translate(word):
    return data[word]

word=input("Enter the word to find it's meaning:")
l=translate(word)
print("'"+word.upper()+"' :")
for i in l:
    print(i)