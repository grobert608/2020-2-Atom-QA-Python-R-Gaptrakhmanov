FILE=$1
FILE_CAT=$(cat $1)

if [ ! -f "$FILE" ]; then
  echo "$FILE not found"
  exit 1
fi

RESULT="result_parse.txt"

printf "%s %s\n" "total count in log is" "$(wc -l "$FILE" | sed -e 's/^[[:space:]]*//' | cut -d ' ' -f 1)"  > $RESULT

for method in $(awk '{print $6}' "$FILE" | sort | uniq)
do
  printf "%s %s\n" "count of ${method#*\"} is" "$(grep -c "${method#*\"}" "$FILE")" >> $RESULT
done

printf "%s\n" "top ten logs by size:" >> $RESULT
awk ' {print $1, $4, $5, $6, $7, $10}' <<< "$FILE_CAT" | sort -nrk6 | head -10 >> $RESULT

printf "%s\n" "top ten logs of client errors:" >> $RESULT
awk ' { if(($9>=400) && ($9<500)) {  print $1, $6, $7, $9, $10 }}' <<< "$FILE_CAT" | sort -nrk5 | head -10 >> $RESULT

printf "%s\n" "top ten logs of server errors:" >> $RESULT
awk ' { if(($9>=300) && ($9<400)) {  print $1, $6, $7, $9, $10 }}' <<< "$FILE_CAT" | sort -nrk5 | head -10 >> $RESULT