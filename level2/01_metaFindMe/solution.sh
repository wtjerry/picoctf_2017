echo "look for lat and long in meta info of image and paste into the following flag template"
cat image.jpg| grep -a flag | grep -ao "flag is .*\."
