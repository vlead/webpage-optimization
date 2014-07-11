while read line
do
	len=`echo $line | wc -c`
	echo $len
	if [ $len > 70 ]; then
		line >> updated.csv
	fi

done < $1
