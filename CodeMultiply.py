# Author - Kevin Gomes

# The following script allows easy multiplying of video game code values (typically in address value pairs)
# Mostly for personal use but can be useful for anyone who needs it. Made to be easy to use
# TODO: Possibly modify to either accept command line args OR ask the user for input for easier use?
import sys

# hexToDec takes a hexadecimal string and returns the converted decimal integer
def hexToDec(hex: str):
    # for each digit right to left
    # map A - F to the corresponding digit, multiply by 16 to the power of its place starting at 0 (loop counter), then add to total
    # 63 = (3 * 16^0) + (6 * 16^1) = 99
    total = 0
    digits = {"A": 10,
              "B": 11,
              "C": 12,
              "D": 13,
              "E": 14,
              "F": 15,
              "0": 0,
              "1": 1,
              "2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9}
    
    hex = hex.upper()
    for i in range (0,len(hex)):
        index = (len(hex)-1)-i
        total += digits[hex[index]] * (16**i)
        
    return total

# decToHex takes a decimal integer and returns a string containing the converted hexadecimal number
def decToHex(dec: int):
    # for each digit left to right
    #  divide by 16, get remainder, place in digit (which is a string)
    #  Repeat for each resulting number as long as it's above 15
    #  Once equal or below 15, map and add to final string, then reverse
    hexNumber = ""
    digits = {"10": "A",
              "11": "B",
              "12": "C",
              "13": "D",
              "14": "E",
              "15": "F",
              "0": "0",
              "1": "1",
              "2": "2",
              "3": "3",
              "4": "4",
              "5": "5",
              "6": "6",
              "7": "7",
              "8": "8",
              "9": "9"}
    
    while dec > 15:
        hexNumber += digits[str(dec%16)]
        dec = dec//16
    hexNumber += digits[str(dec)]
    
    return hexNumber[::-1]

# codeValueMultiply takes a potentially multi-line code and multiplier and prints out every line multiplied
def codeValueMultiply(code: str,mul: int):
    codes = (code.split("\n"))
    for i in range(len(codes)):
        line = codes[i].strip()
        print(singleLineMultiply(line,mul))

# singleLineMultiply takes 1 line of hex code (address value pair) and a multiplier (integer) and returns the same code with multiplied value in hex
def singleLineMultiply(line: str,mul: int):
    addressValuePair = line.split(" ")
    multipliedHexValue = decToHex(hexToDec(addressValuePair[1]) * mul)
    fullValue = "0"*(len(addressValuePair[1])-len(multipliedHexValue)) + multipliedHexValue
    return addressValuePair[0] + " " + fullValue

# fileCodeValueMultiply takes a .txt file full of codes that has already been opened for at least read access and an
# integer multipler and prints each line multiplied
def fileCodeValueMultiply(file,mul: int):
    for line in file:
        line = line.strip()
        # If we fail the try, then we have a line that isn't a number aka title of code
        # Otherwise multiply line and print it out
        try:
            print(singleLineMultiply(line,mul))
        # Print title of code if exception
        except:
            print(line)

# The main point of entry
def main():
    # Get our args and print them to the user - do not include the script filename
    args = sys.argv[1:]
    print("Your args: ")
    print(args)
    # If we are in the default mode, we should have 2 args - the code and the multiplier
    if(len(args)==2):
        print("Printing each line of code multiplied by supplied value...")
        codeValueMultiply(args[0],int(args[1]))
        print("Done!")
    # If we have 3 args, we should be in -file mode. Ensure this to be true and read from file
    elif(len(args)==3 and args[0].lower() == "-file"):
        try:
            print("Reading file \"" + args[1] + '"...')
            file = open(args[1],'r')
            fileCodeValueMultiply(file,int(args[2]))
            file.close()
            print("Done! Note that the file given has not been written to for protection of original data.")
        except:
            print("Exception: No such file exists with filename \"" + args[1]+'"')
    # We fail both checks, something is wrong with the arguments
    else:
        print("Either not enough arguments passed or too many arguments passed. Please check and try again.")

if __name__=="__main__":
    main()