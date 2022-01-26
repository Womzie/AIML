word = "knoll"



for j in range(6):
    solved = True

    guess = input("Input word: ")
    if len(guess) != 5:
        guess = input("Make sure the word is 5 letters long: ")

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

