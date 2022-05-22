This script can be used to multiply the value of any video game code as long as it's written in (address value) pair and print each code it multiplied.
The script requires 2 parameters:
1. The code in question (supports multi-line code too, surround like """line1
                                                                       line2""")
2. The multiplier to use. Should be an integer

For example, assuming you are in the directory of the script...
python CodeMultiply.py "7E220012 007E" 3
The above line will modify this code's value (the 007E part) to be 3 times its value in hex, and print out the modified code for ease of copy and pasting.