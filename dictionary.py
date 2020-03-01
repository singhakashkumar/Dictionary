# Made with love - Akash Singh ♥️
import json

data=json.load(open("dataset.json"))
#print(type(data))
def translate(word):
    #if word in data:
    return data[word]
    #else:
    #    return "The word doesn't exists in the dataset."

word=input("Enter the word to find it's meaning:")
checkInData=word in data
if checkInData:
    listOfWord=translate(word)
else:
    listOfWord=["The word doesn't exists in the dataset."]
print("'"+word.upper()+"' :")
for i in listOfWord:
        print(i)