temp=[]
with open('pubmed1.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    temp.append(lines)
alphabet = {'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0',"\n"} 
with open('pubmed2.txt','w') as output:
    c = []
    for i in range(0, len(temp[0])):
        a = temp[0][i].split(" ")
        b= list(set(a[0]))
        for j in range(0, len(b)):
            if b[j] not in alphabet:
#                 print a[0], temp[0][i]
                c.append(temp[0][i])
            else: 
                continue
    for i in range(0, len(temp[0])):
        if temp[0][i] not in c:
            output.write(temp[0][i])
        else:
            continue

