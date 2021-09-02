#problem :
'''open  files and chek whether their contant is
    identical or not
'''
    
#soln:
with open("main.txt") as main :
    reading_contant_of_main_file  = main.read() 
with open("copyofmain.txt") as copy :
    reading_contant_of_copy_file = copy.read()  
if reading_contant_of_main_file  == reading_contant_of_copy_file:
    print("both file contant is identical")
else:
    print("no match found!")