# Joseph Patambag
# August 26, 2024

# 9-16. Python Module of the Week: One excellent resource for exploring the 
# Python standard library is a site called Python Module of the Week. 
# Go to https://pymotw.com and look at the table of contents. 
# Find a module that looks interesting to you and read about it, 
# perhaps starting with the random module.

import base64
import hashlib
import hmac

#Binary Digest: Opening a text file and encode in base64 bytes
with open('./Resources/test.txt', 'rb') as txt:
    body = txt.read()

txtHash = hmac.new(b"the quick brown fox", 
                body, 
                hashlib.sha1)    

digest = txtHash.digest()
print(f"encoded value: {base64.encodebytes(digest)}")