#!/usr/bin/env python
import sys

with open('theme') as f:
    lines = f.readlines()
    f.close()

ff = open('Emoticons.plist', 'w')

ff.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
ff.write("<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n")
ff.write("<plist version=\"1.0\">\n")
ff.write("<dict>\n")
ff.write("<key>Emoticons</key>\n")
ff.write("<dict>\n")

for line in lines:
    if not (("=" in line) or line.startswith("#") or line.isspace() or line.startswith("[")): #ignore anything that's not an emote definition
        words = line.split()
        if (words[0] == "!"):
            words.pop(0) # pop off the exclamation point if there is one
        ff.write("<key>")
        ff.write(words.pop(0)) # pop off the emote file
        ff.write("</key>\n<dict>\n<key>Equivalents</key>\n<array>\n")
        for word in words:
            ff.write("<string>")
            ff.write(word) # write the emote triggers
            ff.write("</string>\n")
        ff.write("</array>\n<key>Name</key>\n<string>")
        ff.write(words.pop(0)) # pop off the first emote trigger string as name
        ff.write("</string>\n</dict>\n")

ff.write("</dict>\n<key>AdiumSetVersion</key>\n<integer>1</integer>\n</dict>\n</plist>")
ff.close
print ("Emotes file converted to dictionary.")
