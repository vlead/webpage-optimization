Fulltest() 
{
count=0
tmp=1
while read url; do #loop reads a line from urls file i.e $1 
echo "Running tests for $url" #echo on outputstream to indicate flow
files=$(echo $url | sed 's/[:/.-]/_/g' | sed 's/ *//g')       #extracting filename 'file' from 'url'	
phantomjs yslow.js --info grade --format tap --threshold '{"overall": "B", "ycdn": 65}' $url > $files &
let count+=tmp;
if [ $count == 10 ]; then
	wait
	count=0
fi
done < $1	#passing 'urls' file as parameter
}

Fulltest $1 
