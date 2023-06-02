def palindrome_checker(word):
    word = word.lower().replace(" ", "").replace(",", "").replace(".", "")
    return word == word[::-1] #Reverses the String

user_input = input("Enter a word or phrase: \n")
if palindrome_checker(user_input):
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
