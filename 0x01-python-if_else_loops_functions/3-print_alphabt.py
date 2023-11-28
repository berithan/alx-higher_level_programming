#!/usr/bin/python3
# Author - Beritha Niyotwagira
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
