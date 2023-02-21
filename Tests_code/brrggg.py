#Example requires to get what is the higher number a specific color (red, green or blue) will get if blue gets only 1 number, red 2
#and green 3. for example:  1: blue  || 2: red  || 3: red  || 4: green || 5: green  || 6: green  || 7: blue... and so on.
#this code will provide the answer and allows user to know which is the higher number for each color at the end of the cycle. 


arr = []
lr = 0
lb = 0 
lg = 0
ctm = 0
ct = 1
try:
    ctr = int(input("initial value\t"))
    mxnum = int(input("How much numbers do you want to analyze?\t\t"))
    approve = 1
except:
    print("err")
    approve = 0

if approve == 1:
    while ctr <= mxnum:
        if ct == 1:
            arr.append(f"b {ctr}")
            ct += 1
            print(f"b{ct} || {ctr}")
            lb = ctr
            ctr += 1
        elif ct == 2:
            arr.append(f"r {ctr}")
            ctm += 1
            if ctm > 1:
                ct += 1
                ctm = 0
            print(f"r{ct} || {ctr}")
            lr = ctr
            ctr += 1
        elif ct == 3:
            arr.append(f"g {ctr}")
            ctm += 1
            if ctm > 2:
                ct = 1
                ctm = 0
            print(f"g{ct} || {ctr}")
            lg = ctr
            ctr += 1
    print(f"Last Blue: {lb} || last red: {lr} || last green: {lg}")
    try:
        if int(input("Do you want to see the array? 1: yes || 0 no\t\t")) == 1:
            print(arr)
        else:
            pass
    except:
        pass
else:
    pass
