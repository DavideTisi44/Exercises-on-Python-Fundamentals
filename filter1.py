ls = ["uno" , "" , "due" , "tre" , "" , "" , "" , " " , "  " , "fine"]

def nv(ls):
    l1 = []

    for i in ls:
        if len(i.strip())!=0:
            l1.append(i)
    return l1

print(nv(ls))

