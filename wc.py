#user input
sentence = input("Please enter a sentence/paragraph : ")

#algorithm for counting the words
space_count = 0
for character in sentence:
    if character == " ":
        space_count = space_count + 1
number_of_words = space_count + 1

#output given
print("The user entered: ", sentence, sep =" ")
print("The number of words in the sentence is", number_of_words, sep =" ")
