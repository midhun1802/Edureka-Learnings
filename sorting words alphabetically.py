# Program to sort alphabetically the words form a string provided by the user

my_str = "This is my world of love and choice"

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)