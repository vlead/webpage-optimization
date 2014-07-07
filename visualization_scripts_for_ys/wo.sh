#csvcut -c 2 /home/ms/testingframe/yslowNpagspeedGraphs/stats_pagespeed_on.csv | sed "1d"> prac1.csv
FILENAME=$1 # command line input which takes the file containing the names of the rules in the yslow report.
count=0
PATHNAME=$2 # the path to the directory where all the images have to be saved.
CSVPATH=$3 # path to the directory or location where the csv file to be used for plotting is placed.
while read LINE
do    
      count=$(( $count + 1 ))
      if [ "$count" -ge 2 ]
      then 
          csvcut -c $count $CSVPATH | sed "1d" > prac1.csv #1.
          python wo.py prac1.csv "$LINE" "$PATHNAME" #the wo.py is called with the intermediate file,line name,and pathname of where to store the images as an input.
          echo "$count $LINE"
      fi
done < $FILENAME

echo "\nTotal $count Lines read"

#1. csvcut is used to cut the required parts in a csv file. It can be a row or a column. In this case it is a column. The output of the csvcut command is given as an input to the pipeline operator. NOw the sed command is used for deleting the first row in the generated intermediate file which is called as 'prac1.csv'. "1d" implies deleting the first row. 
