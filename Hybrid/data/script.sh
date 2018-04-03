#!/bin/bash

outDir1="./output_xml"
if [ -d "$outDir1" ] 
then 
  rm -rf $outDir1 
fi
mkdir $outDir1	

outDir2="./output_tsv"
if [ -d "$outDir2" ] 
then 
  rm -rf $outDir2 
fi
mkdir $outDir2	

files=./input/*
for file in $files 
do
	if [ -f $file ]
	then  
		echo $(basename "$file")
		cat $file | cut -f2,5 $file | POST https://pub.cl.uzh.ch/projects/ontogene/oger/upload/txt/xml > ./output_xml/$(basename "$file")
		cat $file | cut -f2,5 $file | POST https://pub.cl.uzh.ch/projects/ontogene/oger/upload/txt/tsv > ./output_tsv/$(basename "$file")
	fi
done 


