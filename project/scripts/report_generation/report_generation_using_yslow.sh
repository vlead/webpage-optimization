Fulltest() 
{
  count=0 #variable intialized will be used as  counter
  tmp=1
  while read url; do #loop reads a line from urls file i.e $1 
      echo "Running tests for $url" #echo on outputstream to indicate flow
      filename=$(echo $url | sed 's/[:/.-]/_/g')       #extracting filename 'file' from 'url'	
      phantomjs yslow.js --info grade --format tap --threshold '{"overall": "B", "ycdn": 65}' $url > $files & #command to generate report and     will be dumped into file whose name will be $filename
     let count+=tmp; #increment of variable by one
     if [ $count == 10 ]; then #check for mavimum value for count
	  wait
	  count=0    #initialising variable again to zero
     fi
  done < $1	#passing 'urls' file as parameter
}

Fulltest $1 #invoking function with first command line argument
