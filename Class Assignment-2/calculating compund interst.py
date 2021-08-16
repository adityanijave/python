#problem :
'''     create python to calculate compund interest'''

#soln:
    


p	=	int(input("initial principal balance :"))
r	=	int(input("interest rate :"))
n	=	int(input("number of times interest applied per time period :"))
t	=	int(input("number of time periods elapsed :"))


ci = p*((1+(r/n))**(n*t))
print(ci)