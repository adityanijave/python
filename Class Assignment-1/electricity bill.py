unit_of_coustmer = float(input("Enter your units :\n"))
if unit_of_coustmer <= 50 :
    unit_per_charge_is = 0.50
    billing = unit_of_coustmer * unit_per_charge_is
    extra_charge = ( billing * 20) /100
    net_bill = extra_charge + billing
    print("\nNet bill :\n"+str(net_bill))
elif unit_of_coustmer <= 150 :
    unit_per_charge_is = 0.75
    billing = unit_of_coustmer * unit_per_charge_is
    extra_charge = ( billing * 20) /100
    net_bill = extra_charge + billing
    print("\nNet bill :\n"+str(net_bill))
elif unit_of_coustmer <= 250 :
    unit_per_charge_is = 1.20
    billing = unit_of_coustmer * unit_per_charge_is
    extra_charge = ( billing * 20) /100
    net_bill = extra_charge + billing
    print("\nNet bill :\n"+str(net_bill))
elif unit_of_coustmer > 250 :
    unit_per_charge_is = 1.50
    billing = unit_of_coustmer * unit_per_charge_is
    extra_charge = ( billing * 20) /100
    net_bill = extra_charge + billing
    print("\nNet bill :\n"+str(net_bill))