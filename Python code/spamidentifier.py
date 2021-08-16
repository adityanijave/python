#spam identifier : 
    
i = input("enter the link or phara  :\n\n ")
i = i.lower()

if ("make a lot money" )in i:
    spam =True
elif( "buy now" )in i : 
    spam = True
elif( "subscribe" )in i :
    spam = True
elif (" click this " )in i :
    spam = True
elif("buy") in i :
      spam = True
else :
    spam = False    

if spam is True :
    print("don't click on the link , it's spam ")
else :
     print (" you can click on the link , it's safe ")
    
    
    
    
############ another method ##################



#spam identifier : 
    
# i = input("enter the link or phara  :\n\n ")
# i = i.lower()


# if (("make a lot money" ) or ( "buy now" ) or ( "subscribe" ) or (" click on this " ) or ("buy")) in i:
#     print("don't click on the link , it's spam ")
# else :
#     print (" you can click on the link , it's safe ")
    
