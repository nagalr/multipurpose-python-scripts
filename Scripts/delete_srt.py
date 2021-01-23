# Script to delete all files ending with .*srt from /Desktop and its subfolders
import os, re, os.path
pattern = ".*srt"
mypath = "/Volumes/MyPassport/Courses/"
for root, dirs, files in os.walk(mypath):
    for file in filter(lambda x: re.match(pattern, x), files):
        os.remove(os.path.join(root, file))