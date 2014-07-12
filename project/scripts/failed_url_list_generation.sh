#function to create to get results for all urls i
Fulltest() 
{
    while read url; do #loop reads a line from urls file i.e $1 
        echo "Running tests for $url" #echo on outputstream to indicate flow
        file_name=$(echo $url | sed 's/[:/.-]/_/g')       #extracting filename 'file' from 'url'	
        len=$(wc -l $file_name | cut -f1 -d" ") #counting the words in file
        if [ $len -lt 10 ]; then   #check if it is less than 10
	    echo $url >> failed_url_file    #if it is less than 10 words then it is failed report and storing that url into file
	    rm $files              #deleting that file
        fi
    done < $1	#passing 'urls' file as parameter
}

Fulltest $1   #invoking Fulltest() function with command line arguments $1

grep -v -i -f failed_url_file $1 > new_url_file #comparing failed url file and original file and storing active urls  into failed url file
