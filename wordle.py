import random


legal_words = []
with open('legal_words.txt') as f:
    for line in f:
        legal_words.append(line.strip())

word = random.choice(legal_words)
print(word)
#print(legal_words)

for j in range(6):
    solved = True

    guess = input("Input word: ")
    if guess not in legal_words:
        guess = input("Word not allowed: ")

    imperfect = ""
    for i in range(5):
        if word[i] == guess[i]:
            pass
        else:
            imperfect += word[i]


    #print(imperfect)

    correct = ""

    for i in range(5):
        if word[i] == guess[i]:
            correct += "!"

            #print(word)
        elif guess[i] in imperfect:
            correct += "?"
            #remove from imperfect list
            imperfect = imperfect.replace(guess[i], "", 1)
            solved = False

        else:
            correct += "."
            solved = False



    print (correct)
    if solved == True:
        print(f"CORRECT!! The Word was: {word}")
        break

if solved == False:
    print("You did not find the word \n"
          f"The word was: {word}")

