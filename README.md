Read RAW file for correct formatting!

This script can be used to multiply the value of any video game code as long as it's written in (address value) pair and print each code it multiplied.
Codes are expected in raw/decrypted format. For whichever device the code is for, there are decryptors online to put back into raw format. Use the raw
code to multiply, then encrypt it again in the same format.
Encrypted codes are unsupported since this script would require too many decryptor algorithms for each code type across the various consoles and code devices.

Example codes are given in ExampleCode.txt to provide use case


The script requires 2 parameters:
1. The code in question (supports multi-line code too)
2. The multiplier to use. Should be an integer

For example, in the command prompt or terminal assuming you are in the directory of the script...
python CodeMultiply.py "7E220012 007E" 3
The above line will modify this code's value (the 007E part) to be 3 times its value in hex, and print out the modified code for ease of copy and pasting.

.txt files are supported using -file mode. Codes are expected in the format:

"Name of code"
code line 1
code line 2

"Name of code"
code line 1
code line 2
...

Any amount of whitespace is fine in between codes or in the code itself, as any line that isn't an (address value) pair will simply be printed back
(whitespace is thus ignored and not printed). All codes from file will NOT be written to the file to avoid
losing the original code. It is instead printed out in easy copy and paste format (the same format as the file gave it) for you to do as you wish.

An example using "ExampleCode.txt" in the command prompt or terminal:
python CodeMultiply -file ExampleCode.txt 3