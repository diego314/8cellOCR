# 8cellOCR
OCR document classiffier using the library

The problem that this program was trying to solve was the automation of the scanning and classification of a large number of documents received on paper, each marked with an identifier.

This program reads each scanned file and uses the identifier to create a single pdf file with as many pages as needed for each document. The biggest hurdle the program is designed to solve is the fact that the scanned documents have normaly very low quality (sometimes are scans of a printed document which was scanned from a printed... you get the idea) and therefore some (a lot) flexibility is needed in detecting the identifier, and there are also tools to fix multiple documents incorrectly classified as only one, check for incorrectly recognized identifiers, etc. Such identifier may be located only on the first page of the document (which makes things easier) or on all of them.
