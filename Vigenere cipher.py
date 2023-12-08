# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:55:40 2023

@author: Cowen
"""
import collections

def shiftedArrays(arraytoshift):
    allshiftedarrays = []
    min = 9
    max = 17

    for i in range(min, max):
        shiftedarray = [0] * len(arraytoshift)
        for j in range(len(arraytoshift)):
            if j >= i:
                shiftedarray[j] = arraytoshift[j - i]
        allshiftedarrays.append(shiftedarray)
    return allshiftedarrays

def findMatches(theshiftedarrays, thenonshiftedarray):
    iterations = 0
    matchesvalues = []
    samevalues = 0
    while iterations < 8:
        for x in range(len(thenonshiftedarray)):
            if (theshiftedarrays[iterations][x] == thenonshiftedarray[x]):
                samevalues = samevalues + 1
        matchesvalues.append(samevalues)
        iterations = iterations + 1
        samevalues = 0
    return matchesvalues

def findKeyLength(arrayofmatches):
    maxvalue = arrayofmatches.index(max(arrayofmatches))
    return maxvalue + 9

def splitLines(keyLength, originalarray):
    bins = []
    for i in range(keyLength):
        bin = []
        for letter in range(i, len(originalarray), keyLength):
            bin.append(originalarray[letter])
        bins.append(bin)
    return bins

def frequency_analysis(bin_of_letters):
    frequencies = collections.Counter(bin_of_letters)
    most_common = frequencies.most_common(1)[0][0]
    shift = ord(most_common) - ord('E')  # Assuming 'E' is the most frequent letter in English
    return chr((shift + 26) % 26 + ord('A'))

def find_decryption_key(bins):
    key = ''
    for bin in bins:
        key += frequency_analysis(bin)
    return key

def decrypt_vigenere(cipher_text, key):
    orig_text = []
    key_index = 0
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[key_index]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
        key_index = (key_index + 1) % len(key)
    return "".join(orig_text)

def find_cga_and_following(text):
    index = 0
    results = []
    while index < len(text):
        index = text.find('CGA', index)
        if index == -1:
            break
        if index + 14 <= len(text):  # Check if there are enough characters after 'CGA'
            results.append(text[index:index+14])  # 'CGA' + 11 characters
        index += 3  # Move past the current 'CGA'
    return results

# Read the file
file = open("ciphertext.txt", "r")
data = file.read()
characterlist = [letter for letter in data if letter.isalpha()]  # Filter out non-alphabetic characters

print("To change the file, open this script in the IDE of your choice and edit the open function on line 53.\n")
result = shiftedArrays(characterlist)
indexes = findMatches(result, characterlist)
actualkeyLength = findKeyLength(indexes)
print(f"The estimated key length is {actualkeyLength}.")
bins = splitLines(actualkeyLength, characterlist)

decryption_key = find_decryption_key(bins)
print(f"Estimated Key: {decryption_key}")

decrypted_message = decrypt_vigenere(''.join(characterlist), decryption_key)
#print("Decrypted Message: ", decrypted_message)

# Find 'CGA' and the following 11 characters
cga_results = find_cga_and_following(decrypted_message)
print("Occurrences of 'CGA' followed by 11 characters: ", cga_results)

file.close()
