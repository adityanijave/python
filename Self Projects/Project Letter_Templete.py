
selected_persons =["rahul" , "shubham" ,"ruhi" ,"sam" , "akash" ]
name = str(input("Enter your name :\n")).lower()
date = input("Enter today's date :\n")
def letter_tamplete_for_selected_candinates():
    return '''Dear NAME, 
    Congo ! I'm Happy to tell you that you are selected for AdRo-IT and another important thing that is you can login t0 web after 2 days .
    DATE,
    Aditya Nijave.
    ''' 
def letter_tamplete_for_not_selected_candinates():
    return  '''Dear NAME, 
        Bad luck , sorry to say but you are not selected for  AdRo-IT . Better luck next time !
        DATE,
        Aditya Nijave.
        ''' 
if str(name) in selected_persons :     
    final =  letter_tamplete_for_selected_candinates().replace("DATE",date).replace("NAME",name)    
elif str(name) not in selected_persons :
    if name.startswith("a") or name.startswith("m") or name.startswith("y")  or name.startswith("s") :
        selected_persons=selected_persons.append(name)
        final  =letter_tamplete_for_selected_candinates().replace("DATE",date).replace("NAME",name)    
    else :
        final =letter_tamplete_for_not_selected_candinates().replace("DATE",date).replace("NAME",name)
print("\n"+final)

