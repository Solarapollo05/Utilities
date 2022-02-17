import json
valid_mode = False

def text_to_hex(string):
    ascii = json.load(open("ASCII/hex.json", "r"))

    output_hex = str("")

    for char in string:
        if char == " ":
            char = "Space"

        hex = ascii[char]
        (hex)
        output_hex = f"{output_hex}{hex}"
    return(output_hex)

def hex_to_text(string):
    ascii = json.load(open("ASCII/ascii.json", "r"))

    output_str = str("")
    strt = int(0)
    hex_list = []
    
    for num in range(int(len(string)/2)): # Split the input into 8-bit hex
        hex_list.append(string[strt : strt + 2])
        strt += 2

    for char in hex_list:
        
        char = ascii[char]
        if char == "Space":
            char = " "
        output_str = f"{output_str}{char}"
    return output_str


while valid_mode == False:
    print(""" ----- Convert between ASCII and HEX ----- 

Type A to convert to ascii, and H to convert to Hexadecimal
""")

    mode = input(" >    ").upper()

    if mode == "A" or mode == "H":
        valid_mode = True
        
    else:
        print("Invalid option.\n")

string = str(input("Enter a string to convert\n >   "))
if mode == "A":
    result = hex_to_text(string)

elif mode == "H":
    result = text_to_hex(string)

print("Converted String:\n",result)
## Convert " " (space) to "Space"