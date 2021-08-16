#problem :
'''You aren't paying attention and you accidentally type a bunch of random letters on your keyboard.
 You want to know if you ever typed the same letter twice, or if they are all unique letters.

*Task: If you are given a string of random letters, your task is to evaluate whether
any letter is repeated in the string or if you only hit unique keys while you typing.
*Input Format: A string of random letter characters (no numbers or other buttons were pressed).
*Output Format: A string that says 'Deja Vu' if any letter is repeated in the input string,
or a string that says 'Unique' if there are no repeats.
*Sample Input: aaaaaaaghhhhjkll
*Sample Output: Deja Vu
'''

#sol :
i = input("")
w = []
m = []
s = set()
for j in i :
    w.append(j)
for k in w :
    c = w.count(k)
    m.append(c)
for l in m :
    if l >1 :
        s.add("d")
    else :
        s.add("u")
if "d" in s:
    print("Deja Vu")
else :
    print("Unique")