"""
Phone Number Extraction Module

This module specializes in extracting Iranian mobile and landline phone numbers
from text with support for:
- Multiple phone number formats (with/without country code)
- Persian and Arabic numeral systems (۰-۹, ٠-٩)
- Iranian area codes for landline numbers
- Flexible formatting (spaces, parentheses, hyphens)

The module normalizes all extracted numbers to standard Iranian format (0XXXXXXXXXX).

Functions:
    num2en(string): Converts Persian/Arabic numerals to English
    getMobiles(string): Extracts mobile phone numbers (09XXXXXXXXX format)
    getLandlineNumbers(string): Extracts landline numbers with area codes

Example:
    >>> from info.number import getMobiles
    >>> text = "تماس با ۰۹۱۲۳۴۵۶۷۸۹"
    >>> mobiles = getMobiles(text)
    >>> print(mobiles)  # ['09123456789']
"""

import re
import os

# Read the area codes from the file
with open(os.getcwd() + '/info/AreaCodes.txt', 'r') as file:
    area_codes = [line.strip() for line in file]

# Construct the regular expression pattern for landline numbers
area_code_pattern = '|'.join(area_codes)
landline_regex = re.compile(
    r'(?:(?:\+?98|0{0,2}98|0)[\s()-]* ' + area_code_pattern + r')?[\s()-]*(?:\d[\s()-]*){11}|(?:\d[\s()-]*){8}',
    re.IGNORECASE)

mobileReg = re.compile(r'(?:\+98|0{0,2}98|0)?[\s()-]*9\d[\s()-]*(?:\d[\s()-]*){8}', re.IGNORECASE)
junkReg = re.compile(r'[^\d]')
persianNum = ['\u06F0', '\u06F1', '\u06F2', '\u06F3', '\u06F4', '\u06F5', '\u06F6', '\u06F7', '\u06F8', '\u06F9']
arabicNum = ['\u0660', '\u0661', '\u0662', '\u0663', '\u0664', '\u0665', '\u0666', '\u0667', '\u0668', '\u0669']


def num2en(string):
    string = str(string)  # Ensure the input is a string
    for i in range(10):
        string = string.replace(persianNum[i], str(i)).replace(arabicNum[i], str(i))
    return string


def getMobiles(string):
    string = num2en(string)
    mobiles = re.findall(mobileReg, string) or []
    mobiles = [re.sub(junkReg, '', mobile) for mobile in mobiles]
    mobiles = ['0' + mobile[-10:] for mobile in mobiles]
    return mobiles


def getLandlineNumbers(string):
    string = num2en(string)
    # Remove all phone numbers
    string = re.sub(mobileReg, '', string)
    landline_numbers = re.findall(landline_regex, string) or []
    landline_numbers = [re.sub(junkReg, '', landline) for landline in landline_numbers]
    landline_numbers = ['0' + landline[-10:-8] + landline[-8:] if landline[-10:-8] in area_codes else landline[-8:] for
                        landline in landline_numbers]
    return landline_numbers

# test
# print(getMobiles("jafang 0 91 2 (123) 45-67 jafang or +۹۸ (۹۱٤) ۸۰ ۸۰   ۸۸۸ gjgj  +9122873479"))
# print(getLandlineNumbers("jafang 0 21 666 23 5331 djj 6623 53(3) 12 jafang or +۹۸ (۹۱٤) ۸۰ ۸۰   ۸۸۸ gjgj  +91228734793"))
