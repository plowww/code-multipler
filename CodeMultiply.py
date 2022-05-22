import sys
# TODO: Possibly add file support for .txt docs to make multi-line codes easier to use?

def hexToDec(hex):
    # for each digit right to left
    # map A - F to the corresponding digit, multiply by 16 to the power of its place starting at 0 (loop counter), then add to total
    # 63 = (3 * 16^0) + (6 * 16^1) = 99
    hex = str(hex)
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

def decToHex(dec):
    # for each digit left to right
    #  divide by 16, get remainder, place in digit
    #  Repeat for each resulting number as long as it's above 15, placing each to the left of the last
    #  Once above 15, map and add to final total
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

def codeValueMultiply(code,mul):
    codes = (code.split("\n"))
    for i in range(len(codes)):
        line = codes[i].strip()
        codes[i] = singleLineMultiply(line,mul)
        print(codes[i])
    return codes
    

def singleLineMultiply(string,mul):
    addressValuePair = string.split(" ")
    multipliedHexValue = decToHex(hexToDec(addressValuePair[1]) * mul)
    fullValue = "0"*(len(addressValuePair[1])-len(multipliedHexValue)) + multipliedHexValue
    return addressValuePair[0] + " " + fullValue
    

def main():
    args = sys.argv[1:]
    print("Your args: ")
    print(sys.argv)
    if(len(args)==2):
        print("Printing each line of code multiplied by supplied value...")
        print(codeValueMultiply(args[0],int(args[1])))

if __name__=="__main__":
    main()