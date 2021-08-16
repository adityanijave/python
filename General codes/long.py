text = input("Enter the line :\n")
print("\n"+str(text))

word = text.split()
print(word)

longest_word = word[0]
print("\nlet's consider it is longest word :\n"+str(longest_word))

print("\nrange of string will be :\n" +str(range(0,len(word))))

for letters in range(0,len(word)):
    if len(longest_word) < len(word[letters]):
        longest_word = word[letters]  
        
print(longest_word)