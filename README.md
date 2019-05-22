# Unicode data to key value Array and CSV

To turn Unicode data into CSV and key value arraydo: If you just download the repository use it like a standalone program and type

```console
f@u:~$
f@u:~/yourPATEHtoprogram$ python makenfdlistfromhtml.py
On.
Off.
```

The input is taken from the folder "htmlfromunicodeorg" containing a download of the Unicode character lists of the website

http://www.unicode.org/charts/normalization

# CSV
 The CSV file is ";;" seperated data. The first column is the "Unicode name of combined letter", the second column is the "Unicodenumber for combined character", the third column is the "Unicodeletter combined" and the last column is the "Unicode number of decomposed letter".

# JS Array 
The second output of the program is a key-value Array of NFC (key) to NFD (value) version of the character. 

