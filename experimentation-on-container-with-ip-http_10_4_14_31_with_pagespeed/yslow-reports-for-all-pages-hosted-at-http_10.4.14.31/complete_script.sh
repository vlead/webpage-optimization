#function to create to get results for all urls i
Fulltest() 
{
while read url; do #loop reads a line from urls file i.e $1 
echo "Running tests for $url" #echo on outputstream to indicate flow
files=$(echo $url | sed 's/[:/.-]/_/g')       #extracting filename 'file' from 'url'	
len=$(wc -l $files | cut -f1 -d" ")
if [ $len -lt 10 ]; then
	echo $url >> failed
	rm $files
fi
done < $1	#passing 'urls' file as parameter
}

Fulltest $1   #invoking Fulltest() function with command line arguments $1

grep -v -i -f failed $1 > tmp
