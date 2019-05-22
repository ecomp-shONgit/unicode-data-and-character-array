# Turn Unicode data to key value Array and CSV

If you just download the repository use it like a standalone program and type

python makenfdlistfromhtml.py

The input is taken from the folder containing a download of the Unicode Character Lists of the website

http://www.unicode.org/charts/normalization

# CSV meaning
 The CSV file is ";;" seperated data. The first column is the "Unicode name of combined letter", the second column is the "Unicodenumber for combined character", the third column is the "Unicodeletter combined" and the last column is the "Unicode number of decomposed letter".

# JS Array meaning
The second output of the program is a key-value Array of NFC (key) to NFD (value) version of the character. 

