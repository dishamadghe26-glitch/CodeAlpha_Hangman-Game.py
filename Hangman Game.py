import random

words = ["UMBRELLA","COMPUTER","TELESCOPE","SMARTPHONE"]
word = random.choice(words)
word_letter = list(word)
gussed_word = ['_']*len(word)

total_chances = 7


while total_chances > 0:
    print("\nCurrent word: ","".join(gussed_word))
    letter = input("Gusses a Letter: ").upper()
    if letter in word_letter:
        for index in range(len(word)):
            if word[index] == letter:
                gussed_word[index] = letter
        if "".join(gussed_word) == word:
            print("\nCongratulayions you won..! The word is:",word)
            break
    else:
        total_chances -= 1
        print("Incorrect guess")
        print("the remaining chances are:",total_chances)

else:
    print("\nGame Over")
    print("you lose")
    print("All the chances are exhausted")
    print("the correct word is",word)




