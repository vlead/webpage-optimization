find $PWD | grep html | cut -b 9- > html_paths.txt #collecting paths for html files in www folder  and storing it into file
find $PWD | grep php | cut -b 9- > php_paths.txt   #collecting paths for php files in www folder  and storing it into file
sed -e 's#^#http://deploy.virtual-labs.ac.in#' html_paths.txt > new_html_paths.txt  #adding domain-name to paths and storing it into file
sed -e 's#^#http://deploy.virtual-labs.ac.in#' php_paths.txt > new_php_paths.txt    #adding domain-name to paths and storing it into file
cat new_php_paths.txt >> new_html_paths.txt #concatenating php paths file to html paths file
sort new_html_paths.txt > finalurls.txt    #sorting the file and storing it into new file 
#deleting all the intermediate files
rm html_paths.txt 
rm php_paths.txt 
rm new_html_paths.txt
rm new_php_paths.txt
