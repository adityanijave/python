basic_salary = float(input("enter your basic salary : \n"))
if basic_salary <= 10000 :
    hra = (20*basic_salary )/100
    da = (80*basic_salary)/100
    gross_salary = hra + da + basic_salary
    print("\nGross Salary is : \n" + str(gross_salary))
elif basic_salary <= 20000 :
    hra = (25*basic_salary )/100
    da = (90*basic_salary)/100
    gross_salary = hra + da + basic_salary
    print("\nGross Salary is : \n" + str(gross_salary))
elif basic_salary > 20000 :
    hra = (30*basic_salary )/100
    da = (95*basic_salary)/100
    gross_salary = hra + da + basic_salary
    print("\nGross Salary is : \n" + str(gross_salary))