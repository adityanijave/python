i = input("")
si = i.split()
#print(si)
# {'Grr':'Lions' ,'Rawr': 'Tigers','Ssss':'Snakes','Chirp':'Birds'}

lc = si.count("Grr")
#print ("lion count :", lc )
tc = si.count("Rawr")
#print("tiger count :", tc)
sc = si.count("Ssss")
#print("Snake count :", sc)
bc = si.count("Chirp")
#print("Bird count :", bc)

if "Grr" in si :
    plcv = ("Lion "*lc)
    # print(plcv)
if "Rawr" in si :
    ptcv = ("Tiger "*tc)
    print(type(ptcv))
if "Ssss" in si :
    pscv = ("Snake "*sc)
    # print(pscv)
if "Chirp" in si :
    pbcv = ("Bird "*bc)
    # print(pbcv)
    
    
print(plcv+pscv+pbcv+ptcv)