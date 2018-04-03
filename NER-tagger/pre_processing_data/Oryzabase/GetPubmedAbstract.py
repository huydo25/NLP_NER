# from Bio import Entrez
# from Bio.Entrez import efetch, read
from pubmed_lookup import PubMedLookup, Publication
import re

email1 = "pierre.larmande@ird.fr"
pmid = "10359080"
# NCBI will contact user by email if excessive queries are detected

output = open('./abstract.tsv', 'a')
email = 'pierre.larmande@ird.fr'
url = 'http://www.ncbi.nlm.nih.gov/pubmed/'
counter =  254 #9221 #9237 #9602 #9624  #9954 #9964  #9679  #9723 #9756 #9784 #9836 #9964 #10746

temp = []
with open('./pubmed.tsv','r') as file:
    lines = file.readlines()
    temp.append(lines)

for i in range(10492, len(temp[0])):
    pmid = re.sub('\s', '', temp[0][i])
    lookup = PubMedLookup(url+pmid, email)
    publication = Publication(lookup)
    counter -= 1
    # if (counter != 10452):
#     if (pmid not in ['11779628','14968308']):
    print(counter)
    print(pmid)
    output.write('{pubmed}\t{title}\t{year}\t{journal}\t{abstract}\n'
                 .format(**{
                    'pubmed': pmid,
                    'title': publication.title,
                    'year': publication.year,
                    'journal': publication.journal,
                    'abstract': publication.abstract,
                }))


