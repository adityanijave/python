#problem :
'''You're working on a search engine. Watch your back Google!
The given code takes a text and a word as input and passes them to a function called search().
The search() function should return "Word found" if the word is present in the text, or "Word not found", if it's not.
Sample Input "This is awesome" "awesome"
Sample Output Word found'''

#soln:
def search(text,sentance):
    if text  in sentance :
        print("\nWord Found!")
    else :
        print("\nWord Not Found!")


sentance = input("Enter the sentance : ")
text = input("Enter Text : ")

search(text,sentance)