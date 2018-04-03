import random
import glob
import numpy as np
import pandas as pd
import re
import string as str_lib
import nltk

#define some ultiliser function

def replace(a):
    for i in range(0, len(a)):
        a[i] = a[i].replace("\n",'')
        a[i] = a[i].replace("(",'')
        a[i] = a[i].replace(")",'')
        a[i] = a[i].replace("/",'')
        a[i] = a[i].replace(":",'')
def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        for j in range(len2):
            lcs_temp=0
            match=''
            while ((i+lcs_temp < len1) and (j+lcs_temp<len2) and string1[i+lcs_temp] == string2[j+lcs_temp]):
                match += string2[j+lcs_temp]
                lcs_temp+=1
            if (len(match) > len(answer)):
                answer = match
    return answer
def find_substring(needle, haystack):
    index = haystack.find(needle)
    if index == -1:
        return False
    if index != 0 and haystack[index-1] not in str_lib.whitespace:
        return False
    L = index + len(needle)
    if L < len(haystack) and haystack[L] not in str_lib.whitespace:
        return False
    return True


# list genes in Oryzabase
temp2 =[]
with open('OryzabaseGeneListEn_20171122010121.txt', 'r') as input_file:
    lines = input_file.readlines()
    temp2.append(lines)

#find list of gene
list_gene_temp= []
for k in range(1 ,len(temp2[0])):
    temp2[0][k] = temp2[0][k].lower()
    test = temp2[0][k].split('\t')[1:4]
    for i in range(0, len(test)):
        test[i] = test[i].replace('[','')
        test[i] = test[i].replace(']','')
        test[i] = test[i].replace('*','')
        test1 = test[i].split(',')
        for j in range(0, len(test1)):
            list_gene_temp.append(test1[j])
list_gene=list(set(list_gene_temp))

# print list_gene

#find prefix of a gene
list_gene_name=[]
list_gene_name1= []
list_gene_sym=[]
list_gene_sym1= []
list_gene_symsy=[]
list_gene_symsy1= []
for k in range(1 ,len(temp2[0])):
    temp2[0][k] = temp2[0][k].lower()
    test = temp2[0][k].split('\t')
    for i in range(0, len(test)):
        test[i] = test[i].replace('[','')
        test[i] = test[i].replace(']','')
        test[i] = test[i].replace('*','')
    if len(test) >16:
        list_gene_name.append(test[3])
        list_gene_sym.append(test[2])
        list_gene_symsy.append(test[1])
# print list_test
list_gene_name = list(set(list_gene_name))
list_gene_sym = list(set(list_gene_sym))
list_gene_symsy = list(set(list_gene_symsy))
for k in range(0, len(list_gene_name)-1):
    ans = longestSubstringFinder(list_gene_name[k], list_gene_name[k+1])
    if len(ans) > 5:  
        list_gene_name1.append(ans)

for k in range(0, len(list_gene_sym)-1):
    ans = longestSubstringFinder(list_gene_sym[k], list_gene_sym[k+1])
    if len(ans) > 5:  
        list_gene_sym1.append(ans)
        
for k in range(0, len(list_gene_symsy)-1):
    ans = longestSubstringFinder(list_gene_symsy[k], list_gene_symsy[k+1])
    if len(ans) > 5:  
        list_gene_symsy1.append(ans)     
# print list(set(list_test1))
list_gene_name =[]

for k in range(0, len(list_gene_name1)-1):
    ans = longestSubstringFinder(list_gene_name1[k], list_gene_name1[k+1])
    if len(ans) > 5:  
        list_gene_name.append(ans)
list_gene_name = list(set(list_gene_name))
# print len(list_gene_name)
list_gene_sym =[]
for k in range(0, len(list_gene_sym1)-1):
    ans = longestSubstringFinder(list_gene_sym1[k], list_gene_sym1[k+1])
    if len(ans) > 5:  
        list_gene_sym.append(ans)
list_gene_sym= list(set(list_gene_sym))
# print len(list_gene_sym)
list_gene_symsy =[]       
for k in range(0, len(list_gene_symsy1)-1):
    ans = longestSubstringFinder(list_gene_symsy1[k], list_gene_symsy1[k+1])
    if len(ans) > 5:  
        list_gene_symsy.append(ans)
list_gene_symsy = list(set(list_gene_symsy))
# print len(list_gene_symsy)

# print len(list_gene)
for i in range(0, len(list_gene_name)):
    list_gene.append(list_gene_name[i])
for j in range(0, len(list_gene_sym)):
    list_gene.append(list_gene_sym[j])
for k in range(0, len(list_gene_symsy)):
    list_gene.append(list_gene_symsy[k])
list_gene = list(set(list_gene))
# print list_gene

#filter. 
list_gene_new = []
for i in range(0, len(list_gene)):
    if (len(list_gene[i])>=2):
        list_gene_new.append(list_gene[i])
print len(list_gene_new)

# keep filtering 
for i in range(0, len(list_gene_new)):
    if ((list_gene_new[i].find(')') !=-1) and (list_gene_new[i].find('(') !=-1 )):
        for j in (0, 4):
            if ((list_gene_new[i].find(')') !=-1) and (list_gene_new[i].find('(') !=-1 )):
                list_gene_new[i]=list_gene_new[i].replace(list_gene_new[i][list_gene_new[i].index('('):list_gene_new[i].index(')')+1] , '')
    elif ((list_gene_new[i].find(')') !=-1) or (list_gene_new[i].find('"') !=-1) or (list_gene_new[i].find('=') !=-1 ) or (list_gene_new[i].find(':') !=-1)):
        list_gene_new[i]=list_gene_new[i].replace(list_gene_new[i],'')
    elif list_gene_new[i].find('(') !=-1 :
        list_gene_new[i]=list_gene_new[i].replace(list_gene_new[i][list_gene_new[i].index('('):len(list_gene_new[i])],'')
    else: 
        continue
for i in range(0, len(list_gene_new)):
    if ((list_gene_new[i].find(')') !=-1) or (list_gene_new[i].find('(') !=-1 ) or (list_gene_new[i].find('=') !=-1 )):
        list_gene_new[i] = list_gene_new[i].replace(list_gene_new[i], '')
# print list_gene_new
for i in range(1, len(list_gene_new)-1):
    temp_element = list_gene_new[i].split()
    if (len(temp_element) == 1 ):
        list_gene_new[i] = temp_element[0]
list_gene_new = list(set(list_gene_new))

temp_list= []
for i in range(0, len(list_gene_new)):
    if (len(list_gene_new[i]) >= 2):
        temp_list.append(list_gene_new[i])
list_gene_new = temp_list
# print len(list_gene_new)


#display Oryzabase
df = pd.read_table('./OryzabaseGeneListEn_20171122010121.txt')
print df.get(df.columns)

#create list of abtrast and appendix
temp =[]
for filename in glob.glob('./Oryzabase_dataset/abstract*'):
    temp1 =[]
#     print filename
    with open(filename , 'r') as inputfile:
        lines = inputfile.readlines();
        temp1.append(lines)
    for i in range(0, len(temp1[0])):
        temp.append(temp1[0][i])
print len(temp)      


list_appendix=[]
list_abtract=[]
for i in range(0, len(temp)):
    a = temp[i].split('\t')
    if (len(a[0]) < 10):
        list_abtract.append(temp[i])
    else:
        list_appendix.append(temp[i])
replace(list_appendix)
replace(list_abtract)
# print list_appendix

with open('pubmed1.txt' ,'w') as training_file:    
    string = ""
    for i in range(0, len(list_appendix)):
        list_appendix[i] = list_appendix[i].lower()
        string += list_appendix[i] + " "
    string = string.replace('-',' ')
#     print string
    #start to tag gene in appendix
    for i in range(1, len(list_gene_new)):
        temp_pos = string.find(r'\b'+list_gene_new[i])
        if find_substring(list_gene_new[i], string):
            temp_sequence=list_gene_new[i].split()
            if (len(temp_sequence) <=1 ):
                string = string.replace(list_gene_new[i], list_gene_new[i]+ 'B-gene ')
            else:
    #             print list_gene_new[i]
                temp_string = temp_sequence[0]+'B-gene'
                for j in range(1, len(temp_sequence)):
                    temp_string += ' '+temp_sequence[j]+'I-gene'
    #             print temp_string
                string = string.replace(list_gene_new[i],temp_string)
    #for the rest of data    
    temp_sequence = string.split()
    for j in range(0, len(temp_sequence)):
        if ((temp_sequence[j].find('B-gene') == -1) and (temp_sequence[j].find('I-gene') == -1)):
            temp_sequence[j] = temp_sequence[j] + "_O"
    string = " ".join(temp_sequence)
    temp_sequence = string.split()
    for i in range(0, len(temp_sequence)):
        if (temp_sequence[i].find("_O") !=-1):
            list_element = temp_sequence[i].split('_O')
            a = nltk.pos_tag(nltk.word_tokenize(list_element[0]))
            for j in range(0, len(a)):
                if a[j][0] not in  {'.',',',"'",'"','/','?','>','<','=',"''","``",'@','%','&',';','{','}','[',']' }:
                    training_file.write(a[j][0] + " " + a[j][1] + " O \n")
            if (temp_sequence[i].find(".") !=-1):
                    training_file.write("\n")          
        if (temp_sequence[i].find("B-gene") !=-1):
            list_element = temp_sequence[i].split('B-gene')
            a = nltk.pos_tag(nltk.word_tokenize(list_element[0]))
            for j in range(0, len(a)):
                if a[j][0] not in {'.',',',"'",'"','/','?','>','<','=',"''","``",'@','%','&',';','{','}','[',']' }:
                    training_file.write(a[j][0] + " " + a[j][1] + " B-gene \n")
            if (temp_sequence[i].find(".") !=-1):
                    training_file.write("\n")
                    
        if (temp_sequence[i].find("I-gene") !=-1):
            list_element = temp_sequence[i].split('I-gene')
            a = nltk.pos_tag(nltk.word_tokenize(list_element[0]))
            for j in range(0, len(a)):
                if a[j][0] not in {'.',',',"'",'"','/','?','>','<','=',"''","``",'@','%','&',';','{','}','[',']' }:
                    training_file.write(a[j][0] + " " + a[j][1] + " I-gene \n")
            if (temp_sequence[i].find(".") !=-1):
                    training_file.write("\n")
    training_file.write("\n")


with open('pubmed1.txt', 'a') as training_file:
    for k in range(0, len(list_abtract)):
        temp_sequence1 = list_abtract[k].split('\t')
        if len(temp_sequence1)>4:
#             print temp_sequence1
            string1 = temp_sequence1[1] + ' ' + temp_sequence1[4]
            string1 = string1.replace(',' , '')
            string1 = string1.lower()
            string1 = string1.replace('-',' ')
            # print string1
            string2 = string1 
            for i in range(1, len(list_gene_new)):
                temp_pos = string1.find(r'\b'+list_gene_new[i])
                if find_substring(list_gene_new[i], string1):
    #                 print list_gene_new[i]
                    temp_sequence=list_gene_new[i].split()
                    if (len(temp_sequence) <=1 ):
                        string1 = string1.replace(list_gene_new[i], list_gene_new[i]+ 'B-gene ')
                    else:
            #             print list_gene_new[i]
                        temp_string = temp_sequence[0]+'B-gene'
                        for j in range(1, len(temp_sequence)):
                            temp_string += ' '+temp_sequence[j]+'I-gene'
                        string1 = string1.replace(list_gene_new[i],temp_string)
            #for the rest of data    
            temp_sequence = string1.split()
            for j in range(0, len(temp_sequence)):
                if ((temp_sequence[j].find('B-gene') == -1) and (temp_sequence[j].find('I-gene') == -1)):
                    temp_sequence[j] = temp_sequence[j] + "_O"
            string1 = " ".join(temp_sequence)
    #         print string1

            temp_sequence = string1.split()
            for i in range(0, len(temp_sequence)):
                
                if (temp_sequence[i].find("_O") !=-1):
                    list_element = temp_sequence[i].split('_O')
                    a = nltk.pos_tag(nltk.word_tokenize(list_element[0]))
                    for j in range(0, len(a)):
                        if a[j][0] not in  {'.',',',"'",'"'}:
                            training_file.write(a[j][0] + " " + a[j][1] + " O \n")
                        else: 
                            training_file.write( a[j][0] + " " + a[j][1] + " O O \n")
                    if (temp_sequence[i].find(".") !=-1):
                            training_file.write("\n")          
                if (temp_sequence[i].find("B-gene") !=-1):
                    list_element = temp_sequence[i].split('B-gene')
                    a = nltk.pos_tag(nltk.word_tokenize(list_element[0]))
                    for j in range(0, len(a)):
                        if a[j][0] not in  {'.',',',"'",'"'}:
                            training_file.write(a[j][0] + " " + a[j][1] + " B-gene \n")
                        else: 
                            training_file.write( a[j][0] + " " + a[j][1] + " O O \n")
                    if (temp_sequence[i].find(".") !=-1):
                            training_file.write("\n")

                if (temp_sequence[i].find("I-gene") !=-1):
                    list_element = temp_sequence[i].split('I-gene')
                    a = nltk.pos_tag(nltk.word_tokenize(list_element[0]))
                    for j in range(0, len(a)):
                        if a[j][0] not in  {'.',',',"'",'"'}:
                            training_file.write(a[j][0] + " " + a[j][1] + " I-gene \n")
                        else: 
                            training_file.write( a[j][0] + " " + a[j][1] + " O O \n")
                    if (temp_sequence[i].find(".") !=-1):
                            training_file.write("\n")
                
            training_file.write("\n")


