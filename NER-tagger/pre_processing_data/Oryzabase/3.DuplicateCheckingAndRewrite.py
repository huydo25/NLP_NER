temp=[]
with open('pubmed2.txt', 'r') as inputfile:
    lines = inputfile.readlines()
    temp.append(lines)

check_point=0
with open("pubmed_hin.txt", "w") as output:
    for i in range(0, len(temp[0])):
        if temp[0][i] == '\n':
            if check_point == 0:
                a = temp[0][0:i]
                temp_string = ""
                for j in range(0, len(a)):
                    temp_string+=a[j]
                if temp_string.find("B-gene") != -1: 
                    for k in range(0, len(a)):
                        output.write(a[k])
                    output.write("\n")
                check_point = i
            else:
                a= temp[0][check_point+1:i]
                temp_string = ""
                for j in range(0, len(a)):
                    temp_string+=a[j]
                if temp_string.find("B-gene") != -1: 
                    for k in range(0, len(a)):
                        output.write(a[k])
                    output.write("\n")
                check_point = i

