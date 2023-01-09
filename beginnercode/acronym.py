e = input("text to make acronym\t\t")
o = 0
arr = []
splitted = e.split()
for word in splitted:
    s = [*word]
    for x in s:
        print(x)
        if o == 0:
            if x.isupper():
                arr.append(x)
            else:
                y = x
                z = y.upper()
                arr.append(z)
            o += 1
        else:
            pass
    o = 0
print(arr)