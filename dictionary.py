# Made with love - Akash Singh ♥️
import json
from difflib import get_close_matches # library to compare text(line: 12)

data=json.load(open("dataset.json")) # dataset
data_keys=data.keys() # dataset keys
#print(type(data))
def translate(word):
    word_present=word in data
    if word_present:
        return data[word]
    elif len(get_close_matches(word,data_keys))>0:
        user_correction=input("\nDid you mean %s instead of word? Enter (y/n):" %get_close_matches(word,data_keys)[0])
        if user_correction.lower()=='y':
            return data[get_close_matches(word,data_keys)[0]]
        elif user_correction.lower()=='n':
            print("\nThe word doesn't exists in the dataset.")
            return None
        else:
            print("\nInvalid Entry.")
            return None
    else:
        print("\nThe word doesn't exists in the dataset.")

while True:
    word=input("\nEnter the word to find it's meaning:")
    word=word.lower();
    listOfWord=translate(word)
    if(listOfWord!=None and len(listOfWord)>0):
        for i in listOfWord:
            print("\n"+word.upper()+" :-",end=" ")
            print(i)
        print()
    one_more=input("Do you want to search more meaningful words? (y/n) :")
    if(one_more.lower()!='y'):
        break
    

'''
checkInData=word in data
if checkInData:
    listOfWord=translate(word)
else:
    listOfWord=["The word doesn't exists in the dataset."]

for i in listOfWord:
        print(word.upper()+" :",end=" ")
        print(i)
'''