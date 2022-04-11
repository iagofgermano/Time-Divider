minutes = -1
seconds = -1
numrange = 0
while minutes > 60 or minutes < 0:
    minutes = int(input("Minutes? "))
while seconds > 60 or seconds < 0:
    seconds = int(input("Seconds? "))
numrange = int(input("Up to which number to divide? "))
print("\n")

for i in range(1,numrange + 1):
    prodmin = minutes / i
    prodsec = seconds
    if prodsec > 0:
        prodsec = seconds / i 
    prodsec = prodsec + ((prodmin - int(prodmin)) * 60)
    milliseconds = str(prodsec - int(prodsec))[2:5]
    prodsec = round(prodsec)
    if prodsec < 10:
        prodsec = "0" + str(prodsec)
        
    if milliseconds != '0':
        print(f"\t{int(prodmin)}:{prodsec}:{milliseconds} = time divided by {i}")
    else:
        print(f"\t{int(prodmin)}:{prodsec} = time divided by {i}")