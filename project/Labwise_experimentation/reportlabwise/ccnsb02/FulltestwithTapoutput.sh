#function to create to get results for all urls i
Fulltest() 
{
while read url; do #loop reads a line from urls file i.e $1 
echo "Running tests for $url" #echo on outputstream to indicate flow
dir=$(echo $url | sed 's/[:/.-]/_/g') #extracting filename 'dir' from 'url'	
phantomjs yslow.js --info grade --format tap --threshold '{"overall": "B", "ycdn": 65}' $url > $dir #running phantomjs command with url and redirecting output to a file named $dir
done < $1	#passing 'urls' file as parameter
}

Fulltest $1   #invoking Fulltest() function with command line arguments $1
