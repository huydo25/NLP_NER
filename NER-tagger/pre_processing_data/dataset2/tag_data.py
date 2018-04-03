import nltk
import numpy
import collections


temp =[]
with open('./data.txt', 'r') as f:
    lines = f.readlines();
    temp.append(lines)
    
title =[]
abstract=[]
list_gene=[]
for i in range(0, len(temp[0])):
    if(temp[0][i].find("|t|") != -1):
        title.append(temp[0][i])
    if(temp[0][i].find("|a|") != -1):
        abstract.append(temp[0][i])
    if( (temp[0][i].find("|a|") ==-1 )and (temp[0][i].find("|t|") ==-1) and (temp[0][i] != "\n")):
        list_gene.append(temp[0][i])

gene=[]
code=[]
for i in range(0, len(list_gene)):
    list_gene[i]=list_gene[i].replace("\n",'')
    a= list_gene[i].split('\t',4)
#     print a
    gene.append(a[0]+" "+a[3])
    code.append(a[0])
list_gene_fil = list(set(gene)) 
list_code= list(set(code))

title[1] = title[1].replace('.\n', '')
abstract[1] = abstract[1].replace('.\n', '')
temp_title = title[1].split("|t|")
# print temp_title
temp_abstract = abstract[1].split("|a|")
# print temp_abstract
temp_title[1] = temp_title[1]+ " "+ temp_abstract[1]
#         print "san pham la: ",temp_title[0]
print temp_title[1]
print temp_title[0]

with open("Biocreative_training.txt", "w") as training_file:
    for j in range(0, len(title)):
        temp_list=[]
        title[j] = title[j].replace('.\n', '')
        abstract[j] = abstract[j].replace('.\n', '')
        temp_title = title[j].split("|t|")
        # print temp_title
        temp_abstract = abstract[j].split("|a|")
        # print temp_abstract
        temp_title[1] = temp_title[1]+ " "+ temp_abstract[1]
#         print "san pham la: ",temp_title[0]
        if (temp_title[0] in list_code):
            for i in range(0, len(list_gene_fil)):
                b= list_gene_fil[i].split(' ', 1)
                temp_pos = temp_title[1].find(b[1])
        #         print temp_pos
                if (temp_title[0] == b[0]):
                    if (temp_pos != -1):
                        temp_list.append(b[1])
        #     print temp_list
        #     print temp_title[1]
            for i in range(0, len(temp_list)):
                temp_sequence1=temp_list[i].split()
                if(len(temp_sequence1) <= 1):
                    temp_title[1] = temp_title[1].replace(temp_sequence1[0],temp_sequence1[0]+'B-gene')
                else:
                    temp_title[1] = temp_title[1].replace(temp_sequence1[0],temp_sequence1[0]+'B-gene')
                    for j in range(1, len(temp_sequence1)):
                        temp_title[1] = temp_title[1].replace(temp_sequence1[j],temp_sequence1[j]+'I-gene')
                temp_seq = temp_title[1].split(' ')
                for j in range(0, len(temp_seq)):
                    if ((temp_seq[j].find('B-gene') == -1) and (temp_seq[j].find('I-gene') == -1)):
                        temp_seq[j] = temp_seq[j] + "_O"
                seq = " ".join(temp_seq)
                c = seq.split()
                print c
                for i in range(0, len(c)):
                    if (c[i].find("B-geneB-") != -1):
                        d = c[i].split("B-geneB-",1)
                        c[i] = c[i].replace(c[i], d[0]+"B-gene")
                    if (c[i].find("I-geneI-") != -1):
                        d = c[i].split("I-geneI-",1)
                        c[i] = c[i].replace(c[i], d[0]+"I-gene")
                seq = " ".join(c)
        else:
            temp_seq = temp_title[1].split(' ')
            for i in range(0, len(temp_seq)):
                temp_seq[i] = temp_seq[i]+ '_O'
            seq = ' '.join(temp_seq)
#         print seq
        temp_sequence = seq.split()
        for i in range(0, len(temp_sequence)):
            if (temp_sequence[i].find("_O") !=-1):
                list_element = temp_sequence[i].split('_O')
                training_file.write(list_element[0] + " O \n")
                if (temp_sequence[i].find(".") !=-1):
                    training_file.write("\n")
    #             print list_element[0] + " O"
            if (temp_sequence[i].find("B-gene") !=-1):
                list_element = temp_sequence[i].split('B-gene')
                training_file.write(list_element[0] + " B-gene \n")
                if (temp_sequence[i].find(".") !=-1):
                    training_file.write("\n")
    #             print list_element[0] + " B-gene"
            if (temp_sequence[i].find("I-gene") !=-1):
                list_element = temp_sequence[i].split('I-gene')
                training_file.write(list_element[0] + " I-gene \n")
                if (temp_sequence[i].find(".") !=-1):
                    training_file.write("\n")
    #             print list_element[0] + " I-gene"
        training_file.write("\n")

