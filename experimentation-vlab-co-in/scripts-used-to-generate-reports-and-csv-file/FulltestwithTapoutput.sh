#function to create to get results for all urls i
Fulltest() {
while read url; do #loop reads a line from urls file i.e $1 
	files=$(echo $url | sed 's/[:/.-]/_/g')		#extracting filename 'file' from 'url'	
	echo "Running tests for $url"			#echo on outputstream to indicate flow
	phantomjs yslow.js --info grade --format tap --threshold '{"overall": "B", "ycdn": 65}' $url > $files #running phantomjs command with url and redirecting output to a file named $file
done < $1	#passing 'urls' file as parameter
}

Fulltest $1 #invoking Fulltest() function with command line arguments $1
