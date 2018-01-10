"""
by: Noah Bollinger
when: 1/9/2018
what: a0 - Python: Print, List, Dictionary & Git
"""

print("Starting a0 - Python: Print, List, Dictionary & Git")
lncount = 0
with open("complete.csv") as f:
    for line in f:
        lncount += 1
        if lncount < 15:
            print(line[0:10])
            
            
print("done and we found this many lines:", lncount)