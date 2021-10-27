word = input("Enter The Word, Please. \n").strip()
length = len(word)
reversedWord = ""
new = ""
while length > 0:
    reversedWord = reversedWord + word[length-1]
    length -= 1
length = len(reversedWord)
while length > 0:
    if reversedWord[length-1] == 'a':
         reversedWord = reversedWord.replace(reversedWord[length-1], '0')  
         
    elif reversedWord[length-1] == 'e':
         reversedWord = reversedWord.replace(reversedWord[length-1], '1')
         
    elif reversedWord[length-1] == 'i':
         reversedWord = reversedWord.replace(reversedWord[length-1], '2')
         
    elif reversedWord[length-1] == 'o':
         reversedWord = reversedWord.replace(reversedWord[length-1], '2')
         
    elif reversedWord[length-1] == 'u':
         reversedWord = reversedWord.replace(reversedWord[length-1], '3')  
    length -= 1
print(reversedWord + "aca")
    



