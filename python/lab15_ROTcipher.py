'''
Lab 15 - ROT Cipher
Marcel Schaeffer
10/6/17
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz '
key = 'nopqrstuvwxyzabcdefghijklm '
word = input('Type a word: ') #user types word to encrypt

#encrypts
encrypt = ''
for letter in word:
    code = alphabet.find(letter)
    encrypt += str(key[code])
print(encrypt)

#decrypts
decrypt = ''
for letter in encrypt:
    code = alphabet.find(letter)
    decrypt += str(key[code])
print(decrypt)


