selling = float(input("enter the selling price :\n"))
cost = float(input("enter the cost price :\n"))
if selling - cost > 0 :
    print("\nyou have made profit!")
elif selling - cost == 0 :
    print("\nyou have made no profit no loss .")
else :
    print("\nyou have made loss!")