import nltk

temp =[]
#read data in
with open('./BioC2_data.in' ,'r') as input_file:
    lines = input_file.readlines()
    temp.append(lines)
#read ground truth in
temp1 = []
with open('./BioC2_GENE_GT.eval', 'r') as gt:
    lines = gt.readlines()
    temp1.append(lines)

list_genes = []
list_sentence_id = []
for i in range(0, len(temp1[0])):
    a= temp1[0][i].split("|")
    a[2]=a[2].replace('\n','')
    list_genes.append(a[0]+" "+a[2])
    list_sentence_id.append(a[0])
# print list_genes
# print list_sentence_id

with open('train.txt', 'w') as training_file:
    for num in range(0,len(temp[0])):
        a = temp[0][num] 
        a = a.replace('\n','')
        list_genes_fil = list(set(list_genes))
        temp_sequence = a.split(' ', 1)
    #     print temp_sequence[1]
        if (temp_sequence[0] in list_sentence_id):
            for i in range(0, len(list_genes_fil)):
                b= list_genes_fil[i].split(' ', 1)
                temp_pos = temp_sequence[1].find(b[1])
                if (temp_sequence[0] == b[0]):
                    if (temp_pos != -1):
                        temp_sequence1 = b[1].split()
                        list_element = temp_sequence[1].split()
                        if(len(temp_sequence1) <= 1):
                        #  print temp_sequence1[0]
                            temp_sequence[1] = temp_sequence[1].replace(temp_sequence1[0],temp_sequence1[0]+'B-gene')
                        else:
                            temp_sequence[1] = temp_sequence[1].replace(temp_sequence1[0],temp_sequence1[0]+'B-gene')
                            for j in range(1, len(temp_sequence1)):
                                temp_sequence[1] = temp_sequence[1].replace(temp_sequence1[j],temp_sequence1[j]+'I-gene')
                        temp_seq = temp_sequence[1].split(' ')
                        for j in range(0, len(temp_seq)):
                            if ((temp_seq[j].find('B-gene') == -1) and (temp_seq[j].find('I-gene') == -1)):
                                temp_seq[j] = temp_seq[j] + "_O"
                        seq = " ".join(temp_seq)                  
        # in case not exist gene/protein       
        else:
            temp_seq = temp_sequence[1].split(' ')
        #     print temp_seq
            for i in range(0, len(temp_seq)):
                temp_seq[i] = temp_seq[i]+ '_O'
            seq = ' '.join(temp_seq)
    #     print seq
        temp_sequence = seq.split()
        for i in  range(0, len(temp_sequence)):
            if (temp_sequence[i].find("_O") !=-1):
                list_element = temp_sequence[i].split('_O')
                training_file.write(list_element[0] + " O \n")
    #             print list_element[0] + " O"
            if (temp_sequence[i].find("B-gene") !=-1):
                list_element = temp_sequence[i].split('B-gene')
                training_file.write(list_element[0] + " B-gene \n")
    #             print list_element[0] + " B-gene"
            if (temp_sequence[i].find("I-gene") !=-1):
                list_element = temp_sequence[i].split('I-gene')
                training_file.write(list_element[0] + " I-gene \n")
    #             print list_element[0] + " I-gene"
        training_file.write("\n")

