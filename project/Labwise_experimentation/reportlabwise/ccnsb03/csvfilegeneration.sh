#function to extract required fields reports previously generated
extractCsv() {
res="URL,Overall_Score,Make fewer HTTP requests,Use a Content Delivery Network (CDN),Avoid empty src or href,Add Expires headers,Compress components with gzip,Put CSS at top,Put JavaScript at bottom,Avoid CSS expressions,Reduce DNS lookups,Minify JavaScript and CSS,Avoid URL redirects,Remove duplicate JavaScript and CSS,Configure entity tags (ETags),Make AJAX cacheable,Use GET for AJAX requests,Reduce the number of DOM elements,Avoid HTTP 404 (Not Found) error,Reduce cookie size,Use cookie-free domains,Avoid AlphaImageLoader filter,Do not scale images in HTML,Make favicon small and cacheable"
while read url; do #loop to read url from 'url' file
  res="$res"$'\n'
  res="$res$url"
  dir=$(echo $url | sed 's/[:/.-]/_/g') #extracting filename 'dir' from 'url'
  res="$res,$(cat $dir | grep -o '[A-Z] ([[:digit:]]*)' | awk -vORS=, '{ print $1 $2 }' | sed 's/,$/\n/')"
done < $1
echo "$res" > stats.csv #redirecting content in 'res' to a csv file named '$dir$csv'
echo "Reports are generated successfully in CSV format"  #echoing script completion       
}

#invoking extracCsv() funtion
extractCsv $1
