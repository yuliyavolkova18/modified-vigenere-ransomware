# modified-vigenere-ransomware
**About**

Python program that handles .txt, .py, .docx, and .pdf files and encrypts/decrypts them with an expanded Vigenère cipher in the specified directory with a specified key.

The classical Vigenère cipher operates within the Vigenère square, a 26x26 matrix of either uppercase or lowercase English characters. The modified Vigenère cipher presented expands the operation to a matrix of 95x95, working with characters within the ASCII bound 32-126 (' ' to '~'). The modified variant works well against common cipher identification, Vigenère cipher crackers, and frequency analysis tools. 


**Requirements**
- Python >3.7
- docx: `pip install python-docx`
- PyMuPDF: `pip intall PyMuPDF`

**Launching**
1. `git clone https://github.com/yuliyavolkova18/modified-vigenere-ransomware`
2. `python modified-vigenere-ransomware`

**Vigenère reading**
- Vigenere cipher (2023) *Javatpoint.* 
[https://www.javatpoint.com/vigenere-cipher](https://www.javatpoint.com/vigenere-cipher)
- Deshmukh, S. (2016) *Vigenère Score for Malware Detection, SJSU ScholarWorks.* 
[https://scholarworks.sjsu.edu/etd_projects/487/](https://scholarworks.sjsu.edu/etd_projects/487/)

**Future fixes**

 1. Encryption/decryption of longer .docx and .pdf files and files containing images partially breaks due to mistranslations occurring during decoding.
 2.  Tabbed texts such as in .py files accidentally reveal key. 
