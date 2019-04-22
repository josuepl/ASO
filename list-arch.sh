ls *.mp3
for archivo in $(find . -type f -name  "*.mp3")
 do 
  echo "archivo $archivo";
 
done
