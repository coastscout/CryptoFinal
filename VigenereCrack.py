import re
import os 
import string
from pathlib import Path
#libraries import

def calcGCD(a,b):
    while (b):
        a, b = b, a % b
    return a

def find_most_frequent_character(text):
    letter_counts = {}
    for char in text:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

    most_frequent_char = max(letter_counts, key=letter_counts.get)
    return most_frequent_char

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def char_to_numeric(char):
    if char.isalpha():
        return ord(char.lower()) - ord('a')
    else:
        return None
    
def string_to_numeric_array(input_string):
    return [char_to_numeric(char) for char in input_string]

print ('Instructions: This program finds the estimated keylength of a vigenere cipher between the values of 9 and 16. Enter the file name, such as "ciphertext.txt"\n')
textDoc = input("Enter the file name: ") #grab user input
getDoc = Path(__file__).with_name(textDoc) #sets working directory to the same place as the .py file and allows the user to grab documents from the terminal
enable_keyword_files = False  # Default value

user_input = input("Would you like to enable individual keyword output files? (yes/no): ").lower()

if user_input == "yes":
    enable_keyword_files = True
    print("Individual keyword output files enabled. Processing...")
else:
    print("Individual keyword output files disabled. Processing...")

with open(getDoc, 'r') as i:  
        text = i.read()
        re.sub(r'\W+', '', text)
        finalStr = text.lower()
        #reads file, sets to string, uses re.sub to get rid of all non-alphanumeric characters, converts all characters to lowercase
        
        sampleSize=4 #used later for trying to calculate GCD. Value can be changed to include more or less samples, from 1-9 - higher number = more likely to find most reduced GCD, but also more likely to include garbage value at low ciphertext lengths.
        numShifts=[]
        numMatches=[]
        output = ""
        #create array variables for later use
        
        for shift in range(9,160): #shifts by x - key can be 9 through 16 - this range gives 10 chances for matches to "spike"
            matches = 0
            for n in range(len(finalStr)-shift): #excludes characters that can't be compared due to shift
                if finalStr[n]==finalStr[n+shift]: #compares original string to shifted string
                    matches+=1
            numShifts.append(shift)
            numMatches.append(matches)
            #adds data obtained to array variables
            
        zippedList = zip(numShifts, numMatches) #zips lists together to correlate shift and match numbers
        sortedList = sorted(zippedList, key=lambda x: x[1], reverse=True) #sorts list based on greatest number first
        sortedShifts = [numShifts for numShifts, _ in sortedList] #grabs the shift values themselves out of the zipped list
        sampleList = sortedShifts[:sampleSize] #creates sample list in case of small ciphertext length - not really necessary in this case
        gcd = calcGCD(sampleList[0], sampleList[1])
        for j in range(2, sampleSize):
            gcd = calcGCD(gcd, sampleList[j])
        print("Estimated key length is: ", gcd)
        
        currentDir = os.getcwd()
        binFolder = os.path.join(currentDir, "Bins")
        if not os.path.exists(binFolder):
            os.makedirs(binFolder)
            os.chdir(binFolder)
        print("Current Working Directory:", os.getcwd())
            #makes directory inside current working directory to deposit bin files 
        
        keyword = ""
        
        for k in range(0, gcd):
            for l in range(0, int(len(finalStr)/gcd)):
              output += finalStr[k+(l*gcd)]
            filename = 'output' + str(k) + '.txt'
            #print(output)
            if (enable_keyword_files == True):
                with open(filename, 'w')as f:
                    f.write(output)
                    print("\noutput" + str(k) + ".txt file created")
            keyword += find_most_frequent_character(output)        
            output = ""
            
        
        keyword = caesar(keyword,21)
        print("Keyword is: ", keyword)

        
        # Modify vigArray
        vigArray = string_to_numeric_array(keyword)
        vigArray = [(25 - num) % 26 for num in vigArray]

        # Decrypt the original document using Vigenere cipher
        original_decrypted = ""
        for i, char in enumerate(finalStr):
            if char.isalpha():
                shift = vigArray[i % len(vigArray)]
                original_decrypted += caesar(char, shift)
            else:
                original_decrypted += char

        # Save the decrypted document to "originalDecrypted.txt"
        with open("originalDecrypted.txt", "w") as f:
            f.write(original_decrypted)

        print("Decrypted document saved to 'originalDecrypted.txt \nProcessing complete.'")
        input("\nPress Enter to exit program")
        
         
        
        
        